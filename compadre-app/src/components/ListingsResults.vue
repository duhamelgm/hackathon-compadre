<template>
  <section class="card">
    <div class="card-content">
      <div class="content">
        <datalist class="grid" v-for="(listing, index) in listings" :key="index">
          <div class="cell">
            <figure>
              <img :src="listing.image" width="256px" height="256px" />
            </figure>
          </div>
          <div class="cell">
            <label>{{ listing.name }}</label>
            <p>{{ listing.price }}</p>
            <p>{{ listing.location }}</p>
          </div>
        </datalist>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  data() {
    return {
      listings: [
        { name: "Workspace table", price: "U$ 279,55", image: "https://m.media-amazon.com/images/I/61Y4Ej13XnL._AC_SL1004_.jpg" },
        { name: "Macbook Pro", price: "U$ 875,28", image: "https://cdn.arstechnica.net/wp-content/uploads/2023/11/IMG_1415.jpeg" }
      ]
    }
  }
}
</script>
