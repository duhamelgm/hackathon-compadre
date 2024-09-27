import axios from "axios";
import priceParser from "price-parser"
import parsePrice from "parse-price"

axios.defaults.headers.common['Access-Control-Allow-Origin'] = '*' // for all requests

const brainUrl = "https://compadre-image-recognition-e711182a825b.herokuapp.com/compadre-image-recognition/generate";
const facebookMarketPlaceUrl = "http://192.168.0.187:8000/crawl_facebook_marketplace";
// const amazonUrl = "https://35e8-2001-18c0-24-9b00-6d15-f928-ebc8-6051.ngrok-free.app/crawl_amazon";
const amazonUrl = "http://192.168.0.187:8000/crawl_amazon";

function formatPrice(price) {
    const parsedPrice = priceParser.parseFirst(price);
    const result = Math.max(parsedPrice ? parsedPrice.floatValue : 0, parsePrice(price));
    return result;
}

export const findProducts = {
    methods: {
        findProducts: async function (image, cityName) {
            const description = await this.getImageDescription(image);
            const facebookMarketplaceResults = this.getFacebookMarketplaceProducts(description, cityName);
            const amazonResults = this.getAmazonProducts(description, cityName);
            const results = [];
            await Promise.all([facebookMarketplaceResults, amazonResults]).then((responses) => {
                responses.forEach((response) => {
                    if (response.config.url === facebookMarketPlaceUrl) {
                        response.data.forEach((product) => {
                            const result = {
                                name: product.title,
                                price: formatPrice(product.price),
                                currency: "$CAD",
                                imageUrl: product.image,
                                url: "facebook.com" + product.link,
                                source: product.source,
                            };
                            results.push(result);
                        });
                    } else if (response.config.url === amazonUrl) {
                        response.data.forEach((product) => {
                            const result = {
                                name: product.title,
                                price: formatPrice(product.price),
                                currency: "$CAD",
                                imageUrl: product.image,
                                url: product.link,
                                source: product.source,
                            };
                            results.push(result);
                        });
                    } else {
                        console.error("Unknown url")
                        console.error(response)
                    }
                });
            });

            return results;
        },
        getImageDescription: async function (image) {
            const formData = new FormData();
            formData.append("file", image);
            const response = await axios.post(brainUrl, formData, {
                headers: {
                    "Content-Type" : "multipart/form-data"
                }});
            let description = response.data.description;
            description = description.replace(/[.,\/#!$%\^&\*;:{}=\-_`~()]/g,"");
            description = description.toLowerCase();

            return description;
        },
        getFacebookMarketplaceProducts: async function (description, cityName) {
            return axios.get(facebookMarketPlaceUrl, {params: {city: cityName, query: description}});
        },
        getAmazonProducts: async function (description) {
            return axios.get(amazonUrl, {params: {query: description}});
        },
    }
}
