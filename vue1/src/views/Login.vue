<template>
    <div class="login">
        <el-card class="box-card">
            <div slot="header" class="clearfix">
                <span>欢迎来到影票速达网</span>
            </div>
            <!--滑动栏-->
            <el-tabs v-model="currentIndex" stretch @tab-click="handleTabsClick">
                <el-tab-pane label="登录" name="login">
                    <!--用户名、密码输入框-->
                    <!--这里的username实际上是uid，也就是账户-->
                    <el-form :model="loginForm" :rules="rules" ref="loginForm" status-icon label-width=90px>
                        <el-form-item label="账户" prop="username">
                            <el-input type="text" v-model="loginForm.username"/>
                        </el-form-item>
                        <el-form-item label="密码" prop="password">
                            <el-input type="password" v-model="loginForm.password"/>
                        </el-form-item>
                        <el-form-item>
                            <el-button type="primary" @click="submitForm('loginForm')">提交</el-button>
                        </el-form-item>
                    </el-form>
                </el-tab-pane>
                <el-tab-pane label="注册" name="register">
                    <!--用户名、密码、确认密码输入框-->
                    <el-form :model="registerForm" :rules="rules" ref="registerForm" status-icon label-width=90px>
                        <el-form-item label="账户" prop="username">
                            <el-input type="text" v-model="registerForm.username"/>
                        </el-form-item>
                        <el-form-item label="密码" prop="password">
                            <el-input type="password" v-model="registerForm.password"/>
                        </el-form-item>
                        <el-form-item label="确认密码" prop="confirmPassword">
                            <el-input type="password" v-model="registerForm.confirmPassword"/>
                        </el-form-item>
                        <el-form-item>
                            <el-button type="primary" @click="submitForm('registerForm')">提交</el-button>
                        </el-form-item>
                    </el-form>
                </el-tab-pane>
            </el-tabs>
            
        </el-card>
    </div>
</template>

<script>

const dstway="https://run.mocky.io/v3/64018916-fa31-4882-b305-6b1a5e5bbc7f";
const dstway2="https://run.mocky.io/v3/64018916-fa31-4882-b305-6b1a5e5bbc7f";
//const dstway="http:// 192.168.199.38:5000/login";//连接登录后端
//const dstway2="http://192.168.199.38:5000/register";//连接注册后端
//export var LoginState = false;
export var Username = null;

export default {
    data(){
        //验证规则
        var validateUserName=(rule,value,callback)=>{
            if(value===''){
                callback(new Error("请输入用户名"));
            }else{
                callback();
            }
        }
        var validatePassword=(rule,value,callback)=>{
            if(value.length==''){
                callback(new Error("请输入密码"));
            }else{
                callback();
            }
        }
        var validateConfirmPassword=(rule,value,callback)=>{
            if(value.length==''){
                callback(new Error("请输入密码"));
            }else if(value!=this.registerForm.password){
                callback(new Error("两次密码不一致"));
            }else{
                callback();
            }
        }

        return{
            currentIndex:"login",
            activeTab:"login",
            loginForm:{
                username:"",
                password:""
            },
            registerForm:{
                username:"",
                password:"",
                confirmPassword:""
            },
            rules:{
                username:[
                    {
                        validator:validateUserName,
                        trigger:"blur"
                    }
                ],
                password:[
                    {
                        validator:validatePassword,
                        trigger:"blur"
                    }
                ],
                confirmPassword:[
                    {
                        validator:validateConfirmPassword,
                        trigger:"blur"
                    }
                ]

            }
        }
    },
    methods:{
        submitForm(formName){
            this.$refs[formName].validate((valid) => {
                if (valid) {
                    if(this.activeTab==='login'){//这里可以写接口把数据提交给后台
                        // 发送 POST 请求
                        this.$axios.post(dstway,this.loginForm)
                        .then(response => {
                        // 请求成功时的处理逻辑
                        /*后端回复的接口应该有这样的数据结构，代表登录成功
                        {
                            “success”：ture
                        }
                        */
                        if(response.data.success===true){
                            console.log('Response data:', response.data);
                            //LoginState=true;    
                            localStorage.setItem('LoginState', true);
                            //这里的username是真正的用户名
                            Username=response.data.user;
                            console.log('Username:', Username);
                            localStorage.setItem('Username', Username);
                            this.$router.push('/')
                        }else{
                            alert('用户不存在');
                        }
                        })
                        .catch(error => {
                        // 请求失败时的处理逻辑
                        alert('登录失败!');
                        });
                            console.log(this.loginForm);
                    }else if(this.activeTab==='register'){//这里是注册的逻辑
                        console.log(this.registerForm);
                        // 发送 POST 请求
                        this.$axios.post(dstway2,this.registerForm)
                        .then(response => {
                        // 请求成功时的处理逻辑
                        /*后端回复的接口应该有这样的数据结构，代表登录成功
                        {
                            “success”：ture
                        }
                        */
                        console.log(response);
                        if(response.data.success===true){
                            alert('注册成功');
                        }else{
                            alert('用户已存在');
                        }
                        })
                        .catch(error => {
                        // 请求失败时的处理逻辑
                        alert('注册失败!');
                        });

                    }
                } else {
                    alert('输入数据不合法!');
                    return ;
                }
            })
        },
        handleTabsClick(tab){
            this.activeTab=tab.name;
        }
    }
}
</script>


<style scoped lang="less">

.login{
    width:1200px;
    margin: 0 auto;
    .box-card{
        width: 500px;
        margin: 100px auto;
    }
}

</style>