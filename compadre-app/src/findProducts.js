import axios from "axios";
import priceParser from "price-parser"
import parsePrice from "parse-price"
import {amazonUrl, brainUrl, compareUrl, facebookMarketPlaceUrl} from "@/constant.js";

function formatPrice(price) {
    const parsedPrice = priceParser.parseFirst(price);
    return Math.max(parsedPrice ? parsedPrice.floatValue : 0, parsePrice(price));
}

export const findProducts = {
    methods: {
        findProducts: async function (image, cityName, updateDataState) {
            let results = [];

            try {
                const description = await this.getImageDescription(image);
                updateDataState({descriptionLoaded: true});

                const facebookMarketplaceResults = this.getFacebookMarketplaceProducts(description, cityName);
                const amazonResults = this.getAmazonProducts(description, cityName);
                results = await this.fetchAllProducts(facebookMarketplaceResults, amazonResults);
                updateDataState({adsLoaded: true});

                results = await this.rankProducts(image, results);
                updateDataState({rankingCompleted: true});

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
                }
            }).catch((error) => {
                throw new Error("Generate query failed")
            });
            let description = response.data.description;
            description = description.replace(/[.,\/#!$%\^&\*;:{}=\-_`~()]/g,"");
            description = description.toLowerCase();

            return description;
        },
        getFacebookMarketplaceProducts: async function (description, cityName) {
            return axios.get(facebookMarketPlaceUrl, {
                params: {
                    city: cityName,
                    query: description
                }
            }).catch((error) => {
                throw new Error("Facebook query failed")
            });
        },
        getAmazonProducts: async function (description) {
            return axios.get(amazonUrl, {params: {query: description}}).catch((error) => {
                throw new Error("Amazon query failed")
            });
        },
        fetchAllProducts: async function (facebookMarketplaceResults, amazonResults) {
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
        rankProducts: async function (image, products) {
            const formData = new FormData();
            formData.append("file", image);
            formData.append("payload", JSON.stringify({image_list: products}));
            const response = await axios.post(compareUrl, formData, {
                headers: {
                    "Content-Type": "multipart/form-data"
                }
            }).catch((error) => {
                throw new Error("Compare query failed")
            });
            response.data.response.sort((a, b) => {
                if ( a.MSE < b.MSE ){
                    return -1;
                }
                if ( a.MSE > b.MSE ){
                    return 1;
                }
                return 0;
            });
            console.log(response.data.response);
            return response.data.response;
        },
    }
}
