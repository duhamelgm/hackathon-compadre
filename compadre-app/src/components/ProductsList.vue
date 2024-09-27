<template>
  <section class="card">
    <div class="card-content">
      <div class="content">
        <datalist class="grid" v-for="(product, index) in products" :key="index">
          <div class="cell">
            <figure>
              <img :src="product.image" width="256px" height="256px" />
            </figure>
          </div>
          <div class="cell">
            <label>{{ product.name }}</label>
            <p>{{ product.price }}</p>
            <p>{{ product.location }}</p>
          </div>
        </datalist>
      </div>
    </div>
  </section>
</template>

<script>

export default {
  props: {
    products: {
      type: Array,
      required: true
    }
  },
}
</script>
