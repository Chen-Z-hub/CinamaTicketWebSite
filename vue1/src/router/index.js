import Vue from 'vue'
//import Home from '../views/main/Home.vue'
import Layout from '../views/Layout.vue'
import VueRouter from 'vue-router'




Vue.use(VueRouter)


const routes=[
    {
        path:"/",
        name:"Layout",
        component:Layout,
        children:[
            {
                path:'',
                name:'Home',
                component: ()=>import("../views/main/Home.vue"),
                meta:{
                    isLogin:true
                }
            },
            {
                path:"myfilm",
                name:'Myfilm',
                component: ()=>import("../views/main/Myfilm.vue"),
                meta:{
                    isLogin:true
                }
            },
            {
                path:"cinema",
                name:'Cinema',
                component: ()=>import("../views/main/Cinema.vue"),
                meta:{
                    isLogin:true
                }
            },
            {
                path:"film",
                name:'FilmCategory',
                component: ()=>import("../views/main/FilmCategory.vue"),
                meta:{
                    isLogin:true
                }
            },
            {
                path:"ticket",
                name:'Ticket',
                component: ()=>import("../views/main/Ticket.vue"),
                meta:{
                    isLogin:true
                }
            }
        ]
    },
    {
        path:'/login',
        name:'Login',
        component:()=>import("../views/Login.vue")
    },
];


const router = new VueRouter({
    mode: 'history', // 使用历史模式或哈希模式，根据你的需求选择
    base: process.env.BASE_URL, // 基本 URL
    routes
 })
 

 export default router

 