<template>
    <div v-if="isLoggedIn">
        <h1> Pouze pro nepřihlášené uživatele </h1>
    </div>
    <div v-else>
        <h1> Registrace </h1>
        <form @submit.prevent="submitForm" class="my_form">
            <div class="form-group change">
                <label for class="my_label"> uživatelské jméno </label>
                <input type="text" v-model="username" required class="my_input">
            </div> 
            <div class="form-group change">
                <label for class="my_label"> heslo </label>
                <input type="password" v-model="password" required class="my_input">
            </div>
            <div class="form-group change">
                <label for class="my_label"> heslo znovu </label>
                <input type="password" v-model="password2" required class="my_input">
            </div> 
            <button type="submit" class="my_button"> registrovat se </button>
        </form>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    head() {
      return {
        title: "registrace"
      };
    },
    data() {
        return {
            username: '',
            password: '',
            password2: '',  
        };
    },
    methods: {
        async submitForm() {
            try {
                const response = await axios.post('http://localhost:8000/dlouhodobka/user/register/', {   // Django request
                    username: this.username,
                    password: this.password,
                    password2: this.password2,
                });
            console.log(response.data);
          } catch (error) {
                console.error(error);
            }
        },
    }, 
}
</script>

<style>

</style>