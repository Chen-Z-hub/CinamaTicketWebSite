<template>
    <div class="head">
        <img src="../assets/icon.png" alt="这是一个图标" >

        <el-menu 
        :default-active="$store.state.activeMenu" mode="horizontal" 
        active-text-color="#B886F8" class="nav"
        router
        >
            <el-submenu index="active"><!--城市选项，选择中了选项就将选项传回后端，然后显示在栏目上-->
                <template slot="title" >{{CityName}}</template>
                <el-menu-item @click="CityChange('城市1')">城市1</el-menu-item>
                <el-menu-item @click="CityChange('城市2')">城市2</el-menu-item>
                <el-menu-item @click="CityChange('城市3')">城市3</el-menu-item>
                <el-menu-item @click="CityChange('城市4')">城市4</el-menu-item>
                <el-menu-item @click="CityChange('城市5')">城市5</el-menu-item>
            </el-submenu>

            <el-menu-item index="/">首页</el-menu-item>
            <el-menu-item index="/film">电影</el-menu-item>
            <el-menu-item index="/cinema">影院</el-menu-item>
            <el-menu-item index="/myfilm">我的电影</el-menu-item>
            <el-menu-item class="user">
                <span>{{User}}</span>
                <el-button @click="LogoutHeadle()" >退出</el-button>
            </el-menu-item>
        </el-menu>

    </div>


</template>

<script>
const dstway="https://run.mocky.io/v3/64018916-fa31-4882-b305-6b1a5e5bbc7f";
import { mapState } from 'vuex';
export default {
    data(){
        return{
            active:"/",
            CityName:"城市选择",
            User:localStorage.getItem('Username')
        }
    },
    methods:{
            CityChange(SelectedName){
                this.CityName=SelectedName;
                //this.$store.commit('setRefreshStatus', true);//需要刷新
                //this.$store.commit('setRefreshStatus', false);//需要刷新
                
                if(this.$store.state.shouldRefresh){
                    this.$store.commit('setRefreshStatus', false);//需要刷新
                }else{
                    this.$store.commit('setRefreshStatus', true);//需要刷新
                }
                // 发送 POST 请求
                /*this.$axios.post(dstway,this.CityName)
                .then(response => {
                // 请求成功时的处理逻辑
                /*后端回复的接口应该有这样的数据结构，代表登录成功
                {
                    “success”：ture
                }
                
                    if(response.data.success===true){
                        console.log('Response data:', response.data);
                        this.CityName=SelectedName;
                        console.log(this.CityName);
                    }else{
                        alert('用户不存在');
                    }
                })
                .catch(error => {
                    // 请求失败时的处理逻辑
                    alert('后端链接失败!');
                });*/

            },
            LogoutHeadle(){
                /*LoginState=false;
                this.$router.push('/')*/
                // 清除本地存储中的登录状态
                localStorage.removeItem('LoginState');
                localStorage.removeItem('Username');
                // 重定向到登录页面
                this.$router.push({ name: 'Login' });
            }
    }

}
</script>

<style scoped lang="less" >
.head{
    display: flex;
}
.head>.nav{
    margin-top: 40px;
    margin-left: 50px;
    height: 60px;
    font-size: 50px;
}

.head>.nav>.user{
    margin-left: 450px;
    span{
        margin-right: 50px;
    }
}

</style>