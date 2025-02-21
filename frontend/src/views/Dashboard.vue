<!-- <template>
    <v-container>
      <v-card class="pa-5 mx-auto" max-width="500">
        <v-card-title class="text-center">Welcome to Dashboard</v-card-title>
        <v-card-text>
          <p>You are logged in!</p>
          <v-btn color="error" block @click="logout">Logout</v-btn>
        </v-card-text>
      </v-card>
    </v-container>
  </template>
  
  <script>
  export default {
    methods: {
      logout() {
        localStorage.removeItem("token"); // Remove token
        this.$router.push("/"); // Redirect to login
      }
    }
  };
  </script>
   -->

   <template>
    <v-app>
      <v-navigation-drawer app>
        <v-list>
          <v-list-item link to="/dashboard">
            <v-list-item-content>
              <v-list-item-title>Home</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
  
          <v-list-item link to="/application">
            <v-list-item-content>
              <v-list-item-title>Application</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list>
      </v-navigation-drawer>
  
      <v-app-bar app color="primary" dark>
        <v-toolbar-title>Dashboard</v-toolbar-title>
        <v-spacer></v-spacer>
        <v-btn color="error" @click="logout">Logout</v-btn>
      </v-app-bar>
  
      <v-main>
        <v-container>
          <v-card class="pa-5 mx-auto" max-width="500">
            <v-card-title class="text-center">Welcome to Dashboard</v-card-title>
            <v-card-text>
              <p>You are logged in!</p>
            </v-card-text>
          </v-card>
        </v-container>
      </v-main>
    </v-app>
  </template>
  
  <script>
  export default {
    methods: {
      logout() {
        localStorage.removeItem("token"); // Remove token
        this.$router.push("/"); // Redirect to login
      }
    }
  };
  </script>
  