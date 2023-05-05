import { createApp } from 'vue'
import App from './App.vue'
// import "bootstrap/disct/css/bootstrap.min.css"
import router from './router'
import store from './store'
import axios from 'axios'

// axios.defaults.baseURL = 'http://127.0.0.1:8000'
axios.defaults.baseURL = 'http://43.204.28.3'

createApp(App).use(store).use(router, axios).mount('#app')
