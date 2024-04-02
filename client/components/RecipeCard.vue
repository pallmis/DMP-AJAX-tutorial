<template>
  <div class="card recipe-card">
    <img :src="recipe.picture" class="myimg" height="100">
    <!-- "card-img-top" -->
    <div class="card-body">
      <h5 class="card-title">{{ recipe.name }}</h5>
      <p class="card-text">
        <strong>ingredience:</strong> {{ recipe.ingredients }}
      </p>
      <div class="action-buttons">
        <nuxt-link :to="`/recipes/${recipe.id}/`" class="btn btn-sm btn-success">zobrazit</nuxt-link>
        <nuxt-link :to="`/recipes/${recipe.id}/edit/`" class="btn btn-sm btn-primary">upravit</nuxt-link>
        <!-- <button @click="toggleFavorite" class="btn btn-sm btn-outline-warning"> <i v-bind:class="{ 'fas fa-heart': isFavorited, 'far fa-heart': !isFavorited }"> </i> </button>
        <button v-if="this.recipe.owner.id === this.$auth.user.id" @click="deleteRecipe" class="btn btn-sm btn-danger">smazat</button> -->
      </div>
    </div>
  </div>
</template>
  
<script>
export default {
  props: ["recipe"], //props: ["recipe", "onDelete"]
//   data() {
//     return {
//       isFavorited: false,
//     };
//   },
//   async mounted() {
//     async function fetchData() {
//       try {
//         const response = await this.$axios.$get(`/recipes/${this.recipe.id}`);
//         // Assign fetched data to the local property (avoiding prop mutation)
//         this.recipe = response.data;
//         this.isFavorited = this.recipe.favorited_by.some(user => user.id === this.$auth.user.id);
//       } catch (error) {
//         console.error('Error fetching recipe:', error);
//         // Handle errors appropriately, e.g., display an error message
//       }
//     }
//     fetchData();
//   },
//   methods: {
//   async toggleFavorite() {
//     try {
//       const url = `/recipes/${this.recipe.id}/favorite/`; // Adjust based on your backend endpoint
//       const method = this.isFavorited ? 'DELETE' : 'POST'; // Toggle between adding/removing from favorites
//       const response = await this.$axios[method](url);

//       // Update local state and potentially UI (e.g., icon change) based on response
//       this.isFavorited = !this.isFavorited;

//     } catch (error) {
//       console.error('Error toggling favorite:', error);
//       // Handle errors appropriately, e.g., display an error message
//     }
//   },
// },
};
</script>
  
<style>
.recipe-card {
    box-shadow: 0 1rem 1.5rem rgba(0,0,0,.6);
    min-height: 250px;
}

.myimg {
  max-height: 200px;
}

.card-text{
  min-height: 50px;
}

a,
a:visited {
text-decoration: none;
color: none;
}
</style>