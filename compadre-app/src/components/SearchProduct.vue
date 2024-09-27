<template>
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
</template>

<script>
export default {
  data() {
    return {
      file: null,
    };
  },
  methods: {
    handleProductUpload(event) {
      debugger;
      this.file = event.target.files[0];
    }
  },
  watch: {
    file(newFile) {
      if (newFile) {
        console.log("File changed: ", newFile.name)
      }
    }
  }
}
</script>
