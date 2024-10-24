import router from "./index";
import store from "@/store"; // 确保引入了 Vuex store
//import {LoginState} from "../views/Login.vue"

router.beforeEach((to,from,next)=>{
    //将LoginState存储在浏览器内部空间里，这样刷新就不会导致回到登录界面
    if(to.meta.isLogin){
        let token= localStorage.getItem('LoginState');
        if(token){
            // 登录成功后将登录状态存储在本地存储中
            store.commit('SET_ACTIVE_MENU', to.path);
            next();
        }else{
            next({
                name:'Login'
            })
        }
    }else{
        next();
    }

})