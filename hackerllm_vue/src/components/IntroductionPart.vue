<template>
  <v-main class="main">
    <v-row no-gutters>
      <div class="spacer"></div>
      <v-col col="1" class="d-flex justify-start">
        <div>
          <span class="title">We "Hack" <br>the Site<br></span>
          <span class="subtitle">analysis hacker site <br>and find out way to become a good hacker.</span>
        </div>
      </v-col>
    </v-row>
  </v-main>
  <v-main style="margin-top: 0; margin-bottom: 0; padding-top: 0; padding-bottom: 0;">
    <v-row>
      <div class="spacer"></div>
      <v-col>
        <span class="articleTitle">Introduction</span><br>
        <span class="articleSubTitle">What this project does</span>
        <v-divider></v-divider>
        <v-row>
          <v-col cols="12" md="4" offset="10">
            <v-btn color="#b1ed4a" @click="showDialog">
              <v-icon>mdi-account</v-icon>
              <span>Group Member</span>
            </v-btn>
          </v-col>
          <v-col cols="11">
            <p class="article">
          This project aims to analyze hacker-related data from various websites to uncover the key factors that contribute to becoming an excellent hacker. By extracting and analyzing data from platforms like HackerOne, Hack The Box, and Hack This Site, we seek to provide structured guidance for aspiring hackers. The high entry barriers in the field, including the lack of clear starting points, necessary skills, and effective practice methods, motivate this project. We will utilize advanced data processing techniques such as Principal Component Analysis, Correlation/Cluster Analysis, and Feature Importance Analysis to understand the primary factors influencing hacker rankings. Additionally, we aim to implement a Retrieval-Augmented Generation (RAG) system to generate personalized learning recommendations for beginners. This project also includes the development of a website using FastAPI and Vue.js to facilitate easy access to our findings and recommendations, leveraging the capabilities of Qwen2 for chatbot integration. Ultimately, our goal is to lower the barriers to entry and provide actionable insights and resources for those looking to excel in the cybersecurity domain.
        </p>
          </v-col>
        </v-row>

        <div style="height: 50px;"></div>
      </v-col>
    </v-row>
  </v-main>
  <v-dialog v-model="localDialog" class="custom-dialog">
    <v-card class="custom-card">
      <v-card-title class="dialog-headline"><span style="font-weight: bold;">Group Member Introduction</span></v-card-title>
      <v-card-text style="color: black;">
        <h3>Group Member</h3>
        LI LANZHE<br>
        HUANG YUHAO<br>
        HUANG JIAXI<br>
        ZHU ZIYI<br>
        WANG YUYU<br>
        <br>
        <h3>Work Allocation</h3>
        <span class ="work-allocation">Data Collection</span> HUANG YUHAO, HUANG JIAXI<br>
        <span class ="work-allocation">Data Analysis and Evaluation</span>: ZHU ZIYI, WANGYUYU, LI LIANZHE<br>
        <span class ="work-allocation">Model Train and Deploy</span>: HUANG JIAXI, LI LIANZHE<br>
        <span class ="work-allocation">Website Development</span>:HUANG JIAXI, HUANG YUHAO<br>
      </v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn color="primary" text @click="hideDialog">Close</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
export default {
  name: 'IntroductionPart',
  props: {
    dialog: {
      type: Boolean,
      required: true
    }
  },
  data() {
    return {
      localDialog: this.dialog
    };
  },
  watch: {
    dialog(val) {
      this.localDialog = val;
    },
    localDialog(val) {
      this.$emit('update:dialog', val);
    }
  },
  methods: {
    showDialog() {
      this.localDialog = true;
    },
    hideDialog() {
      this.localDialog = false;
    }
  }
};
</script>

<style>
@keyframes fadeIn {
  0% {
    opacity: 0;
  }
  100% {
    opacity: 1;
  }
}

.main {
  width: 100vw;
  height: 950px;
  background-image: url('https://cdn.pixabay.com/photo/2022/08/12/12/25/vulture-7381642_1280.jpg');
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  overflow: hidden;
  animation: fadeIn 3s ease-in-out;
}
.title {
  font-family: Arial, sans-serif;
  font-size: 6em;
  font-weight: bold;
  line-height: 1.5;
  color: white;
}
.subtitle {
  font-family: Arial, sans-serif;
  font-size: 1.75em;
  line-height: 1.0;
  color: rgb(156, 147, 147);
}
.spacer {
  width: 7%;
}
.article {
  font-family: Arial, sans-serif;
  font-size: 1.75em;
  line-height: 1.5;
  color: white;
}
.articleTitle {
  font-family: Arial, sans-serif;
  font-size: 5em;
  font-weight: bold;
  line-height: 1.5;
  color: white;
  text-decoration: underline
}
.articleSubTitle {
  font-family: Arial, sans-serif;
  font-size: 1.75em;
  line-height: 1.0;
  color: rgb(156, 147, 147);
}
.custom-dialog {
  max-width: 700px;
}
.custom-card {
  height: 450px; /* 设置对话框的高度 */
}
.dialog-headline {
  background-color: #b1ed4a;
}
.work-allocation {
  font-weight: bold;
}
</style>
