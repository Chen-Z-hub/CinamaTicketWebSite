import Vue from 'vue'
import App from './App.vue'
import axios from 'axios'
import './plugins/element.js'

import router from './router/index.js'//
import "./assets/css/common.css";
import "./router/permession.js"

import store from './store'; // ����store����

Vue.prototype.$axios = axios;
axios.defaults.baseURL = '/proxy_url'


Vue.config.productionTip = false

new Vue({
  router,//·������
  store, // ʹ��store
  render: h => h(App),
}).$mount('#app')

