<template>
  <v-app class="custom-app-background">
    
    <HeaderA @toggle-drawer="drawer = !drawer" />
    <AppSidebar v-model:drawer="drawer" v-model:mini-variant="miniVariant" />
    <IntroductionPart></IntroductionPart>
    <v-main>
        <v-container fluid>
        <GraphDisplayArea></GraphDisplayArea>
        <div>
      <beautiful-chat
        :always-scroll-to-bottom="alwaysScrollToBottom"
        :close="closeChat"
        :colors="colors"
        :is-open="isChatOpen"
        :message-list="messageList"
        :message-styling="messageStyling"
        :new-messages-count="newMessagesCount"
        :on-message-was-sent="onMessageWasSent"
        :open="openChat"
        :participants="participants"
        :show-close-button="true"
        :show-launcher="true"
        :show-emoji="false"
        :show-file="false"
        :show-typing-indicator="showTypingIndicator"
        :show-edition="true"
        :show-deletion="true"
        :show-confirmation-deletion="true"
        :confirmation-deletion-message="'确定删除？'"
        :title-image-url="titleImageUrl"
        :disable-user-list-toggle="false"
        @onType="handleOnType"
        @edit="editMessage"
        @remove="removeMessage"
      >
        <template v-slot:header>
          chat between {{ participants.map((m) => m.name).join(' & ') }}
        </template>
        <template v-slot:text-message-toolbox="scopedProps">
          <button
            v-if="!scopedProps.me && scopedProps.message.type === 'text'"
            @click.prevent="like(scopedProps.message.id)"
          >
            👍
          </button>
        </template>
        <template v-slot:text-message-body="scopedProps">
          <p class="sc-message--text-content" v-html="scopedProps.messageText"></p>
          <p
            v-if="scopedProps.message.data.meta"
            class="sc-message--meta"
            :style="{color: scopedProps.messageColors.color}"
          >
            {{ scopedProps.message.data.meta }}
          </p>
          <p
            v-if="scopedProps.message.isEdited || scopedProps.message.liked"
            class="sc-message--edited"
          >
            <template v-if="scopedProps.message.isEdited">✎</template>
            <template v-if="scopedProps.message.liked">👍</template>
          </p>
        </template>
        <template v-slot:system-message-body="{message}"> [System]: {{ message.text }} </template>
      </beautiful-chat>
    </div>
      </v-container>

    </v-main>


  </v-app>

  
</template>

<script>
import HeaderA from './components/HeaderA.vue';
import AppSidebar from './components/AppSidebar.vue'
import messageHistory from './components/messageHistory'
import chatParticipants from './components/chatProfiles'
import availableColors from './components/colors'
import IntroductionPart from './components/IntroductionPart.vue'
import GraphDisplayArea from './components/GraphDisplayArea.vue'



