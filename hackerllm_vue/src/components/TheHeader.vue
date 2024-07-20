<template>
  <div class="demo-header">
    <div class="demo-header--title">HackerLLMWithRag</div>
  </div>
</template>

<script>
export default {
  props: {
    colors: {
      type: Object,
      required: true
    },
    chosenColor: {
      type: String,
      required: true
    }
  },
  computed: {
    linkColor() {
      return this.chosenColor === 'dark' ? this.colors.sentMessage.text : this.colors.launcher.bg
    }
  }
}
</script>

<style scoped>
.demo-header {
  width: 100%;
  max-width: 1100px;
  margin: auto;
  padding: 30px 0;
  display: flex;
  justify-content: center; /* 水平居中所有子元素 */
  align-items: center; /* 垂直居中所有子元素 */
  color: white; /* 文本颜色 */
}

.demo-header--title {
  font-size: 24px;
  font-weight: 600;
}

</style>
