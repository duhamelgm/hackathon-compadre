<template>
  <section class="products">
    <div class="products-content">
      <div class="content">
        <div class="is-flex is-flex-wrap-wrap" style="gap: 2rem;">
          <div class="is-flex is-flex-direction-row" v-for="(product, index) in products" :key="index">
            <div class="is-flex">
              <img :src="product.imageUrl" style="width: 128px; height: 128px" />
            </div>
            <div class="is-flex is-flex-direction-column">
              <div class="is-flex">
                <span class="icon-text has-text-info has-text-weight-semibold">
                  <span class="icon">
                    <i class="fas fa-tag"></i>
                  </span>
                  <span>{{ product.name }}</span>
                </span>
              </div>
              <div class="is-flex">
                <span class="icon-text has-text-success">
                  <span class="icon">
                    <i class="fas fa-comment-dollar"></i>
                  </span>
                  <span>{{ product.price }}</span>
                </span>
              </div>
              <div class="is-flex">
                <span class="icon-text has-text-warning">
                  <span class="icon">
                    <i class="fas fa-comment-dollar"></i>
                  </span>
                  <span>{{ product.source }}</span>
                </span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<style>
.products-content {
  max-height: 90vh;
  overflow: scroll;
}

.products-content .content {
  margin: 0;
}
</style>

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