export default {
  name: 'App',
  components: {
    HeaderA,
    AppSidebar,
    IntroductionPart,
    GraphDisplayArea,
  },
  data() {
    return {
      participants: chatParticipants,
      titleImageUrl: 'https://th.bing.com/th?id=ODLS.25f47eaa-cc98-4cdb-8fa4-5fec7f196820&w=32&h=32&qlt=90&pcl=fffffa&o=6&pid=1.2',
      messageList: messageHistory,
      newMessagesCount: 0,
      isChatOpen: false,
      showTypingIndicator: '',
      colors: null,
      availableColors,
      chosenColor: null,
      alwaysScrollToBottom: true,
      messageStyling: true,
      userIsTyping: false,
      drawer: false,
      dialog: false
    }
  },
  computed: {
    linkColor() {
      return this.chosenColor === 'dark' ? this.colors.sentMessage.text : this.colors.launcher.bg
    },
    backgroundColor() {
      return this.chosenColor === 'dark' ? this.colors.messageList.bg : '#fff'
    }
  },
  created() {
    this.setColor('dark')
  },
  mounted() {
    this.messageList.forEach((x) => (x.liked = false))
  },
  methods: {
    // 这里是由robot发送调用的发送函数
    // user的发送由chat组件完成
    sendSupportMessage(text) {
      if (text.length > 0) {
        this.newMessagesCount = this.isChatOpen ? this.newMessagesCount : this.newMessagesCount + 1
        this.onMessageWasSent({
          author: 'support',
          type: 'text',
          id: Math.random(),
          data: {text}
        })
      }
    },
    sendSystemMessage(text) {
      if (typeof text === 'string' && text.length > 0) {
        this.newMessagesCount = this.isChatOpen ? this.newMessagesCount : this.newMessagesCount + 1;

        // 获取当前时间
        const date = new Date();
        const day = String(date.getDate()).padStart(2, '0');
        const month = String(date.getMonth() + 1).padStart(2, '0'); // 月份从0开始，所以要加1
        const year = date.getFullYear();
        const hours = String(date.getHours()).padStart(2, '0');
        const minutes = String(date.getMinutes()).padStart(2, '0');

        // 组合成所需格式
        const formattedDate = `${month}-${day}-${year} ${hours}:${minutes}`;

        // 发送信息
        this.onMessageWasSent({
          type: 'system',
          id: Math.random(), // 这里可以考虑使用更可靠的唯一 ID 生成方法
          data: {
            text: text,
            meta: formattedDate
          }
        });
      }
    },
    handleTyping(text) {
      this.showTypingIndicator =
        text.length > 0 ? this.participants[this.participants.length - 1].id : ''
    },
    //onMessageWasSent就是发送信息的回调函数
    onMessageWasSent(message) {
      // 将信息打在公屏上
      this.messageList = [...this.messageList, Object.assign({}, message, { id: Math.random() })];
      // 仅在用户发出信息后进行相关操作
      if (message.author == "me") {
        console.log('Sending message to backend:', message);
        let request = {
          question: message.data.text
        };
        console.log(request)
        fetch("http://localhost:8886/api", {
          method: 'POST', // 请求方法
          headers: {
            'Content-Type': 'application/json', // 请求头，表示请求体是 JSON 格式
          },
          body: JSON.stringify(request) // 请求体，将 JavaScript 对象转换为 JSON 字符串
        })
        .then(response => {
          console.log('Response status:', response.status); // 记录响应状态
          if (!response.ok) {
            this.sendSystemMessage("Internal Server Error")
            throw new Error('Network response was not ok');
          }
          return response.json();
        })
        .then(data => {
          console.log('Response data:', data); // 记录响应数据
          // 将机器人的回复发送出去
          this.sendSupportMessage(data.response);
        })
        .catch(error => {
          this.sendSystemMessage("Internal Server Error")
          console.error('There has been a problem with your fetch operation:', error);
        });
      }
    },
    openChat() {
      this.isChatOpen = true
      this.newMessagesCount = 0
    },
    closeChat() {
      this.isChatOpen = false
    },
    setColor(color) {
      this.colors = this.availableColors[color]
      this.chosenColor = color
    },
    showStylingInfo() {
      alert(
        'You can use *word* to <strong>boldify</strong>, /word/ to <em>emphasize</em>, _word_ to <u>underline</u>, `code` to <code>write = code;</code>, ~this~ to <del>delete</del> and ^sup^ or ¡sub¡ to write <sup>sup</sup> and <sub>sub</sub>'
      )
      // this.$modal.show('dialog', {
      //   title: 'Info',
      //   text:
      //     'You can use *word* to <strong>boldify</strong>, /word/ to <em>emphasize</em>, _word_ to <u>underline</u>, `code` to <code>write = code;</code>, ~this~ to <del>delete</del> and ^sup^ or ¡sub¡ to write <sup>sup</sup> and <sub>sub</sub>'
      // })
    },
    messageStylingToggled(e) {
      this.messageStyling = e.target.checked
    },
    handleOnType(e) {
      this.$event.$emit('onType', e)
      this.userIsTyping = true
    },
    editMessage(message) {
      const m = this.messageList.find((m) => m.id === message.id)
      m.isEdited = true
      m.data.text = message.data.text
    },
    removeMessage(message) {
      const m = this.messageList.find((m) => m.id === message.id)
      m.type = 'system'
      m.data.text = 'This message has been removed'
    },
    like(id) {
      const m = this.messageList.findIndex((m) => m.id === id)
      var msg = this.messageList[m]
      msg.liked = !msg.liked
      this.messageList[m] = msg
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: left;
  color: #2c3e50;
  margin-top: 60px;
}
@import '~vuetify/dist/vuetify.min.css';
.custom-app-background {
  background-color: #161c2a; /* 你想要的背景颜色 */
}
</style>