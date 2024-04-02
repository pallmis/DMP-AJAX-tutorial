export const state = () => ({
    recipes: [],
  });
  
export const mutations = {
    allRecipes(state, recipes) {
        state.recipes = recipes;
    },
};

export const actions = {
    logout({ commit }) {
        localStorage.removeItem('userToken');
    },

    async fetchRecipes({ commit }) {
        try {
          const recipes = await this.$axios.$get('/recipes/');
          commit('allRecipes', recipes);
        } catch (error) {
          console.error('Error fetching recipes:', error);
        }
    },
};

export const getters = {
    isLoggedIn(state) {
        if (process.client) {
            return !!localStorage.getItem('userToken');
        }
        return false;
    },
};


