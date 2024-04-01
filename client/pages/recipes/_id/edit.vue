<template>
    <main class="container my-5">
      <div class="row">
        <div class="col-12 text-center my-3">
          <h2 class="mb-3 display-4 text-uppercase">{{ recipe.name }}</h2>
        </div>
        <div class="col-md-6 mb-4">
          <img v-if="!preview" class="img-fluid" style="width: 400px; border-radius: 10px; box-shadow: 0 1rem 1rem rgba(0,0,0,.7);"  :src="recipe.picture">
          <img v-else class="img-fluid" style="width: 400px; border-radius: 10px; box-shadow: 0 1rem 1rem rgba(0,0,0,.7);"  :src="preview">
        </div>
        <div class="col-md-4">
          <form @submit.prevent="submitRecipe">
            <div class="form-group">
              <label for>název receptu</label>
              <input type="text" class="form-control" v-model="recipe.name" >
            </div>
            <div class="form-group">
              <label for>Ingredience</label>
              <input type="text" v-model="recipe.ingredients" class="form-control" name="Ingredients" >
            </div>
            <div class="form-group">
              <label for="obrázek">obrázek</label>
              <input type="file" @change="onFileChange">
            </div>
            <div class="row">
              <div class="col-md-6">
                <div class="form-group">
                  <label for>obtížnost</label>
                  <select v-model="recipe.difficulty" class="form-control" >
                    <option value="Easy">jednoduchá</option>
                    <option value="Medium">střední</option>
                    <option value="Hard">těžká</option>
                  </select>
                </div>
              </div>
              <div class="col-md-6">
                <div class="form-group">
                  <label for>
                     čas přípravy
                    <small>(minutes)</small>
                  </label>
                  <input type="text" v-model="recipe.prep_time" class="form-control" name="Ingredients" >
                </div>
              </div>
            </div>
            <div class="form-group mb-3">
              <label for>postup</label>
              <textarea v-model="recipe.prep_guide" class="form-control" rows="8"></textarea>
            </div>
            <button type="submit" class="btn btn-success">uložit</button>
          </form>
        </div>
      </div>
    </main>
  </template>
  
  <script>
  export default {
    head(){
        return {
          title: "úprava receptu"
        }
      },
    async asyncData({ $axios, params }) {
      try {
        let recipe = await $axios.$get(`/recipes/${params.id}`);
        return { recipe };
      } catch (e) {
        return { recipe: [] };
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
        },
        preview: ""
      };
    },
    methods: {
      onFileChange(e) {
        let files = e.target.files || e.dataTransfer.files;
        if (!files.length) {
          return;
        }
        this.recipe.picture = files[0]
        this.createImage(files[0]);
      },
      createImage(file) {
        let reader = new FileReader();
        let vm = this;
        reader.onload = e => {
          vm.preview = e.target.result;
        };
        reader.readAsDataURL(file);
      },
      async submitRecipe() {
        let editedRecipe = this.recipe;
        console.log("editedRecipe:", editedRecipe);
        // if (editedRecipe.picture && typeof editedRecipe.picture === 'object' && editedRecipe.picture.name && editedRecipe.picture.name.indexOf("http://") !== -1) {
        //   delete editedRecipe["picture"]
        // }
        const config = {
          headers: { "content-type": "multipart/form-data" }
        };
        let formData = new FormData();
        for (let data in editedRecipe) {
          formData.append(data, editedRecipe[data]);
        }
        try {
          let response = await this.$axios.$patch(`/recipes/${editedRecipe.id}/`, formData, config);
          console.log("response:", response);
          this.$router.push("/recipes/");
        } catch (e) {
          console.log("error:",e);
        }
      }
    }
  };
  </script>;
  
  <style scoped>
  a,
  a:visited {
  text-decoration: none;
  color: none;
  }
  </style>