<template>
    <el-container>
        <el-header></el-header>
        <el-container>
            <el-aside width="50px"></el-aside>
            <el-main><!--main-->
                <div class="movie-list">
                <br>
                <div style="margin-top:15px;width:500px"><!--搜索栏-->
                    <el-input placeholder="请输入内容" v-model="search" class="input-with-select">
                        <el-button slot="append" icon="el-icon-search" @click="searchfilm()"></el-button>
                    </el-input>
                </div>
                <br>
                <br>
                    <el-row :gutter="30">
                        <el-col :span="5" v-for="(movie, index) in  paginatedMovies" :key="index">
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
                    <div class="pagination">
                        <el-button type="primary" @click="prevPage" :disabled="currentPage === 1">上一页</el-button>
                        <el-button type="primary" @click="nextPage" :disabled="currentPage === totalPages">下一页</el-button>
                    </div>
                </div>
            </el-main>
        </el-container>
        <el-footer></el-footer>
    </el-container>
</template>

<style scoped lang="less">
    .title{
        margin-left: 20px;
        margin-bottom: 10px;
        text-align: left;
    }
    .movie-info {
        display: flex; /* 使用Flex布局 */
        //align-items: center; /* 垂直居中对齐 */
        //justify-content: space-between; /* 在两端对齐，中间留有空白 */
        flex-wrap: nowrap; /* 防止换行 */
        gap: 10px; /* 为元素间添加间隔，如果需要的话 */
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
    .pagination {
        display: flex;
        justify-content: center;
        margin-top: 20px;
    }

</style>

<script>
    const url='http://localhost:5006/all_movies';
    const url2='http://localhost:5006/all_movies_search';
    export default {
        async created() { // 或者使用mounted，根据你的需求选择合适的生命周期钩子
            try {
                const response = await this.$axios.get(url, {
                    params: {
                        city: this.$store.state.selectedCity,
                    },
                });
                this.movies = response.data;
            } catch (error) {
                console.error('从后端获取数据时出错:', error);
            }
        },
        data(){
            return{
                search:'',
                movies: [
                    //{
                    //name: '《流浪地球》1',
                    //poster: 'https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png'
                    //},
                    // 更多电影...
                ],
                currentPage: 1,
                pageSize: 8 // 每页显示的电影数量
            }
        },
         watch: {
            selectedCity: {
                async handler(newVal) {
                    if (newVal) {
                        //alert('??');
                        try {
                            const response = await this.$axios.get(url, {
                                params: {
                                    city: this.$store.state.selectedCity,
                                },
                            });
                            this.movies = response.data;
                        } catch (error) {
                            console.error('从后端获取数据时出错:', error);
                        }
                    }
                },
                immediate: true
            }
        },
        computed: {
            selectedCity() {
                 return this.$store.state.selectedCity;
            },
            totalPages() {
                return Math.ceil(this.movies.length / this.pageSize);
            },
            paginatedMovies() {
                const start = (this.currentPage - 1) * this.pageSize;
                const end = start + this.pageSize;
                return this.movies.slice(start, end);
            }
        },
        methods: {
            // 返回排名对应的类名
            ToCinema(movie){
            //跳转到cinema界面
                this.$store.commit('setMovie', movie);
                console.log("mid:",movie.mid);//打表mid
                this.$store.dispatch('updateActiveMenu', '/cinema');
                this.$router.push('/cinema');
            },
            prevPage() {
                if (this.currentPage > 1) {
                    this.currentPage--;
                }
            },
            nextPage() {
                if (this.currentPage < this.totalPages) {
                    this.currentPage++;
                }
            },
            async searchfilm() {
                try {
                    const response2 = await this.$axios.post(url2, {
                    searchname: this.search,
                    city: this.$store.state.selectedCity
                });
                this.movies = response2.data;
                console.log(this.movies);
                } catch (error) {
                    console.error("Error fetching data:", error);
                }
            },
        }
    }
</script>

