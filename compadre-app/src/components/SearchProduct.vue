<script setup>
import ProductsList from "./ProductsList.vue";
</script>

<template>
  <div class="container">
    <div class="is-flex is-flex-direction-row">
      <div v-if="file" class="is-flex is-align-items-center" :style="{ gap: '2em' }">
        <div class="is-flex is-flex-direction-column is-align-self-flex-start">
          <label class="is-flex is-align-self-center">Product</label>
          <figure class="is-flex" v-if="imagePreview">
            <img :src="imagePreview" alt="Image preview" style="max-width: 300px; max-height: 300px;" />
          </figure>
          <p v-else>No image preview available.</p>
        </div>
        <div class="is-flex">
          <ProductsList :products="products" v-if="products.length > 0" />
        </div>
      </div>

      <div v-else class="is-flex is-justify-content-center is-align-items-center">
        <div class="file is-info is-boxed">
          <label class="file-label">
            <input class="file-input" type="file" name="product" @change="handleProductUpload" />
            <span class="file-cta">
              <span class="file-icon">
                <i class="fas fa-cloud-upload-alt"></i>
              </span>
              <span class="file-label"> Upload a photo </span>
            </span>
            <span class="file-name"> No photo uploaded </span>
          </label>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { findProducts } from "../findProducts.js"

export default {
  data() {
    return {
      file: null,
      imagePreview: null,
      products: [],
    };
  },
  methods: {
    handleProductUpload(event) {
      const selectedFile = event.target.files[0];
      if (selectedFile) {
        this.file = selectedFile;
        this.createImagePreview(selectedFile);
        this.loadingProducts = true;
        this.findProducts(selectedFile, "Montréal").then((data) => {
          this.products = data;
        }).finally(() => this.loadingProducts = false)
      }
    },
    createImagePreview(file) {
      this.imagePreview = URL.createObjectURL(file);
    },
  },
  mixins: [findProducts],
  watch: {
    file(newFile) {
      if (newFile) {
        console.log("File changed: ", newFile.name)
      }
    }
  },
  beforeDestroy() {
    if (this.imagePreview) {
      URL.revokeObjectURL(this.imagePreview);
    }
  },
}
</script>
