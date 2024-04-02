<template>
    <main class="container mt-5"> 
      <div class="row">
        <div class="col-12 text-right mb-4">
          <div class="d-flex justify-content-between">
            <h3>Recepty</h3>
            <nuxt-link v-if="isLoggedIn" to="/recipes/add" class="btn btn-info">přidat recept</nuxt-link>
          </div>
        </div>
        <template > 
          <div v-for="recipe in recipes" :key="recipe.id" class="col-lg-3 col-md-4 col-sm-6 mb-4">
              <recipe-card :onDelete="deleteRecipe" :key="recipe.id" :recipe="recipe"></recipe-card>
          </div>
        </template>
      </div> 
    </main>
  </template>

  <script>
  import RecipeCard from "~/components/RecipeCard.vue";

  export default {
    components: {
      RecipeCard,
    },
    mounted() {
      if (this.recipes.length === 0) {
        this.$store.dispatch('fetchRecipes');
      }
    },
    computed: {
      recipes() {
        return this.$store.state.recipes;
      },
      isLoggedIn() {
        return this.$store.getters.isLoggedIn;
      },
    },
    methods: {
      async deleteRecipe(recipe_id) {
        try {
          await this.$axios.$delete(`/recipes/${recipe_id}/`);
          // let newRecipes = await this.$axios.$get("/recipes/"); 
          // this.recipes = newRecipes; 
        } catch (e) {
          console.log(e);
        }
      }
    },
  };
  </script>

  <style scoped>
  a,
  a:visited {
  text-decoration: none;
  color: none;
  }
  </style>

