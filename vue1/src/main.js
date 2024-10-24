import Vue from 'vue'
import App from './App.vue'
import axios from 'axios'
import './plugins/element.js'

import router from './router/index.js'//
import "./assets/css/common.css";
import "./router/permession.js"

import store from './store'; // 引入store配置

Vue.prototype.$axios = axios;


Vue.config.productionTip = false

new Vue({
  router,//路由配置
  store, // 使用store
  render: h => h(App),
}).$mount('#app')

