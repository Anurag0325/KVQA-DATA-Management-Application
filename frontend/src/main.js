import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import vuetify from './plugins/vuetify' // ✅ Ensure this import is correct

createApp(App).use(store).use(router).use(vuetify).mount('#app')