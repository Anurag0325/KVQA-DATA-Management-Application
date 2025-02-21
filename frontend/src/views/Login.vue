<template>
    <v-container>
      <v-card class="pa-5 mx-auto" max-width="400">
        <v-card-title class="text-center">Login</v-card-title>
        <v-card-text>
          <v-form @submit.prevent="login">
            <v-text-field label="Email" v-model="email" required></v-text-field>
            <v-text-field label="Password" v-model="password" type="password" required></v-text-field>
            <v-btn type="submit" color="primary" block>Login</v-btn>
          </v-form>
          <p v-if="errorMessage" class="red--text">{{ errorMessage }}</p>
        </v-card-text>
      </v-card>
    </v-container>
  </template>
  
  <script>
  import axios from "axios";
  
  export default {
    data() {
      return {
        email: "",
        password: "",
        errorMessage: ""
      };
    },
    methods: {
      async login() {
        try {
          const response = await axios.post("http://127.0.0.1:5000/login", {
            email: this.email,
            password: this.password
          });
  
          localStorage.setItem("token", response.data.token);
          this.$router.push("/dashboard"); // Redirect after login
        } catch (error) {
          this.errorMessage = error.response?.data?.error || "Login failed";
        }
      }
    }
  };
  </script>
  
  <style scoped>
  @import 'vuetify/styles';
  /* .v-container {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
  } */
  </style>
  