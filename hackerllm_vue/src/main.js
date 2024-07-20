import { createApp } from 'vue'
import App from './App.vue'
import Chat from 'vue3-beautiful-chat'
import vuetify from './plugins/vuetify'
import { loadFonts } from './plugins/webfontloader'
loadFonts()
const app = createApp(App)
app.use(Chat)
app.use(vuetify)
app.mount('#app')