<script setup>
import ProductsList from "./ProductsList.vue";
</script>

<template>
  <div class="container">
    <div class="image-file-input">
      <figure class="is-flex" v-if="imagePreview">
        <img :src="imagePreview" alt="Image preview" style="max-width: 300px; max-height: 300px;" />
      </figure>

      <div class="file is-info is-boxed">
        <label class="file-label">
          <input class="file-input" type="file" name="product" @change="handleProductUpload" />
          <span class="file-cta">
            <span class="file-icon">
              <i class="fas fa-cloud-upload-alt"></i>
            </span>
            <span class="file-label"> Upload a photo </span>
          </span>
        </label>
      </div>
    </div>

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
</style>

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
