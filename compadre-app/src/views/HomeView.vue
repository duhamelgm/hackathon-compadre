<script setup>
import SearchProduct from "../components/SearchProduct.vue"
</script>

<template>
  <main>
    <nav class="navbar navbar-custom" role="navigation" aria-label="main navigation">
      <div class="navbar-brand">
        <a class="navbar-item" href="https://bulma.io">
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