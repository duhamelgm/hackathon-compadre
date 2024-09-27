<template>
  <div class="about">
    <h1>This is an about page</h1>
    <div>
      <input type="file" @change="uploadFile" />
      <button @click="submitFile">Submit</button>
    </div>
  </div>

</template>

<script setup>
import { ref, computed } from "vue";
// import axios from "axios";

const file = ref(null);

const fileName = computed(() => file.value?.name);
const fileExtension = computed(() => fileName.value?.substr(fileName.value?.lastIndexOf(".") + 1));
const fileMimeType = computed(() => file.value?.type);

const uploadFile = (event) => {
  file.value = event.target.files[0];
};

const submitFile = async () => {
  console.log(file.value.name);
  //
  // const reader = new FileReader();
  // reader.readAsDataURL(file.value);
  // reader.onload = async () => {
  //   const encodedFile = reader.result.split(",")[1];
  //   const data = {
  //     file: encodedFile,
  //     fileName: fileName.value,
  //     fileExtension: fileExtension.value,
  //     fileMimeType: fileMimeType.value,
  //   };
  //   try {
  //     const endpoint = "https://example.com/upload";
  //     const response = await axios.post(endpoint, data);
  //     console.log(response.data);
  //   } catch (error) {
  //     console.error(error);
  //   }
  // };
};
</script>

<style>
@media (min-width: 1024px) {
  .about {
    min-height: 100vh;
    display: flex;
    align-items: center;
  }
}
</style>
