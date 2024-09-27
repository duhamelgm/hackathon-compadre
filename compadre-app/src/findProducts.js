import axios from "axios";
import priceParser from "price-parser"
import parsePrice from "parse-price"
import {amazonUrl, brainUrl, facebookMarketPlaceUrl} from "@/constant.js";

function formatPrice(price) {
    const parsedPrice = priceParser.parseFirst(price);
    const result = Math.max(parsedPrice ? parsedPrice.floatValue : 0, parsePrice(price));
    return result;
}

export const findProducts = {
    methods: {
        findProducts: async function (image, cityName, updateDataState) {
            const results = [];

            try {
                const description = await this.getImageDescription(image);
                updateDataState({descriptionLoaded: true});

                const facebookMarketplaceResults = this.getFacebookMarketplaceProducts(description, cityName);
                const amazonResults = this.getAmazonProducts(description, cityName);
                await Promise.all([facebookMarketplaceResults, amazonResults]).then((responses) => {
                    debugger
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
                updateDataState({adsLoaded: true});
                return results;
            } catch (error) {
                updateDataState({errorOccurred: true})
                return results;
            }
        },
        getImageDescription: async function (image) {
            const formData = new FormData();
            formData.append("file", image);
            const response = await axios.post(brainUrl, formData, {
                headers: {
                    "Content-Type" : "multipart/form-data"
                }}).catch();
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
