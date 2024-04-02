<template>
    <div>
        <nav>
            <ul>
                <li class="top_nav_color"> <NuxtLink to="/"> tutoriál </NuxtLink> </li>
                <li class="top_nav_color"> <NuxtLink to="/recipes"> recepty </NuxtLink> </li>
            </ul>
        </nav>
        <nav v-if="showDefaultNav" class="grey">
            <ul>
                <li> <NuxtLink to="/recipes"> recepty </NuxtLink> </li>
                <li v-if="!isLoggedIn"> <NuxtLink to="/recipes/login"> přihlášení </NuxtLink> </li> 
                <li v-if="!isLoggedIn"> <NuxtLink to="/recipes/register"> registrace </NuxtLink> </li>
                <li v-if="isLoggedIn" @click="logout"> <a href=""> odhlásit se </a> </li>
            </ul>
        </nav>
        <!-- obsah -->
        <main>
            <Nuxt /> <!-- tady je stránka z /pages -->
        </main>
        <!-- obsah -->
        <footer>
          <p></p>
        </footer>
    </div>
</template>

<script>
export default {
  created() {
    console.log(this.$store);
  },
  computed: {
    showDefaultNav() {
      return this.$route.path.includes("/recipes");
    },
    isLoggedIn() {
      return this.$store.getters.isLoggedIn;
    }
  },
  methods: {
    async logout() {
      await this.$store.dispatch('logout');
      this.$router.push('/recipes');
    }
  },
};
</script>

<style>

a.nuxt-link-active {
  font-weight: bold;
}

a.nuxt-link-exact-active {
  color: #57C8FF;
}

main {
  margin: 0 auto;
  padding: 0;
  margin-top: 0px;
  text-align: center;
  min-height: 1000px;
}

ul {
  list-style-type: none;
  padding: 0;
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
}
li {
  font-weight: bold;
  margin: 0 0.5rem;
  padding: 0.25rem;
  font-size: 1.2rem;
}

a,
a:visited {
  text-decoration: none;
  color: inherit;
}

a:hover {
  color: #57C8FF;
}

footer {
  background-color: #BDBDBD;
  min-height: 50px;
  text-align: center;
}

.grey {
  background-color: #BDBDBD;
}

.top_nav_color {
  color: black;
}
</style>