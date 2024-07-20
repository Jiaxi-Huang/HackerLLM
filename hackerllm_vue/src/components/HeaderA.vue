<template>
  <v-app-bar app color="#b1ed4a" dark :height="80">
    <v-app-bar-nav-icon @click.stop="toggleDrawer"></v-app-bar-nav-icon>
    <img src="https://www.logosc.cn/oss/icons/2023/01/08/f67e3e299acfd8e8a90d456f994f5eb0.png" alt="Logo" class="logo">
    <v-toolbar-title>
      We <span class="bold-text">Hack</span> the <span class="bold-text">Site</span>
    </v-toolbar-title>
    <v-spacer></v-spacer>
    <v-text-field
      v-model="search"
      append-icon="mdi-magnify"
      label="Search"
      single-line
      hide-details
      class="search-bar"
    ></v-text-field>
    <div class="spacer"></div>
    <!-- 将图片包装在 v-btn 中实现点击跳转 -->
    <v-btn icon href="https://github.com/CeS-3/hackerllm_rag_front_end" target="_blank">
      <img src="https://pngimg.com/uploads/github/github_PNG40.png" alt="Github" class="gitlog">
    </v-btn>
  </v-app-bar>
</template>

<script>
export default {
  name: 'HeaderA',
  data() {
    return {
    };
  },
  methods: {
    toggleDrawer() {
      this.$emit('toggle-drawer');
    }
  }
};
</script>

<style scoped>
.bold-text {
  font-weight: bold;
  font-family: Arial, Helvetica, sans-serif; /* 根据需要调整字体 */
}

.logo {
  width: 5%;
  height: 100%;
  object-fit: contain;
}

.gitlog {
  width: 48px; /* 设置合适的宽度 */
  height: 48px; /* 设置合适的高度 */
  object-fit: contain;
}

.spacer {
  width: 5%;
}
</style>
