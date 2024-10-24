<template>
    <el-container>
        <el-header>Header</el-header>
        <el-container>
            <el-aside width="50px"></el-aside>
            <el-main><!--main-->
                <div class="movie-list">
                    <br>
                    <div style="margin-top: 15px; width:500px"><!--搜索栏-->
                        <el-input placeholder="请输入内容" v-model="search" class="input-with-select">
                            <el-button slot="append" icon="el-icon-search" @click="searchfilm()"></el-button>
                        </el-input>
                    </div>
                    <br><br>
                    <el-row :gutter="30">
                        <el-col :span="30" v-for="(movie, index) in  paginatedMovies" :key="index">
                            <el-card shadow="hover" class="movie-card" >
                                <img :src="movie.poster" alt="movie.name" class="movie-poster">
                                <div style="padding: 14px;">
                                    <div class="bottom clearfix">
                                        <h3 class="time">{{ movie.name }}</h3>
                                        <br>
                                        <el-button type="text" class="button" @click="ToCinema()">立刻购票</el-button>
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
        <el-footer>Footer</el-footer>
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
    export default {
        data(){
            return{
                search:'',
                movies: [
                    {
                    name: '《流浪地球》1',
                    poster: 'https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png'
                    },
                    {
                    name: '《头号玩家2》',
                    poster: 'https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png'
                    },
                    {
                    name: '《头号玩家》3',
                    poster: 'https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png'
                    },
                    {
                    name: '《头号玩家》4',
                    poster: 'https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png'
                    },
                    {
                    name: '《头号玩家》5',
                    poster: 'https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png'
                    },
                    {
                    name: '《头号玩家》6',
                    poster: 'https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png'
                    },
                    {
                    name: '《头号玩家》7',
                    poster: 'https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png'
                    },
                    {
                    name: '《头号玩家》8',
                    poster: 'https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png'
                    },
                    {
                    name: '《头号玩家》9',
                    poster: 'https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png'
                    },
                    {
                    name: '《头号玩家》10',
                    poster: 'https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png'
                    },
                    {
                    name: '《头号玩家》11',
                    poster: 'https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png'
                    },
                    {
                    name: '《头号玩家》12',
                    poster: 'https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png'
                    },
                    {
                    name: '《头号玩家》13',
                    poster: 'https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png'
                    },
                    {
                    name: '《头号玩家》14',
                    poster: 'https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png'
                    }
                    // 更多电影...
                ],
                currentPage: 1,
                pageSize: 8 // 每页显示的电影数量
            }
        },
        computed: {
            shouldRefresh() {
                return this.$store.state.shouldRefresh;
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
            searchfilm(){
                console.log('search_name',this.search);//换成接口
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
            ToCinema(movie){
            //跳转到cinema界面
                //console.log("mid:",movie.mid);//打表mid
                this.$store.commit('setMovie', movie);
                this.$store.dispatch('updateActiveMenu', '/cinema');
                this.$router.push('/cinema');
            },
        },
        watch:{
            shouldRefresh(newVal) {
                if (newVal) {
                //this.fetchData(); // 或其他刷新逻辑
                alert("nihao");
                }
            },
        }
    }
</script>

