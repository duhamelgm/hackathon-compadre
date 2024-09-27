<template>
  <section class="products">
    <div class="products-content">
      <div class="content">
        <div class="is-flex is-flex-wrap-wrap" style="gap: 2rem;">
          <div class="is-flex is-flex-direction-row productBlock" v-for="(product, index) in products" :key="index">
            <a :href="product.url" target="_blank">
              <div class="is-flex">
                <img :src="product.imageUrl" width="100%" style="min-width: 120px; max-width: 120px;" class="imgBox" />
              </div>
              <div class="is-flex is-flex-direction-column">
                <span class="icon-text has-text-info has-text-weight-semibold">
                  <span class="icon">
                    <i class="fas fa-tag"></i>
                  </span>
                  <span class="textWrapped">{{ product.name }}</span>
                  <span v-if="[0, 1, 2].includes(index)" class="icon-text has-text-warning">
                    <span class="icon">
                      <i class="fas fa-star"></i>
                    </span>
                  </span>
                </span>
                <span class="icon-text has-text-success">
                  <span class="icon">
                    <i class="fas fa-comment-dollar"></i>
                  </span>
                  <span>{{ product.price === 0 ? "Free" : "$ " + product.price }}</span>
                </span>
                <span class="icon-text has-text-warning">
                  <span class="icon">
                    <i class="fas fa-store"></i>
                  </span>
                  <span>{{ product.source }}</span>
                </span>
              </div>
            </a>
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

@media (max-width: 1024px) {
  .products-content {
    max-height: unset;
    margin: 0 2rem 6rem;
  }
}

.textWrapped {
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-line-clamp: 3;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: normal;

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

<style scope>
.imgBox {
  border-radius: 1rem;
  object-fit: fill;
}

.productBlock {
  gap: 1rem;
}
</style>
