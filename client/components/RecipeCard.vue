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
        <button v-if="isLoggedIn" @click="onDelete(recipe.id)" class="btn btn-sm btn-danger">smazat</button>
      </div>
    </div>
  </div>
</template>
  
<script>
export default {
  props: ["recipe", "onDelete"],
  computed: {
    isLoggedIn() {
      return this.$store.getters.isLoggedIn;
    }
  }
};
</script>
  
<style>
.recipe-card {
    box-shadow: 0 1rem 1.5rem rgba(0,0,0,.6);
    min-height: 250px;
    max-width: 200px;
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