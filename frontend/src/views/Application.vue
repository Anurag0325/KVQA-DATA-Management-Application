<!-- <template>
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
  
      <v-container>
        <v-card class="pa-5 mx-auto" max-width="500">
          <v-card-title class="text-center">Application Page</v-card-title>
          <v-card-text>
            <v-btn color="primary" block @click="navigateToApplicationForm">
              Add Application Data
            </v-btn>
          </v-card-text>
        </v-card>
      </v-container>
    </v-app>
  </template>
  
  <script>
  export default {
    methods: {
      navigateToApplicationForm() {
        this.$router.push("/applicationform"); // Redirect to ApplicationForm.vue
      }
    }
  };
  </script>
   -->



   <!-- <template>
    <v-app> -->
      <!-- Top Navigation Bar -->
      <!-- <v-app-bar color="black" dark>
        <v-spacer></v-spacer>
        <span class="white--text text-h6">Welcome to dashboard User!</span>
        <v-spacer></v-spacer>
        <v-btn text color="blue" @click="logout">Logout</v-btn>
      </v-app-bar> -->
  
      <!-- Side Navigation Drawer -->
      <!-- <v-navigation-drawer app permanent width="200">
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
   -->
      <!-- Main Content -->
      <!-- <v-main>
        <v-container fluid> -->
          <!-- Create New Application Button -->
          <!-- <v-btn color="primary" class="mb-4" @click="navigateToApplicationForm">
            Create new application
          </v-btn> -->
  
          <!-- Search Fields -->
          <!-- <v-row>
            <v-col cols="5">
              <v-text-field v-model="organisationName" label="Organisation name"></v-text-field>
            </v-col>
            <v-col cols="5">
              <v-text-field v-model="auditNumber" label="Audit number"></v-text-field>
            </v-col>
            <v-col cols="2">
              <v-btn color="primary">Search</v-btn>
            </v-col>
          </v-row> -->
  
          <!-- Applications Table -->
          <!-- <v-card>
            <v-card-title class="white--text" style="background-color: #A00; padding: 10px;">
              Applications:
            </v-card-title>
  
            <v-data-table :headers="headers" :items="applications" class="elevation-1"> -->
              <!-- <template v-slot:item.delete="{ item }"> -->
              <!-- <template #[`item.delete`]="{ item }">
                <v-btn color="red" text @click="deleteApplication(item)">Delete</v-btn>
              </template>
              <template #[`item.view`]="{ item }">
                <v-btn color="blue" text @click="viewApplication(item)">View</v-btn>
              </template>
            </v-data-table>
          </v-card>
        </v-container>
      </v-main>
    </v-app>
  </template>
  
  <script>
  export default {
    data() {
      return {
        organisationName: "",
        auditNumber: "",
        applications: [],
        headers: [
        { title: "S.NO", key: "sno" },
        { title: "Organisation Name", key: "org" },
        { title: "Audit Number", key: "audit" },
        { title: "Application Status", key: "status" },
        { title: "Auditor", key: "auditor" },
        { title: "Decision Maker", key: "decision" },
        { title: "Delete", key: "delete", sortable: false },
        { title: "View", key: "view", sortable: false }
        ]
      };
    },
    methods: {
      navigateToApplicationForm() {
        this.$router.push("/applicationform"); // Navigate to ApplicationForm.vue
      },
      logout() {
        console.log("Logging out...");
        this.$router.push("/"); // Redirect to login page
      },
      deleteApplication(item) {
        console.log("Deleting application:", item);
      },
      viewApplication(item) {
        console.log("Viewing application:", item);
      }
    }
  };
  </script> -->


  <template>
    <v-app>
      <!-- Top Navigation Bar -->
      <v-app-bar color="black" dark>
        <v-spacer></v-spacer>
        <span class="white--text text-h6">Welcome to dashboard User!</span>
        <v-spacer></v-spacer>
        <v-btn text color="blue" @click="logout">Logout</v-btn>
      </v-app-bar>
  
      <!-- Side Navigation Drawer -->
      <v-navigation-drawer app permanent width="200">
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
  
      <!-- Main Content -->
      <v-main>
        <v-container fluid>
          <!-- Create New Application Button -->
          <v-btn color="primary" class="mb-4" @click="navigateToApplicationForm">
            Create new application
          </v-btn>
  
          <!-- Search Fields -->
          <v-row>
            <v-col cols="5">
              <v-text-field v-model="organisationName" label="Organisation name"></v-text-field>
            </v-col>
            <v-col cols="5">
              <v-text-field v-model="auditNumber" label="Audit number"></v-text-field>
            </v-col>
            <v-col cols="2">
              <!-- <v-btn color="primary">Search</v-btn> -->
              <v-btn color="primary" @click="searchApplications">Search</v-btn>
            </v-col>
          </v-row>
  
          <!-- Applications Table -->
          <v-card>
            <v-card-title class="white--text" style="background-color: #A00; padding: 10px;">
              Applications:
            </v-card-title>
  
            <v-data-table :headers="headers" :items="applications" class="elevation-1">
              <template #[`item.delete`]="{ item }">
                <v-btn color="red" text @click="deleteApplication(item.id)">Delete</v-btn>
              </template>
              <template #[`item.view`]="{ item }">
                <v-btn color="blue" text @click="viewApplication(item.org_name, item.audit_number)">View</v-btn>
              </template>
            </v-data-table>
          </v-card>
        </v-container>
      </v-main>
    </v-app>
  </template>
  
  <script>
  import axios from "axios";
  
  export default {
    data() {
      return {
        organisationName: "",
        auditNumber: "",
        applications: [],
        headers: [
          { title: "S.NO", key: "id" },
          { title: "Organisation Name", key: "org_name" },
          { title: "Audit Number", key: "audit_number" },
          { title: "Application Status", key: "status" },
          { title: "Auditor", key: "auditor" },
          { title: "Decision Maker", key: "decision_maker" },
          { title: "Delete", key: "delete", sortable: false },
          { title: "View", key: "view", sortable: false }
        ]
      };
    },
    methods: {
      // async fetchApplications() {
      //   try {
      //     const response = await axios.get("http://127.0.0.1:5000/dashboard");
      //     this.applications = response.data;
      //   } catch (error) {
      //     console.error("Error fetching applications:", error);
      //     alert("Failed to fetch applications.");
      //   }
      // },

      async fetchApplications() {
  try {
    const token = localStorage.getItem("token"); // Get token from local storage
    console.log("Stored Token:", token); // ✅ Debugging

    if (!token) {
      throw new Error("No authentication token found. Please log in again.");
    }

    const response = await axios.get("http://127.0.0.1:5000/dashboard", {
      headers: {
        Authorization: `Bearer ${token}`, // Attach the token in the request header
      },
    });

    console.log("API Response:", response.data); // ✅ Debugging
    this.applications = response.data;
  } catch (error) {
    console.error("Error fetching applications:", error);
    alert("Failed to fetch applications. Please log in again.");
    this.$router.push("/"); // Redirect to login if unauthorized
  }
},

      navigateToApplicationForm() {
        this.$router.push("/applicationform");
      },
      logout() {
        console.log("Logging out...");
        this.$router.push("/");
      },
      // async deleteApplication(id) {
      //   try {
      //     await axios.delete(`http://127.0.0.1:5000/dashboard/${id}`);
      //     this.applications = this.applications.filter(app => app.id !== id);
      //   } catch (error) {
      //     console.error("Error deleting application:", error);
      //     alert("Failed to delete application.");
      //   }
      // },

      async deleteApplication(id) {
    try {
        const token = localStorage.getItem("token"); // Retrieve token from storage
        if (!token) {
            throw new Error("No authentication token found. Please log in again.");
        }

        await axios.delete(`http://127.0.0.1:5000/dashboard/${id}`, {
            headers: {
                Authorization: `Bearer ${token}`, // Attach token in the request header
            },
        });

        // Remove the deleted application from the list
        this.applications = this.applications.filter(app => app.id !== id);
        alert("Application deleted successfully!");

    } catch (error) {
        console.error("Error deleting application:", error);
        alert("Failed to delete application. Please log in again.");
        this.$router.push("/"); // Redirect to login page if unauthorized
    }
},

async searchApplications() {
      try {
        console.log("🔍 Search button clicked!");

        const token = localStorage.getItem("token");
        console.log("🔑 Token:", token);

        if (!token) {
          throw new Error("No authentication token found. Please log in again.");
        }

        const response = await axios.get("http://127.0.0.1:5000/search", {
          headers: { Authorization: `Bearer ${token}` },
          params: {
            org_name: this.organisationName.trim(),
            audit_number: this.auditNumber.trim(),
          },
        });

        console.log("✅ API Response:", response.data);
        this.applications = response.data;
      } catch (error) {
        console.error("❌ Error searching applications:", error);
        alert("Failed to fetch filtered applications.");
      }
    },


      viewApplication(organisationName, auditNumber) {
        this.$router.push({
          name: "ApplicationDetails",
          params: { organisation_name: organisationName, audit_number: auditNumber }
        });
      }
    },
    created() {
      this.fetchApplications();
    }
  };
  </script>
  
  
  