<template>
    <v-container>
      <v-card class="pa-5 mt-3 mx-auto" max-width="800">
        <v-card-title class="white--text" style="background-color: #A00; padding: 10px;">
          Stage 2 Form
        </v-card-title>
  
        <v-card-text>
          <v-form @submit.prevent="submitStage2">
            <v-row>    
              <v-col cols="6">
                <v-text-field v-model="organisationName" label="Organisation Name" disabled></v-text-field>
              </v-col>
              <v-col cols="6">
                <v-text-field v-model="scope" label="Scope" required></v-text-field>
              </v-col>
              <v-col cols="6">
                <v-file-input label="Stage 2 Plan Upload *" v-model="stage2Plan" required></v-file-input>
              </v-col>

              <v-col cols="6">
                <v-file-input label="Additional Data *" v-model="additionaldata"></v-file-input>
              </v-col>
  
              <v-col cols="6">
                <!-- <v-text-field v-model="mailFrom" label="Mail From" required></v-text-field> -->
                <v-text-field v-model="mailTo" label="Mail To" required></v-text-field>
                <!-- <v-select
                  v-model="mailFrom"
                  label="Mail From"
                  :items="['abc@kvqaindia.com', 'training@kvqaindia.com', 'tech@kvqaindia.com']"
                  required
                ></v-select> -->
              </v-col>

              <v-col cols="12">
                <!-- <v-btn v-model="sendmail" >Send Mail</v-btn> -->
                <v-btn color="primary" @click="sendEmail">Send Email</v-btn>
              </v-col>
  
              <!-- <v-col cols="6">
                <v-menu v-model="menu" :close-on-content-click="false" transition="scale-transition">
                  <template v-slot:activator="{ on, attrs }">
                    <v-text-field
                      v-model="selectedDate"
                      label="Select Date"
                      readonly
                      v-bind="attrs"
                      v-on="on"
                    ></v-text-field>
                  </template>
                  <v-date-picker v-model="selectedDate" @input="menu = false"></v-date-picker>
                </v-menu>
              </v-col> -->

              <v-col cols="6">
                <v-menu 
                    v-model="menu" 
                    :close-on-content-click="false" 
                    transition="scale-transition"
                    >
                    <template v-slot:activator="{ props }">
                        <v-text-field
                            v-model="selectedDate"
                            label="Select Date"
                            readonly
                            v-bind="props"
                        ></v-text-field>
                    </template>
                
                <!-- <v-date-picker 
                    v-model="selectedDate"
                    @update:modelValue="updateDate"
                ></v-date-picker> -->
                    <v-container>
                        <v-row justify="space-around">
                        <v-date-picker v-on:update:model-value="changeRoleDate" hide-actions @click.native.stop elevation="24">
                        </v-date-picker>
                        </v-row>
                    </v-container>
                </v-menu>
            </v-col>
    
            </v-row>
            <v-conatiner>
            <h4>Stage 2 report</h4>
            <v-row>   
              <v-col cols="6">
                <v-text-field v-model="comment" label="Comment" required></v-text-field>
              </v-col>
              <v-col cols="6">
                <v-menu 
                    v-model="menucomment" 
                    :close-on-content-click="false" 
                    transition="scale-transition"
                    >
                    <template v-slot:activator="{ props }">
                        <v-text-field
                            v-model="selectedCommentDate"
                            label="Select Date"
                            readonly
                            v-bind="props"
                        ></v-text-field>
                    </template>
                
                <!-- <v-date-picker 
                    v-model="selectedDate"
                    @update:modelValue="updateDate"
                ></v-date-picker> -->
                    <v-container>
                        <v-row justify="space-around">
                        <v-date-picker v-on:update:model-value="changeCommentDate" hide-actions @click.native.stop elevation="24">
                        </v-date-picker>
                        </v-row>
                    </v-container>
                </v-menu>
            </v-col>
            <v-col cols="6">
                <v-file-input label="Stage 2 Report Upload *" v-model="stage2Report" required></v-file-input>
              </v-col>
              <v-col cols="6">
                <v-text-field v-model="mailToReport" label="Mail To" required></v-text-field>
              </v-col>
              <v-col cols="12">
                <!-- <v-btn v-model="sendmail" >Send Mail</v-btn> -->
                <v-btn color="primary" @click="sendEmailReport">Send Email</v-btn>
              </v-col>
            </v-row>
        </v-conatiner>
        <v-col cols="12">
                <v-btn type="submit" color="primary">Submit</v-btn>
        </v-col>
          </v-form>
        </v-card-text>
      </v-card>
    </v-container>
  </template>
  
  <script>
  import axios from "axios"
  export default {
    props: {
        format: String
    },
    data() {
      return {
        organisationName: this.$route.query.orgName || "", // Get org name from query params
        scope: "",
        stage2Plan: null,
        mailFrom: "tech@kvqaindia.com",
        mailTo: "",
        selectedDate: "",
        menu: false,
        selectedDate: null,
        selectedCommentDate: null,
        menucomment: false,
        stage2Report: null,
        comment: "",
        additionaldata: null,
        mailToReport: ""
      };
    },

    computed: {
        selectedDate() {
            if (!this.selectedDate) return "";
            return new Intl.DateTimeFormat("en-GB", {
                day: "2-digit",
                month: "short",
                year: "numeric",
            }).format(new Date(this.selectedDate));
        },

        selectedCommentDate() {
            if (!this.selectedCommentDate) return "";
            return new Intl.DateTimeFormat("en-GB", {
                day: "2-digit",
                month: "short",
                year: "numeric",
            }).format(new Date(this.selectedCommentDate));
        },
  },
    methods: {
    //   async submitStage2() {
    //     if (!this.scope || !this.stage2Plan || !this.mailTo || !this.selectedDate) {
    //         alert("Please fill in all required fields!");
    //         return;
    //     }

    //     let formData = new FormData();
    //     formData.append("organisationName", this.organisationName);
    //     formData.append("scope", this.scope);
    //     formData.append("stage2Plan", this.stage2Plan);
    //     // formData.append("mailFrom", this.mailFrom);
    //     formData.append("mailTo", this.mailTo);
    //     formData.append("selectedDate", this.selectedDate);
    //     formData.append("selectedCommentDate", this.selectedCommentDate);
    //     formData.append("stage2Report", this.stage2Report);
    //     formData.append("comment", this.comment);

    //     const token = localStorage.getItem("token"); // Adjust if using Vuex

    //     try {
    //         const response = await axios.post("http://127.0.0.1:5000/stage2", formData, {
    //           headers: { 
    //             "Content-Type": "multipart/form-data",
    //             "Authorization": `Bearer ${token}` // Attach JWT token
    //         },
    //     });

    //     alert(response.data.message);
    //     this.$router.push({
    //         path: "application",
    //     });

    //     } catch (error) {
    //         console.error("Error submitting Stage 2:", error.response ? error.response.data : error.message);
    //         alert("Failed to submit Stage 2 form.");
    //     }
    // },

    async submitStage2() {
    if (!this.scope || !this.stage2Plan || !this.mailTo || !this.selectedDate) {
        alert("Please fill in all required fields!");
        return;
    }

    let formData = new FormData();
    formData.append("organisationName", this.organisationName);
    formData.append("scope", this.scope);
    formData.append("stage2Plan", this.stage2Plan);
    formData.append("mailFrom", this.mailFrom);
    formData.append("mailTo", this.mailTo);
    formData.append("selectedDate", this.selectedDate);
    formData.append("selectedCommentDate", this.selectedCommentDate);
    formData.append("stage2Report", this.stage2Report);
    formData.append("comment", this.comment);

    let token = localStorage.getItem("token");

    try {
        // const response = await axios.post("http://127.0.0.1:5000/stage2", formData, {
        const response = await axios.post("https://kvqa-data-management-application.onrender.com/stage2", formData, {
            headers: { 
                "Content-Type": "multipart/form-data",
                "Authorization": `Bearer ${token}`
            }
        });

        alert(response.data.message);
        this.$router.push({ path: "application" });

    } catch (error) {
        if (error.response && error.response.status === 401 && error.response.data.msg === "Token has expired") {
            console.log("Token expired, trying to refresh...");

            // Refresh the token
            const newToken = await this.refreshToken();
            if (!newToken) return;

            // Retry request with new token
            try {
                // const response = await axios.post("http://127.0.0.1:5000/stage2", formData, {
                const response = await axios.post("https://kvqa-data-management-application.onrender.com/stage2", formData, {
                    headers: { 
                        "Content-Type": "multipart/form-data",
                        "Authorization": `Bearer ${newToken}`
                    }
                });

                alert(response.data.message);
                this.$router.push({ path: "application" });

            } catch (retryError) {
                console.error("Retry failed:", retryError);
                alert("Failed to submit Stage 2 form.");
            }
        } else {
            console.error("Error submitting Stage 2:", error.response ? error.response.data : error.message);
            alert("Failed to submit Stage 2 form.");
        }
    }
},


      updateDate() {
        this.selectedDate = date
        
      },

      changeRoleDate(date) {
            this.selectedDate = date
            this.menu = false
        },

        changeCommentDate(date) {
            this.selectedCommentDate = date
            this.menucomment = false
        },

        async sendEmail() {
            if (!this.mailTo || !this.stage2Plan || !this.additionaldata) {
                alert("Please fill in all required fields and upload the necessary files!");
                return;
            }

            console.log("Mail Button is clicked!")

            let emailData = new FormData();
            emailData.append("mailTo", this.mailTo);
            emailData.append("subject", "Stage 2 Plan Submission");
            emailData.append("body", "Please find attached the Stage 2 Plan and Additional Data.");
            emailData.append("attachments", this.stage2Plan);
            emailData.append("attachments", this.additionaldata);

            try {
                // const response = await axios.post("http://127.0.0.1:5000/send-email", emailData, {
                const response = await axios.post("https://kvqa-data-management-application.onrender.com/send-email", emailData, {
                    headers: { "Content-Type": "multipart/form-data" },
                });

                alert(response.data.message);
            } catch (error) {
                console.error("Error sending email:", error.response ? error.response.data : error.message);
                alert("Failed to send email.");
            }
        },

        async sendEmailReport() {
    if (!this.mailToReport || !this.stage2Report) {
        alert("Please enter the recipient email and upload the Stage 1 Report!");
        return;
    }

    console.log("Send Report Email button clicked!");

    let reportEmailData = new FormData();
    reportEmailData.append("mailTo", this.mailToReport);
    reportEmailData.append("subject", "Stage 2 Report Submission");
    reportEmailData.append("body", "Please find attached the Stage 2 Report.");
    reportEmailData.append("attachments", this.stage2Report);

    try {
        // const response = await axios.post("http://127.0.0.1:5000/send-email", reportEmailData, {
        const response = await axios.post("https://kvqa-data-management-application.onrender.com/send-email", reportEmailData, {
            headers: { "Content-Type": "multipart/form-data" },
        });

        alert(response.data.message);
    } catch (error) {
        console.error("Error sending report email:", error.response ? error.response.data : error.message);
        alert("Failed to send report email.");
    }
},

async refreshToken() {
    try {
        const refreshToken = localStorage.getItem("refresh_token"); // Retrieve refresh token
        if (!refreshToken) {
            alert("Session expired. Please log in again.");
            this.$router.push("/login");
            return null;
        }

        // const response = await axios.post("http://127.0.0.1:5000/refresh", {
        const response = await axios.post("https://kvqa-data-management-application.onrender.com/refresh", {
            refresh_token: refreshToken,
        });

        // Save new token
        localStorage.setItem("token", response.data.access_token);
        return response.data.access_token;

    } catch (error) {
        console.error("Error refreshing token:", error);
        alert("Session expired. Please log in again.");
        this.$router.push("/login");
        return null;
    }
}

    // selectedDate() {
    //     if (!this.date) return null;
    //         let format = this.format || "%Y-%m-%d";
    //         format = format.replace('%Y', this.date.getYear() + 1900)
    //             .replace('%m', (this.date.getMonth() + 1 + "").padStart(2, "0"))
    //             .replace('%d', (this.date.getDate() + "").padStart(2, "0"));
    //         return format;
    //     }
    }
  };
  </script>
  