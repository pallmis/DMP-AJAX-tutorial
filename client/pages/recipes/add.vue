<template>
    <main class="container my-5">
      <div class="row">
        <div class="col-12 text-center my-3">
          <h2 class="mb-3 display-4 text-uppercase">{{ recipe.name }}</h2>
        </div>
        <div class="col-md-6 mb-4">
          <img
            v-if="preview"
            class="img-fluid"
            style="width: 400px; border-radius: 10px; box-shadow: 0 1rem 1rem rgba(0,0,0,.7);"
            :src="preview"
            alt
          >
        </div>
        <div class="col-md-4">
          <form @submit.prevent="submitRecipe">
            <div class="form-group">
              <label for>název receptu</label>
              <input type="text" class="form-control" v-model="recipe.name">
            </div>
            <div class="form-group">
              <label for>Ingredience</label>
              <input v-model="recipe.ingredients" type="text" class="form-control">
            </div>
            <div class="form-group">
              <label for>obrázek</label>
              <input type="file" name="file" @change="onFileChange">
            </div>
            <div class="row">
              <div class="col-md-6">
                <div class="form-group">
                  <label for class="down">obtížnost</label>
                  <select v-model="recipe.difficulty" class="form-control">
                    <option value="Jednoduchá">jednudochá</option>
                    <option value="Střední">střední</option>
                    <option value="Težká">těžká</option>
                  </select>
                </div>
              </div>
              <div class="col-md-6">
                <div class="form-group">
                  <label for>
                    čas přípravy
                    <small>(minuty)</small>
                  </label>
                  <input v-model="recipe.prep_time" type="number" class="form-control">
                </div>
              </div>
            </div>
            <div class="form-group mb-3">
              <label for>postup</label>
              <textarea v-model="recipe.prep_guide" class="form-control" rows="8"></textarea>
            </div>
            <button type="submit" class="btn btn-primary">uložit</button>
          </form>
        </div>
      </div>
    </main>
  </template>
  
  <script>
  export default {
    head() {
      return {
        title: "Přidání receptu"
      };
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
        this.recipe.picture = files[0];
        this.createImage(files[0]);
      },
      createImage(file) {
        // let image = new Image();
        let reader = new FileReader();
        let vm = this;
        reader.onload = e => {
          vm.preview = e.target.result;
        };
        reader.readAsDataURL(file);
      },
      async submitRecipe() {
        const config = {
          headers: { "content-type": "multipart/form-data" }
        };
        let formData = new FormData();
        for (let data in this.recipe) {
          formData.append(data, this.recipe[data]);
        }
        try {
          let response = await this.$axios.$post("/recipes/", formData, config);
          this.$router.push("/recipes/");
        } catch (e) {
          console.log(e);
        }
      }
    },
    destroyed() {
      this.$store.dispatch('fetchRecipes');
    },
  };
  </script>
  
  <style scoped>

  a,
  a:visited {
  text-decoration: none;
  color: none;
  }

  .down {
    padding-bottom: 24px;
  }

  </style>  