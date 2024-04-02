<template>
    <div>
        <h1> Přihlásit se </h1>
        <form @submit.prevent="submitForm" class="my_form">
            <div class="form-group change">
                <label for class="my_label"> uživatelské jméno </label>
                <input type="text" v-model="username" required class="my_input">
            </div> 
            <div class="form-group change">
                <label for class="my_label"> heslo </label>
                <input type="password" v-model="password" required class="my_input">
            </div> 
            <button type="submit" class="my_button"> přihlásit se </button>
        </form>
        <div>
            <p> {{ loginMessage }} </p>
        </div>
    </div>
</template>

<!--    v databázi user table je main_customuser
        pole: username, password, last_login    -->


<script>
import axios from 'axios';

export default {
    head() {
      return {
        title: "přihlášení"
      };
    }, 
    data() {
        return {
            username: '',
            password: '',
            loginMessage: '',
        }
    },
    methods: {
        async submitForm() {
            try {
                // request na backend
                const response = await axios.post('http://localhost:8000/dlouhodobka/user/login/', {   
                    username: this.username,
                    password: this.password,
                });

                if (response.data.token) {
                    const token = response.data.token;
                    localStorage.setItem('userToken', token);
                    localStorage.setItem('username', this.username);
                    this.isLoggedIn = true;
                    this.$router.push('/recipes/');     // přesune na stránku s recepty
                }   else {
                    this.loginMessage = response.data.message;  // ukáže message s errorem
                    this.isLoggedIn = false;
                }
          } catch (error) {
                console.error(error);
                this.loginMessage = 'Nastal error při přihlašování.';
            }
        },
    },
    computed: {
        hasToken() {
            return !!this.token; 
        },
    },
    destroyed() {    // UI se updatne až po F5 -> F5 po odchodu z login 
        location.reload();
    },
}
</script>

<style>

.my_form {
    display: flex;
    flex-direction: column;
    align-items: center;
}

.change {
    display: flex;
    flex-direction: row;
    justify-content: space-between; 
    align-items: center; 
    width: 40%;
}

.my_label {
    display: block;
    text-align: left;
}

.my_input {
    width: 50%; 
}

.my_button {
    cursor: pointer;
}

</style>