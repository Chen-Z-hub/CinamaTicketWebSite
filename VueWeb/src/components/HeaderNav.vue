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
                <el-menu-item @click="CityChange('上海')">上海</el-menu-item>
                <el-menu-item @click="CityChange('广州')">广州</el-menu-item>
                <el-menu-item @click="CityChange('苏州')">苏州</el-menu-item>
                <el-menu-item @click="CityChange('泰州')">泰州</el-menu-item>
                <el-menu-item @click="CityChange('无锡')">无锡</el-menu-item>
                <el-menu-item @click="CityChange('南京')">南京</el-menu-item>
                <el-menu-item @click="CityChange('徐州')">徐州</el-menu-item>
                <el-menu-item @click="CityChange('常州')">常州</el-menu-item>
                <el-menu-item @click="CityChange('连云港')">连云港</el-menu-item>
                <el-menu-item @click="CityChange('盐城')">盐城</el-menu-item>
                <el-menu-item @click="CityChange('扬州')">扬州</el-menu-item>
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
const dstway="http://localhost:5006/city";
import { mapState } from 'vuex';
export default {
    data(){
        return{
            active:"/",
            CityName:"上海",
            User:localStorage.getItem('Username')
        }
    },
    methods:{
            CityChange(SelectedName){
                this.CityName=SelectedName;
                this.$store.commit('setSelectedCity', this.CityName);
            },
                // if(this.$store.state.shouldRefresh){
                //     this.$store.commit('setRefreshStatus', false);//需要刷新
                // }else{
                //     this.$store.commit('setRefreshStatus', true);//需要刷新
                // }
                // 发送 POST 请求
                // this.$axios.post(dstway,{ cityName: this.CityName })
                // .then(response => {
                // // 请求成功时的处理逻辑
                // /*后端回复的接口应该有这样的数据结构
                // {
                //     "success":true
                // }
                // */
                //     if(response.data.success===true){
                //         //console.log('Response data:', response.data);
                //         this.CityName=SelectedName;
                //         //console.log(this.CityName);
                //     }else{
                //         alert('用户不存在');
                //     }
                // })
                // .catch(error => {
                //     // 请求失败时的处理逻辑
                //     alert('后端链接失败!');
                // });
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
    margin-left: 200px;
    span{
        margin-right: 50px;
    }
}

</style>