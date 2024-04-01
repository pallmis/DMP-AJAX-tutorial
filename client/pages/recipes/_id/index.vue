<template>
    <main class="container my-5">
      <div class="row">
        <div class="col-12 text-center my-3">
          <h2 class="mb-3 display-4 text-uppercase">{{ recipe.name }}</h2>
        </div>
        <div class="col-md-6 mb-4">
          <img
            class="img-fluid"
            style="width: 400px; border-radius: 10px; box-shadow: 0 1rem 1rem rgba(0,0,0,.7);"
            :src="recipe.picture"
            alt
          >
        </div>
        <div class="col-md-6">
          <div class="recipe-details">
            <h4>Ingredience</h4>
            <p>{{ recipe.ingredients }}</p>
            <h4>čas přípravy</h4>
            <p>{{ recipe.prep_time }} minut</p>
            <h4>obtížnost</h4>
            <p>{{ recipe.difficulty }}</p>
            <h4>postup</h4>
            <textarea class="form-control" rows="10" v-html="recipe.prep_guide" readonly></textarea>
          </div>
        </div>
      </div>
    </main>
  </template>
  
  <script>
  export default {
    head() {
      return {
        title: "recept"
      };
    },
    async asyncData({ $axios, params }) {
      console.log(params.id);
      try {
        let recipe = await $axios.$get(`/recipes/${params.id}/`);
        console.log(recipe);
        return { recipe };
      } catch (e) {
        console.error(e);
        return { recipe: null };
      }
    },
    data() {
      return {
        recipe: {
          name: "",
          picture: "",
          ingredients: "",
          difficulty: "",
          prep_time: null,
          prep_guide: ""
        }
      };
    }
  };
  </script>
  
  <style scoped>
  a,
  a:visited {
  text-decoration: none;
  color: none;
  }
  </style>