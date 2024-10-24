import Vue from 'vue';
import Vuex from 'vuex'


Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    selectedMovie: null,
    activeMenu: '', // 用于存储当前激活的菜单项
    shouldRefresh:false,
  },
  mutations: {
    setMovie(state, movie) {
      state.selectedMovie = movie;
    },
    SET_ACTIVE_MENU(state, menuPath) {
      state.activeMenu = menuPath;
    },
    setRefreshStatus(state, status) {
      state.shouldRefresh = status;
    },
  },
  actions: {
    updateActiveMenu({ commit }, menuPath) {
      commit('SET_ACTIVE_MENU', menuPath);
    }
  }
});