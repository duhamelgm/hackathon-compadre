import axios from "axios";

axios.defaults.headers.common['Access-Control-Allow-Origin'] = '*' // for all requests

export const brainUrl = "https://compadre-image-recognition-e711182a825b.herokuapp.com/compadre-image-recognition/generate";
export const compareUrl = "https://compadre-image-recognition-e711182a825b.herokuapp.com/compadre-image-recognition/compare";
export const facebookMarketPlaceUrl = "https://214a-2001-18c0-24-9b00-6d15-f928-ebc8-6051.ngrok-free.app/crawl_facebook_marketplace";
export const amazonUrl = "https://214a-2001-18c0-24-9b00-6d15-f928-ebc8-6051.ngrok-free.app/crawl_amazon";
