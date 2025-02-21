<template>
  <v-app>
    <v-container>
    <v-app-bar color="black" dark>
        <v-spacer></v-spacer>
        <span class="white--text text-h6">Welcome to dashboard User!</span>
        <v-spacer></v-spacer>
        <v-btn text color="blue" @click="logout">Logout</v-btn>
        <v-btn color="primary" @click="goBack">Cancel</v-btn>
      </v-app-bar>
    </v-container>
  <v-container>
    <!-- <v-btn color="primary" @click="$router.push('/application')">Cancel</v-btn> -->
    <!-- <v-btn color="primary" @click="goBack">Cancel</v-btn> -->

    <v-card class="pa-5 mt-3 mx-auto" max-width="800">
      <v-card-title class="white--text" style="background-color: #A00; padding: 10px;">
        Create New Application
      </v-card-title>

      <v-card-text>
        <v-form @submit.prevent="submitApplication">
          <v-row>
            <v-col cols="6">
              <v-text-field v-model="organisationName" label="Enter organisation name" required></v-text-field>
            </v-col>
            <v-col cols="6">
              <v-text-field v-model="auditNumber" label="Audit number" required></v-text-field>
            </v-col>

            <!-- File Inputs -->
            <!-- <v-col cols="6">
                <v-file-input label="File1 *" v-model="file1" required></v-file-input>
                <v-file-input label="File3 *" v-model="file3" required></v-file-input>
                <v-file-input label="File5 *" v-model="file5" required></v-file-input>
              </v-col>
  
              <v-col cols="6">
                <v-file-input label="File2 *" v-model="file2" required></v-file-input>
                <v-file-input label="File4 *" v-model="file4" required></v-file-input>
              </v-col> -->

              <!-- Folder Upload -->
            <v-col cols="12">
              <label>Select a folder:</label>
              <input type="file" webkitdirectory directory multiple @change="handleFolderUpload">
              <p v-if="folderFiles.length">Selected files: {{ folderFiles.length }}</p>
            </v-col>

            <!-- Select Fields -->
            <v-col cols="6">
              <v-select v-model="leadAuditor" label="Lead Auditor" :items="['Auditor 1', 'Auditor 2', 'Auditor 3']"
                required></v-select>
            </v-col>

            <v-col cols="6">
              <v-select v-model="decisionMaker" label="Decision Maker *" :items="['Manager', 'Director', 'CEO']"
                required></v-select>
            </v-col>

            <!-- Comments -->
            <v-col cols="12">
              <v-textarea v-model="comments" label="Additional comments"></v-textarea>
            </v-col>

            <!-- Submit Button -->
            <v-col cols="12">
              <v-btn type="submit" color="primary">Submit</v-btn>
            </v-col>
          </v-row>
        </v-form>
      </v-card-text>
    </v-card>
  </v-container>
</v-app>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      organisationName: "",
      auditNumber: "",
      // file1: null,
      // file2: null,
      // file3: null,
      // file4: null,
      // file5: null,
      leadAuditor: "",
      decisionMaker: "",
      comments: "",
      folderFiles: []
    };
  },
  methods: {
    // submitForm() {
    //   console.log("Submitting form:", {
    //     organisationName: this.organisationName,
    //     auditNumber: this.auditNumber,
    //     // files: [this.file1, this.file2, this.file3, this.file4, this.file5],
    //     leadAuditor: this.leadAuditor,
    //     decisionMaker: this.decisionMaker,
    //     comments: this.comments
    //   });
    //   this.$router.push({
    //     path: "/stageform",
    //     query: {
    //       orgName: this.organisationName
    //     }
    //   });
    // }

    // async submitApplication() {
    //   if (!this.organisationName || !this.auditNumber || !this.leadAuditor || !this.decisionMaker) {
    //     alert("Please fill in all required fields!");
    //     return;
    //   }

    //   let applicationData = {
    //     org_name: this.organisationName,
    //     audit_number: this.auditNumber,
    //     auditor: this.leadAuditor,
    //     decision_maker: this.decisionMaker,
    //   };

    //   try {
    //     const response = await axios.post("http://127.0.0.1:5000/dashboard", applicationData, {
    //       headers: { "Content-Type": "application/json" },
    //     });
    //     alert(response.data.message);
    //     this.$router.push({
    //       path: "/stageform",
    //       query: {
    //         org_name: this.organisationName
    //       }
    //     });
    //   } catch (error) {
    //     console.error("Error submitting application:", error.response ? error.response.data : error.message);
    //     alert("Failed to submit application.");
    //   }
    // },

    handleFolderUpload(event) {
      this.folderFiles = Array.from(event.target.files);
    },

    async submitApplication() {
  if (!this.organisationName || !this.auditNumber || !this.leadAuditor || !this.decisionMaker) {
    alert("Please fill in all required fields!");
    return;
  }

  let applicationData = {
    org_name: this.organisationName,
    audit_number: this.auditNumber,
    auditor: this.leadAuditor,
    decision_maker: this.decisionMaker,
  };

  try {
    // Retrieve the JWT token from localStorage (or Vuex if you store it there)
    const token = localStorage.getItem("token"); // Ensure you store the token after login

    if (!token) {
      alert("Authentication required. Please log in.");
      return;
    }

    const response = await axios.post("http://127.0.0.1:5000/dashboard", applicationData, {
      headers: { 
        "Content-Type": "application/json",
        "Authorization": `Bearer ${token}` // ✅ Add JWT token here
      },
    });

    alert(response.data.message);
    this.$router.push({
      path: "/stageform",
      query: {
        org_name: this.organisationName
      }
    });

  } catch (error) {
    console.error("Error submitting application:", error.response ? error.response.data : error.message);
    alert("Failed to submit application.");
  }
},

    goBack() {
    this.$router.push('/application');
  }
  }
};
</script>