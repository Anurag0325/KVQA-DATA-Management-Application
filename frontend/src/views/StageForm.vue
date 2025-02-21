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
      <v-card class="pa-5 mt-3 mx-auto" max-width="800">
        <v-card-title class="white--text" style="background-color: #A00; padding: 10px;">
          Stage 1 Form
        </v-card-title>
  
        <v-card-text>
          <v-form @submit.prevent="submitStage1">
            <v-row>    
              <v-col cols="6">
                <v-text-field v-model="organisationName" label="Organisation Name" disabled></v-text-field>
              </v-col>
              <v-col cols="6">
                <v-text-field v-model="scope" label="Scope" required></v-text-field>
              </v-col>
              <v-col cols="6">
                <v-file-input label="Stage 1 Plan Upload *" v-model="stage1Plan" required></v-file-input>
              </v-col>

              <v-col cols="6">
                <v-file-input label="Additional Data *" v-model="additionaldata"></v-file-input>
              </v-col>
  
              <!-- <v-col cols="6"> -->
                <!-- <v-text-field v-model="mailFrom" label="Mail From" required></v-text-field> -->
                <!-- <v-text-field v-model="mailTo" label="Mail To" required></v-text-field> -->
                <!-- <v-select
                  v-model="mailFrom"
                  label="Mail From"
                  :items="['abc@kvqaindia.com', 'training@kvqaindia.com', 'tech@kvqaindia.com']"
                  required
                ></v-select> -->
              <!-- </v-col> -->
              <v-col cols="6">
                <v-text-field v-model="mailTo" label="Mail To" required></v-text-field>
              </v-col>
              <v-col cols="12">
                <!-- <v-btn v-model="sendmail" >Send Mail</v-btn> -->
                <v-btn color="primary" @click="sendEmail">Send Email</v-btn>
              </v-col>

              <!-- <v-col cols="6"> -->
                <!-- <v-text-field v-model="mailFrom" label="Mail From" required></v-text-field>
                <v-text-field v-model="mailTo" label="Mail To" required></v-text-field> -->
                <!-- <v-select
                  v-model="mailTo"
                  label="Mail To"
                  :items="['xyz@company.com', 'zxc@company.com', 'qwerty@company.com']"
                  required
                ></v-select>
              </v-col> -->
  
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
            <h4>Stage 1 report</h4>
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
                <v-file-input label="Stage 1 Report Upload *" v-model="stage1Report" required></v-file-input>
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
                <v-btn type="submit" color="primary">Proceed to Stage 2</v-btn>
        </v-col>
          </v-form>
        </v-card-text>
      </v-card>
    </v-container>
  </v-app>
  </template>
  
  <script>
  import axios from "axios";
  export default {
    props: {
        format: String
    },
    data() {
      return {
        organisationName: this.$route.query.org_name || "", // Get org name from query params
        scope: "",
        stage1Plan: null,
        mailFrom: "tech@kvqaindia.com",
        mailTo: "",
        selectedDate: "",
        menu: false,
        selectedDate: null,
        selectedCommentDate: null,
        menucomment: false,
        stage1Report: null,
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
    //   submitStage1() {
    //     console.log("Stage 1 Data Submitted:", {
    //       organisationName: this.organisationName,
    //       scope: this.scope,
    //       stage1Plan: this.stage1Plan,
    //       mailFrom: this.mailFrom,
    //       mailTo: this.mailTo,
    //       selectedDate: this.selectedDate,
    //       selectedCommentDate: this.selectedCommentDate,
    //       stage1Report: this.stage1Report,
    //       comment: this.comment
    //     });
    //     this.$router.push({
    //       path: "/stage2form",
    //       query: {
    //         orgName: this.organisationName
    //       }
    //     });
  
    //     // Navigate to Stage 2 form (extend this later)
    //     alert("Stage 1 submitted! Redirecting to Stage 2...");
    //   },


    // async submitStage1() {
    //     if (!this.scope || !this.stage1Plan || !this.mailFrom || !this.mailTo || !this.selectedDate) {
    //         alert("Please fill in all required fields!");
    //         return;
    //     }

    //     let formData = new FormData();
    //     formData.append("organisationName", this.organisationName);
    //     formData.append("scope", this.scope);
    //     formData.append("stage1Plan", this.stage1Plan);
    //     formData.append("mailFrom", this.mailFrom);
    //     formData.append("mailTo", this.mailTo);
    //     formData.append("selectedDate", this.selectedDate);
    //     formData.append("selectedCommentDate", this.selectedCommentDate);
    //     formData.append("stage1Report", this.stage1Report);
    //     formData.append("comment", this.comment);

    //     try {
    //         const response = await axios.post("http://127.0.0.1:5000/stage1", formData, {
    //             headers: { "Content-Type": "multipart/form-data" },
    //     });

    //     alert(response.data.message);
    //     this.$router.push({
    //         path: "/stage2form",
    //         query: { orgName: this.organisationName }
    //     });

    //     } catch (error) {
    //         console.error("Error submitting Stage 1:", error.response ? error.response.data : error.message);
    //         alert("Failed to submit Stage 1 form.");
    //     }
    // },

    async submitStage1() {
    if (!this.scope || !this.stage1Plan || !this.mailTo || !this.selectedDate) {
        alert("Please fill in all required fields!");
        return;
    }

    let formData = new FormData();
    formData.append("organisationName", this.organisationName);
    formData.append("scope", this.scope);
    formData.append("stage1Plan", this.stage1Plan);
    formData.append("mailFrom", this.mailFrom);
    formData.append("mailTo", this.mailTo);
    formData.append("selectedDate", this.selectedDate);
    formData.append("selectedCommentDate", this.selectedCommentDate);
    formData.append("stage1Report", this.stage1Report);
    formData.append("comment", this.comment);

    // Get the JWT token from local storage or Vuex store
    const token = localStorage.getItem("token"); // Adjust if using Vuex

    try {
        const response = await axios.post("http://127.0.0.1:5000/stage1", formData, {
            headers: { 
                "Content-Type": "multipart/form-data",
                "Authorization": `Bearer ${token}` // Attach JWT token
            },
        });

        alert(response.data.message);
        this.$router.push({
            path: "/stage2form",
            query: { orgName: this.organisationName }
        });

    } catch (error) {
        console.error("Error submitting Stage 1:", error.response ? error.response.data : error.message);
        alert("Failed to submit Stage 1 form.");
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
            if (!this.mailTo || !this.stage1Plan || !this.additionaldata) {
                alert("Please fill in all required fields and upload the necessary files!");
                return;
            }

            console.log("Mail Button is clicked!")

            let emailData = new FormData();
            emailData.append("mailTo", this.mailTo);
            emailData.append("subject", "Stage 1 Plan Submission");
            emailData.append("body", "Please find attached the Stage 1 Plan and Additional Data.");
            emailData.append("attachments", this.stage1Plan);
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
    if (!this.mailToReport || !this.stage1Report) {
        alert("Please enter the recipient email and upload the Stage 1 Report!");
        return;
    }

    console.log("Send Report Email button clicked!");

    let reportEmailData = new FormData();
    reportEmailData.append("mailTo", this.mailToReport);
    reportEmailData.append("subject", "Stage 1 Report Submission");
    reportEmailData.append("body", "Please find attached the Stage 1 Report.");
    reportEmailData.append("attachments", this.stage1Report);

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

goBack() {
    this.$router.push('/application');
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
  