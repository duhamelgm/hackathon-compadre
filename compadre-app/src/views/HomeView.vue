<script setup>
import SearchProduct from "../components/SearchProduct.vue"
</script>

<template>
  <main>
    <nav class="navbar navbar-custom" role="navigation" aria-label="main navigation">
      <div class="navbar-brand" style="justify-content: center;">
        <a class="navbar-item" href="https://compadre.me">
          COMPADRE.ME
        </a>
      </div>
    </nav>

    <SearchProduct />
  </main>
</template>

<style>
.navbar-custom {
  /* background: rgb(250, 68, 56); */
}

.navbar-custom .navbar-item {
  font-weight: 700;
  color: white;
}
</style>
