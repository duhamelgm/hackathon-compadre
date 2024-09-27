<template>
  <section class="card">
    <div class="card-content">
      <div class="content">
        <div class="columns">
          <div v-for="(product, index) in products" :key="index" class="column">
            <img :src="product.imageUrl" style="width: 128px; height: 128px" />
            <span class="icon-text has-text-info has-text-weight-semibold">
              <span class="icon">
                <i class="fas fa-tag"></i>
              </span>
              <span>{{ product.name }}</span>
            </span>
            <span class="icon-text has-text-success">
              <span class="icon">
                <i class="fas fa-comment-dollar"></i>
              </span>
              <span>{{ product.price }}</span>
            </span>
            <span class="icon-text has-text-warning">
              <span class="icon">
                <i class="fas fa-comment-dollar"></i>
              </span>
              <span>{{ product.location }}</span>
            </span>
          </div>
        </div>
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
