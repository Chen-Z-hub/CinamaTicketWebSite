<template>
    <el-container>
        <el-header>Header</el-header>
        <el-container>
            <el-main><!--main-->
                <div class="movie-list">
                    <h3 class="title">正在热映></h3>
                    <el-row :gutter="30">
                        <el-col :span="7" v-for="(movie, index) in movies" :key="index">
                            <el-card shadow="hover" class="movie-card" >
                                <img :src="movie.poster" alt="movie.name" class="movie-poster">
                                <div style="padding: 14px;">
                                    <div class="bottom clearfix">
                                        <h3 class="time">{{ movie.name }}</h3>
                                        <br>
                                        <el-button type="text" class="button" @click="ToCinema(movie)">立刻购票</el-button>
                                    </div>
                                </div>
                            </el-card>
                        </el-col>
                    </el-row>
                </div>
            </el-main>
            <el-aside width="500px"><!--Aside-->
                <div class="rating-list">
                    <h3 class="title">高分推荐></h3>
                    <el-col 
                    v-for="(item, index) in ratings" 
                    :key="index" 
                    :class="[getRankClass(index)]"
                    :span="24"
                    >
                    <el-card shadow="hover" class="movie-info">
                        <div class="rank" :class="getRankColorClass(index)">{{ index + 1 }}</div>
                        <div class="name">{{ item.name }}</div>
                        <el-rate 
                        v-model="item.score" 
                        disabled 
                        show-score 
                        text-color="#ff9900" 
                        score-template="{value}"
                        ></el-rate>
                    </el-card>
                    </el-col>
                </div>
            </el-aside>
        </el-container>
        <el-footer>Footer</el-footer>
    </el-container>
</template>

<style scoped lang="less">
    .title{
        margin-left: 20px;
        margin-bottom: 10px;
        text-align: left;
    }

    .rating-list {
  /* 可以根据需要添加额外样式 */
        margin-top: 30px;
    }
    .movie-info {
        display: flex; /* 使用Flex布局 */
        //align-items: center; /* 垂直居中对齐 */
        //justify-content: space-between; /* 在两端对齐，中间留有空白 */
        flex-wrap: nowrap; /* 防止换行 */
        gap: 10px; /* 为元素间添加间隔，如果需要的话 */
    }
    .rank {
    display: inline-block;
    width: 60px; /* 根据需要调整宽度 */
    text-align: right;
    padding-right: 10px;
    }
    .bold {
    font-weight: bold;
    }
    .red {
    color: red;
    }
    .orange {
    color: orange;
    }
    .yellow {
    color: yellow;
    }
    .name {
    margin-left: 10px;
    }

    .movie-card{
        padding: 0px; 
        margin-bottom: 20px;
    }
    .movie-poster {
        width: 100%;
        height: auto;
    }
    .el-header, .el-footer {
        margin-top: 10px;
        background-color: #e3d6f5;
        color: #333;
        text-align: center;
        line-height: 60px;
    }

</style>

<script>
    import BookingButton from '../../components/BookButton.vue';
    const url='https://run.mocky.io/v3/5381d9dc-d6a1-4ae3-9914-59b9b908af14';
    export default {
        async created() { // 或者使用mounted，根据你的需求选择合适的生命周期钩子
            try {
            const response = await this.$axios.get(url); // 替换为你的实际后端API地址
            console.log('Response information:', response.data);
            this.movies = response.data; // 假设后端返回的数据直接是表格数据数组
            } catch (error) {
            console.error('从后端获取数据时出错:', error);
            // 可以在这里处理错误情况，比如提示用户
            }
        },
        components:{
            BookingButton
        },
        data(){
            return{
                ratings: [
                    { name: '电影A', score: 4.5 },
                    { name: '电影B', score: 4.0 },
                    { name: '电影C', score: 3.5 },
                    { name: '电影C', score: 3.5 },
                    { name: '电影C', score: 3.5 },
                    { name: '电影C', score: 3.5 },
                    // 更多电影...
                ],
                movies: [
                    {name:'神奇女侠',poster:'http://p1.meituan.net/movie/f013c57e9506cd2e7c609397c8da04d9213647.jpg@464w_644h_1e_1c',mid:'1'}
                ]
                /*
                {name:'',poster:'',mid:''}
                movies:[
                    {name:'神奇女侠',poster:'http://p1.meituan.net/movie/f013c57e9506cd2e7c609397c8da04d9213647.jpg@464w_644h_1e_1c',mid:'1'}
                ]
                */ 
            }
        },
        methods: {
            /*
            <el-button type="text" class="button" @click="Book(movie.name,movie.poster)">立刻购票</el-button>
            Book(name,poster){
                //this.$router.push('/ticket');
                this.$router.push({ path: `/ticket/${encodeURIComponent(name)}/${encodeURIComponent(poster)}` })
            },*/
            // 返回排名对应的类名
            ToCinema(movie){
            //跳转到cinema界面
                //console.log("mid:",movie.mid);//打表mid
                this.$store.commit('setMovie', movie);
                this.$store.dispatch('updateActiveMenu', '/cinema');
                this.$router.push('/cinema');
            },
            getRankClass(index) {
                return { first: index === 0, second: index === 1, third: index === 2 };
            },
            // 返回排名颜色的类名
            getRankColorClass(index) {
                return { red: index === 0, orange: index === 1, yellow: index === 2, bold: true };
            },
        }
    }
</script>

