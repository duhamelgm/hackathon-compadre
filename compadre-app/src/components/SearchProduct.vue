<script setup>
import ProductsList from "./ProductsList.vue";
</script>

<template>
  <div class="container">
    <div class="image-file-input">
      <figure class="is-flex" v-if="imagePreview">
        <img :src="imagePreview" alt="Image preview" style="max-width: 300px; max-height: 300px;" />
      </figure>

      <div class="file is-info is-boxed" :style="{ opacity: loading ? 0.2 : 1 }">
        <label class="file-label">
          <input class="file-input" type="file" name="product" @change="handleProductUpload" />
          <span class="file-cta">
            <span class="file-icon">
              <i class="fas fa-cloud-upload-alt"></i>
            </span>
            <span class="file-label">{{ file && (!dataState.descriptionLoaded || !dataState.adsLoaded ||
              !dataState.rankingCompleted) ? "Uploading..." : "Upload a photo" }}</span>
          </span>
        </label>
      </div>
    </div>

    <div v-if="file && (!dataState.descriptionLoaded || !dataState.adsLoaded || !dataState.rankingCompleted)"
      class="is-flex is-flex-wrap-wrap">
      <progress class="progress is-medium is-info ml-2 mr-2" max="100" />
      <section class="hero pb-6">
        <div class="hero-body pt-2">
          <p class="title">We're working on recommendations for you!</p>
          <p class="subtitle mt-4"><i v-if="dataState.descriptionLoaded"
              class="has-text-success fas fa-check-square mr-3" /><span v-else class="loader mr-2" />Processing the
            images informations.
          </p>
          <p class="subtitle mt-2"><i v-if="dataState.adsLoaded"
              class="has-text-success fas fa-check-square mr-3" /><span v-else class="loader mr-2" />Comparing with the
            online listings.
          </p>
          <p class="subtitle mt-2"><i v-if="dataState.rankingCompleted"
              class="has-text-success fas fa-check-square mr-3" /><span v-else class="loader mr-2" />Finding the top
            recommendations.</p>
        </div>
      </section>
    </div>

    <div v-if="file && dataState.descriptionLoaded && dataState.adsLoaded && dataState.rankingCompleted"
      class="is-flex is-flex-direction-row">
      <div class="is-flex is-align-items-center" :style="{ gap: '2em' }">
        <div class="is-flex">
          <ProductsList :products="products" v-if="products.length > 0" />
        </div>
      </div>
    </div>
  </div>
</template>

<style>
.container {
  max-width: 800px;
  margin: auto;
  display: flex;
  flex-direction: row;
  margin-top: 2rem;
  max-height: 100vh;
  overflow: hidden;
  gap: 2rem;
}

@media (max-width: 1024px) {
  .container {
    flex-direction: column;
    overflow: scroll;
  }

  .image-file-input {
    margin: auto;
  }
}

.image-file-input {
  display: flex;
  flex-direction: column;
  max-width: 300px;
}

.file-label {
  width: 100%;
}

.file-cta {
  border-radius: 0;
}

.file-label {
  text-align: center;
}

.loader {
  width: 20px;
  height: 20px;
  border: 5px solid #FFF;
  border-bottom-color: transparent;
  border-radius: 50%;
  display: inline-block;
  box-sizing: border-box;
  animation: rotation 1s linear infinite;
}

@keyframes rotation {
  0% {
    transform: rotate(0deg);
  }

  100% {
    transform: rotate(360deg);
  }
}
</style>

<script>
import { findProducts } from "../findProducts.js"

export default {
  data() {
    return {
      file: null,
      imagePreview: null,
      products: [],
      dataState: {
        descriptionLoaded: false,
        adsLoaded: false,
        rankingCompleted: false,
        errorOccurred: false,
      }
    };
  },
  methods: {
    handleProductUpload(event) {
      const selectedFile = event.target.files[0];
      if (selectedFile) {
        this.file = selectedFile;
        this.createImagePreview(selectedFile);
        this.loadingProducts = true;
        this.findProducts(selectedFile, "Montréal", this.stateUpdate).then((data) => {
          this.products = data;
        }).finally(() => this.loadingProducts = false)
      }
    },
    stateUpdate(dataState) {
      this.dataState = { ...this.dataState, ...dataState };
    },
    createImagePreview(file) {
      this.imagePreview = URL.createObjectURL(file);
    },
  },
  mixins: [findProducts],
  beforeDestroy() {
    if (this.imagePreview) {
      URL.revokeObjectURL(this.imagePreview);
    }
  },
}
</script>
