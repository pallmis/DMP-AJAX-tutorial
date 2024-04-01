<template>
    <div v-if="isLoggedIn">
        <nav>
            <ul>
                <li> <a href=""> oblíbené recepty </a> </li>
                <li> <a href=""> vaše recepty </a> </li>
            </ul>
        </nav>
        <div>

        </div>
    </div>
    <div v-else>
        <h1> Nejse přihlášen </h1>
    </div>
</template>

<script>
export default {
    computed: {
        isLoggedIn() {
            return this.$store.getters.isLoggedIn;
        },
    },
};
</script>

<style>

</style>