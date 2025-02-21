<!-- <template>
    <v-container>
      <v-card>
        <v-card-title>Application Details</v-card-title>
        <v-card-text>
          <h3>Stage 1 Details</h3>
          <p><strong>Scope:</strong> {{ applicationDetails.stage1.scope }}</p>
          <p><strong>Plan:</strong> {{ applicationDetails.stage1.stage1_plan }}</p>
          <p><strong>Selected Date:</strong> {{ applicationDetails.stage1.selected_date }}</p>
          <p><strong>Report:</strong> {{ applicationDetails.stage1.stage1_report }}</p>
          <p><strong>Comments:</strong> {{ applicationDetails.stage1.comment }}</p>
  
          <h3>Stage 2 Details</h3>
          <p><strong>Scope:</strong> {{ applicationDetails.stage2.scope }}</p>
          <p><strong>Plan:</strong> {{ applicationDetails.stage2.stage2_plan }}</p>
          <p><strong>Selected Date:</strong> {{ applicationDetails.stage2.selected_date }}</p>
          <p><strong>Report:</strong> {{ applicationDetails.stage2.stage2_report }}</p>
          <p><strong>Comments:</strong> {{ applicationDetails.stage2.comment }}</p>
        </v-card-text>
        <v-card-actions>
          <v-btn color="blue" @click="$router.push('/application')">Back</v-btn>
        </v-card-actions>
      </v-card>
    </v-container>
  </template>
  
  <script>
  import axios from "axios";
  
  export default {
    props: ["organisation_name"],
    data() {
      return {
        applicationDetails: { stage1: {}, stage2: {} },
      };
    },
    methods: {
      async fetchApplicationDetails() {
        try {
          const response = await axios.get(`http://127.0.0.1:5000/application/${this.organisation_name}`);
          this.applicationDetails = response.data;
        } catch (error) {
          console.error("Error fetching application details:", error);
          alert("Failed to fetch details.");
        }
      },
    },
    created() {
      this.fetchApplicationDetails();
    },
  };
  </script>
   -->


   <!-- <template>
    <v-container>
      <v-card>
        <v-card-title>Application Details</v-card-title>
        <v-card-text>
          <h3>Stage 1 Details</h3>
          <p><strong>Scope:</strong> {{ applicationDetails.stage1.scope }}</p>
          <p> -->
            <!-- <strong>Plan:</strong>
            <a v-if="applicationDetails.stage1.stage1_plan"
               :href="getDownloadUrl(applicationDetails.stage1.stage1_plan)" 
               target="_blank">
              {{ applicationDetails.stage1.stage1_plan }}
            </a> -->

            <!-- <strong>Plan:</strong>
              <v-btn v-if="applicationDetails.stage1.stage1_plan"
                    color="primary"
                    @click="downloadFile(applicationDetails.stage1.stage1_plan)">
                  Download
              </v-btn>
          </p>
          <p>
            <strong>Report:</strong> -->
            <!-- <a v-if="applicationDetails.stage1.stage1_report"
               :href="getDownloadUrl(applicationDetails.stage1.stage1_report)" 
               target="_blank">
              {{ applicationDetails.stage1.stage1_report }}
            </a> -->
            <!-- <v-btn v-if="applicationDetails.stage1.stage1_report"
                  color="primary"
                  @click="downloadFile(applicationDetails.stage1.stage1_report)">
                Download
            </v-btn>
          </p>
  
          <h3>Stage 2 Details</h3>
          <p><strong>Scope:</strong> {{ applicationDetails.stage2.scope }}</p>
          <p>
            <strong>Plan:</strong> -->
            <!-- <a v-if="applicationDetails.stage2.stage2_plan"
               :href="getDownloadUrl(applicationDetails.stage2.stage2_plan)" 
               target="_blank">
              {{ applicationDetails.stage2.stage2_plan }}
            </a> -->
            <!-- <v-btn v-if="applicationDetails.stage2.stage2_plan"
                    color="primary"
                    @click="downloadFile(applicationDetails.stage2.stage2_plan)">
                  Download
            </v-btn>
          </p>
          <p>
            <strong>Report:</strong> -->
            <!-- <a v-if="applicationDetails.stage2.stage2_report"
               :href="getDownloadUrl(applicationDetails.stage2.stage2_report)" 
               target="_blank">
              {{ applicationDetails.stage2.stage2_report }}
            </a> -->
            <!-- <v-btn v-if="applicationDetails.stage2.stage2_report"
                  color="primary"
                  @click="downloadFile(applicationDetails.stage2.stage2_report)">
                Download
            </v-btn>
          </p>
        </v-card-text>
        <v-card-actions>
          <v-btn color="blue" @click="$router.push('/application')">Back</v-btn>
        </v-card-actions>
      </v-card>
    </v-container>
  </template>
  
  <script>
  import axios from "axios";
  
  export default {
    props: ["organisation_name"],
    data() {
      return {
        applicationDetails: { stage1: {}, stage2: {} },
      };
    },
    methods: {
      // async fetchApplicationDetails() {
      //   try {
      //     const response = await axios.get(`http://127.0.0.1:5000/application/${this.organisation_name}`);
      //     this.applicationDetails = response.data;
      //   } catch (error) {
      //     console.error("Error fetching application details:", error);
      //     alert("Failed to fetch details.");
      //   }
      // },

      async fetchApplicationDetails() {
    try {
        const token = localStorage.getItem("token"); // Retrieve token
        if (!token) {
            throw new Error("No authentication token found. Please log in again.");
        }

        const response = await axios.get(`http://127.0.0.1:5000/application/${this.organisation_name}`, {
            headers: {
                Authorization: `Bearer ${token}`, // Attach token in the request header
            },
        });

        this.applicationDetails = response.data;
    } catch (error) {
        console.error("Error fetching application details:", error);
        alert("Failed to fetch details. Please log in again.");
        this.$router.push("/"); // Redirect to login page if unauthorized
    }
},
      // getDownloadUrl(filename) {
      //       // Remove "uploads/" if present
      //       const cleanFilename = filename.replace(/^uploads\//, "");
      //       return `http://127.0.0.1:5000/download/${encodeURIComponent(cleanFilename)}`;
      //   }

      async downloadFile(filename) {
        try {
            const token = localStorage.getItem("token");
            if (!token) {
                throw new Error("No authentication token found. Please log in again.");
            }

            // Remove "uploads/" prefix if present
            const cleanFilename = filename.replace(/^uploads\//, "");

            const response = await axios.get(`http://127.0.0.1:5000/download/${encodeURIComponent(cleanFilename)}`, {
                headers: { Authorization: `Bearer ${token}` },
                responseType: "blob", // Ensures it's treated as a file
            });

            // Create a Blob and trigger download
            const blob = new Blob([response.data], { type: response.headers["content-type"] });
            const link = document.createElement("a");
            link.href = window.URL.createObjectURL(blob);
            link.setAttribute("download", cleanFilename);
            document.body.appendChild(link);
            link.click();
            document.body.removeChild(link);
        } catch (error) {
            console.error("Error downloading file:", error);
            alert("Failed to download the file.");
        }
    }
    },
    created() {
      this.fetchApplicationDetails();
    },
  };
  </script> -->


  <!-- <template>
    <v-container>
      <v-card>
        <v-card-title>Application Details</v-card-title>
        <v-card-text>
          
          <h3>Organisation Information</h3>
          <p><strong>Organisation Name:</strong> {{ applicationDetails.organisation_name }}</p>
          <p><strong>Audit Number:</strong> {{ applicationDetails.audit_number }}</p>
  
          <h3>Stage 1 Details</h3>
          <p><strong>Date of Audit:</strong> {{ applicationDetails.stage1.audit_date }}</p>
          <p><strong>Mail To:</strong> {{ applicationDetails.stage1.mail_to }}</p>
          <p><strong>Mail From:</strong> {{ applicationDetails.stage1.mail_from }}</p>
          <p><strong>Scope:</strong> {{ applicationDetails.stage1.scope }}</p>
  
          <p>
            <strong>Plan:</strong>
            <v-btn v-if="applicationDetails.stage1.stage1_plan"
                  color="primary"
                  @click="downloadFile(applicationDetails.stage1.stage1_plan)">
                Download
            </v-btn>
          </p>
          <p>
            <strong>Report:</strong>
            <v-btn v-if="applicationDetails.stage1.stage1_report"
                  color="primary"
                  @click="downloadFile(applicationDetails.stage1.stage1_report)">
                Download
            </v-btn>
          </p>
  
          <h3>Stage 2 Details</h3>
          <p><strong>Date of Audit:</strong> {{ applicationDetails.stage2.audit_date }}</p>
          <p><strong>Mail To:</strong> {{ applicationDetails.stage2.mail_to }}</p>
          <p><strong>Mail From:</strong> {{ applicationDetails.stage2.mail_from }}</p>
          <p><strong>Scope:</strong> {{ applicationDetails.stage2.scope }}</p>
  
          <p>
            <strong>Plan:</strong>
            <v-btn v-if="applicationDetails.stage2.stage2_plan"
                  color="primary"
                  @click="downloadFile(applicationDetails.stage2.stage2_plan)">
                Download
            </v-btn>
          </p>
          <p>
            <strong>Report:</strong>
            <v-btn v-if="applicationDetails.stage2.stage2_report"
                  color="primary"
                  @click="downloadFile(applicationDetails.stage2.stage2_report)">
                Download
            </v-btn>
          </p>
        </v-card-text>
        <v-card-actions>
          <v-btn color="blue" @click="$router.push('/application')">Back</v-btn>
        </v-card-actions>
      </v-card>
    </v-container>
  </template>
  
  <script>
  import axios from "axios";
  
  export default {
    props: ["organisation_name"],
    data() {
      return {
        applicationDetails: { stage1: {}, stage2: {} },
      };
    },
    methods: {
      async fetchApplicationDetails() {
        try {
          const token = localStorage.getItem("token"); // Retrieve token
          if (!token) {
            throw new Error("No authentication token found. Please log in again.");
          }
  
          const response = await axios.get(`http://127.0.0.1:5000/application/${this.organisation_name}`, {
            headers: {
              Authorization: `Bearer ${token}`, // Attach token in the request header
            },
          });
  
          this.applicationDetails = response.data;
        } catch (error) {
          console.error("Error fetching application details:", error);
          alert("Failed to fetch details. Please log in again.");
          this.$router.push("/"); // Redirect to login page if unauthorized
        }
      },
  
      async downloadFile(filename) {
        try {
          const token = localStorage.getItem("token");
          if (!token) {
            throw new Error("No authentication token found. Please log in again.");
          }
  
          const cleanFilename = filename.replace(/^uploads\//, "");
          const response = await axios.get(`http://127.0.0.1:5000/download/${encodeURIComponent(cleanFilename)}`, {
            headers: { Authorization: `Bearer ${token}` },
            responseType: "blob",
          });
  
          const blob = new Blob([response.data], { type: response.headers["content-type"] });
          const link = document.createElement("a");
          link.href = window.URL.createObjectURL(blob);
          link.setAttribute("download", cleanFilename);
          document.body.appendChild(link);
          link.click();
          document.body.removeChild(link);
        } catch (error) {
          console.error("Error downloading file:", error);
          alert("Failed to download the file.");
        }
      }
    },
    created() {
      this.fetchApplicationDetails();
    },
  };
  </script> -->



 <template>
  <v-container fluid class="full-screen-container">
    <v-card class="pa-4 full-screen-card">
      <v-card-title class="text-h5 font-weight-bold">Application Details</v-card-title>
      <v-divider class="mb-4"></v-divider>

      <!-- Organisation & Audit Details -->
      <v-row>
        <v-col cols="12" md="6">
          <v-card outlined class="pa-3">
            <v-card-subtitle class="text-h6 font-weight-bold">Organisation Name</v-card-subtitle>
            <v-card-text class="text-body-1">{{ organisation_name }}</v-card-text>
          </v-card>
        </v-col>
        <v-col cols="12" md="6">
          <v-card outlined class="pa-3">
            <v-card-subtitle class="text-h6 font-weight-bold">Audit Number</v-card-subtitle>
            <v-card-text class="text-body-1">{{ audit_number }}</v-card-text>
          </v-card>
        </v-col>
      </v-row>

      <!-- Stage 1 Details -->
      <v-card class="mt-4 pa-4 elevation-2 details-card">
        <v-card-title class="text-h6 font-weight-bold">Stage 1 Details</v-card-title>
        <v-divider class="mb-3"></v-divider>

        <v-row>
          <v-col cols="12" md="4">
            <v-card-subtitle class="text-body-1 font-weight-medium">Date of Audit</v-card-subtitle>
            <v-card-text>{{ formatDate(applicationDetails.stage1.selected_date) }}</v-card-text>
          </v-col>
          <v-col cols="12" md="4">
            <v-card-subtitle class="text-body-1 font-weight-medium">Mail To</v-card-subtitle>
            <v-card-text>{{ applicationDetails.stage1.mail_to }}</v-card-text>
          </v-col>
          <v-col cols="12" md="4">
            <v-card-subtitle class="text-body-1 font-weight-medium">Mail From</v-card-subtitle>
            <v-card-text>{{ applicationDetails.stage1.mail_from }}</v-card-text>
          </v-col>
        </v-row>

        <v-row>
          <v-col cols="6">
            <v-card-subtitle class="text-body-1 font-weight-medium">Date of Comment</v-card-subtitle>
            <v-card-text>{{ formatDate(applicationDetails.stage1.selected_comment_date) }}</v-card-text>
          </v-col>
          <v-col cols="6">
            <v-card-subtitle class="text-body-1 font-weight-medium mt-3">Scope</v-card-subtitle>
            <v-card-text>{{ applicationDetails.stage1.scope }}</v-card-text>
          </v-col>
        </v-row>

        <v-row class="mt-3">
          <v-col cols="12" md="6">
            <v-btn v-if="applicationDetails.stage1.stage1_plan"
                   color="primary"
                   class="elevation-1"
                   @click="downloadFile(applicationDetails.stage1.stage1_plan)">
              Download Stage 1 Plan
            </v-btn>
          </v-col>
          <v-col cols="12" md="6">
            <v-btn v-if="applicationDetails.stage1.stage1_report"
                   color="primary"
                   class="elevation-1"
                   @click="downloadFile(applicationDetails.stage1.stage1_report)">
              Download Stage 1 Report
            </v-btn>
          </v-col>
        </v-row>
      </v-card>

      <!-- Stage 2 Details -->
      <v-card class="mt-4 pa-4 elevation-2 details-card">
        <v-card-title class="text-h6 font-weight-bold">Stage 2 Details</v-card-title>
        <v-divider class="mb-3"></v-divider>

        <v-row>
          <v-col cols="12" md="4">
            <v-card-subtitle class="text-body-1 font-weight-medium">Date of Audit</v-card-subtitle>
            <v-card-text>{{ formatDate(applicationDetails.stage2.selected_date) }}</v-card-text>
          </v-col>
          <v-col cols="12" md="4">
            <v-card-subtitle class="text-body-1 font-weight-medium">Mail To</v-card-subtitle>
            <v-card-text>{{ applicationDetails.stage2.mail_to }}</v-card-text>
          </v-col>
          <v-col cols="12" md="4">
            <v-card-subtitle class="text-body-1 font-weight-medium">Mail From</v-card-subtitle>
            <v-card-text>{{ applicationDetails.stage2.mail_from }}</v-card-text>
          </v-col>
        </v-row>
        <v-row>
          <v-col cols="6">
            <v-card-subtitle class="text-body-1 font-weight-medium">Date of Comment</v-card-subtitle>
            <v-card-text>{{ formatDate(applicationDetails.stage2.selected_comment_date) }}</v-card-text>
          </v-col>
          <v-col cols="6">
            <v-card-subtitle class="text-body-1 font-weight-medium mt-3">Scope</v-card-subtitle>
            <v-card-text>{{ applicationDetails.stage2.scope }}</v-card-text>
          </v-col>
        </v-row>

        <v-row class="mt-3">
          <v-col cols="12" md="6">
            <v-btn v-if="applicationDetails.stage2.stage2_plan"
                   color="primary"
                   class="elevation-1"
                   @click="downloadFile(applicationDetails.stage2.stage2_plan)">
              Download Stage 2 Plan
            </v-btn>
          </v-col>
          <v-col cols="12" md="6">
            <v-btn v-if="applicationDetails.stage2.stage2_report"
                   color="primary"
                   class="elevation-1"
                   @click="downloadFile(applicationDetails.stage2.stage2_report)">
              Download Stage 2 Report
            </v-btn>
          </v-col>
        </v-row>
      </v-card>

      <!-- Back Button -->
      <v-card-actions class="justify-center">
        <v-btn color="blue-darken-3" class="mt-4" @click="$router.push('/application')">
          Back
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-container>
</template>
  
  <script>
  import axios from "axios";
  
  export default {
    props: ["organisation_name"],
    data() {
      return {
        organisation_name: this.$route.params.organisation_name || "",
        audit_number: this.$route.params.audit_number || "",
        applicationDetails: { stage1: {}, stage2: {} },
      };
    },
    methods: {
      async fetchApplicationDetails() {
        try {
          const token = localStorage.getItem("token");
          if (!token) {
            throw new Error("No authentication token found. Please log in again.");
          }
  
          const response = await axios.get(`http://127.0.0.1:5000/application/${this.organisation_name}`, {
            headers: {
              Authorization: `Bearer ${token}`,
            },
          });
  
          this.applicationDetails = response.data;
        } catch (error) {
          console.error("Error fetching application details:", error);
          alert("Failed to fetch details. Please log in again.");
          this.$router.push("/");
        }
      },
  
      async downloadFile(filename) {
        try {
          const token = localStorage.getItem("token");
          if (!token) {
            throw new Error("No authentication token found. Please log in again.");
          }
  
          const cleanFilename = filename.replace(/^uploads\//, "");
          const response = await axios.get(`http://127.0.0.1:5000/download/${encodeURIComponent(cleanFilename)}`, {
            headers: { Authorization: `Bearer ${token}` },
            responseType: "blob",
          });
  
          const blob = new Blob([response.data], { type: response.headers["content-type"] });
          const link = document.createElement("a");
          link.href = window.URL.createObjectURL(blob);
          link.setAttribute("download", cleanFilename);
          document.body.appendChild(link);
          link.click();
          document.body.removeChild(link);
        } catch (error) {
          console.error("Error downloading file:", error);
          alert("Failed to download the file.");
        }
      },

      formatDate(dateString) {
    if (!dateString) return "Invalid Date"; // Handle null/undefined cases

    const date = new Date(dateString);
    if (isNaN(date)) return "Invalid Date"; // Handle incorrect date formats

    return date.toDateString(); // Outputs: "Thu Feb 27 2025"
  }
    },
    created() {
      this.fetchApplicationDetails();
    },
  };
  </script>
  
  
  