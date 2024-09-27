export const findProducts = {
    methods: {
        findProducts: async function (file, cityName) {
            const description = await this.getImageDescription(file);
            const facebookMarketplaceResults = await this.getFacebookMarketplaceProducts(description, cityName);
            const amazonResults = await this.getAmazonProducts(description, cityName);
            const results = facebookMarketplaceResults.concat(amazonResults);
            console.log(results);
            return results;
        },
        getImageDescription: async function (file) {
            await new Promise(resolve => setTimeout(resolve, 1000));
            return "brown sofa comfortable leather used"
        },
        getFacebookMarketplaceProducts: async function (description, cityName) {
            await new Promise(resolve => setTimeout(resolve, 1000));
            return [
                {
                    "name": "MacBook Pro",
                    "price": "700 $US",
                    "location": "nyc",
                    "title": "MacBook Pro",
                    "image": "https://scontent-yyz1-1.xx.fbcdn.net/v/t45.5328-4/461437584_1033091461699714_4833654038005810545_n.jpg?stp=c0.43.261.261a_dst-jpg_p261x260&_nc_cat=103&ccb=1-7&_nc_sid=247b10&_nc_ohc=GEmcbveYAvwQ7kNvgEmFH0m&_nc_ht=scontent-yyz1-1.xx&_nc_gid=AmSt-7DavXtHf7hGB8qGpBN&oh=00_AYDMVqto8awtaNaHN-yTv3qbshyvORH8_Er47H18p9a0Sw&oe=66FBF343"
                }
            ];
        },
        getAmazonProducts: async function (description, cityName) {
            await new Promise(resolve => setTimeout(resolve, 1000));
            return [
                {
                    "name": "MacBook Pro",
                    "price": "700 $US",
                    "location": "nyc",
                    "title": "MacBook Pro",
                    "image": "https://scontent-yyz1-1.xx.fbcdn.net/v/t45.5328-4/461437584_1033091461699714_4833654038005810545_n.jpg?stp=c0.43.261.261a_dst-jpg_p261x260&_nc_cat=103&ccb=1-7&_nc_sid=247b10&_nc_ohc=GEmcbveYAvwQ7kNvgEmFH0m&_nc_ht=scontent-yyz1-1.xx&_nc_gid=AmSt-7DavXtHf7hGB8qGpBN&oh=00_AYDMVqto8awtaNaHN-yTv3qbshyvORH8_Er47H18p9a0Sw&oe=66FBF343"
                }
            ];
        },
    }
}
