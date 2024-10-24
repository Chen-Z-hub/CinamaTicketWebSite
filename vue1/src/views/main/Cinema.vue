<template>
<div>
  <div v-if="selectedMovie">
    <h3>您选择的电影：</h3>
    <div class="if-movie">
      <img class="if-poster" :src="selectedMovie.poster" alt="电影海报" />
      <p>{{ selectedMovie.name }}</p>
    </div>
  </div>
  <!-- 这里是影院筛选器 -->
    <el-form ref="form" :model="form" label-width="80px" class="inner-select">
          <el-form-item label="场次筛选">
          <el-col :span="7">
            <el-select v-model="form.cid" placeholder="选择影院品牌">
              <el-option 
                v-for="(cinema, index) in cinemas"
                :key="index" 
                :label="cinema.name"
                :value="cinema.cid"
              ></el-option>
            </el-select>
          </el-col>
          <el-col :span="7">
            <el-select v-model="form.show_date" placeholder="选择观影日期">
              <el-option 
                v-for="(date, index) in show_date"
                :key="index" 
                :label="date"
                :value="date"
              ></el-option>
            </el-select>
          </el-col>
          <el-col :span="7">
            <el-select v-model="form.show_time" placeholder="选择放映时间">
              <el-option 
                v-for="(time, index) in show_time"
                :key="index" 
                :label="time"
                :value="time"
              ></el-option>
            </el-select>
          </el-col>

        </el-form-item>

      <el-form-item>
        <el-button type="primary" @click="onSubmit()">立即搜索</el-button>
      </el-form-item>
    </el-form>

    <el-table
    :data="cinema_screen"
    style="width: 100%">
      <el-table-column fixed
        prop="cinema.name"
        label="影院名"
        width="200"></el-table-column>
        
      <el-table-column 
        prop="cinema.address" 
        label="电影地址"
        width="500"></el-table-column>

        <el-table-column 
        prop="screen.price" 
        label="价格"
        width="200"></el-table-column>

      <el-table-column fixed="right" label="操作" >
        <template slot-scope="scope">
          <el-button @click="SubmitScreen(scope.row)">立即购票</el-button>
        </template>
      </el-table-column>

    </el-table>


  </div>

</template>

<script>
export default {

  computed: {
    selectedMovie() {
      return this.$store.state.selectedMovie; // 或者其他数据源
    },
  },
  created() {
    // 当组件创建时，从Vuex中同步selectedMovie的mid到form
    if (this.selectedMovie) {
      this.form.mid = this.selectedMovie.mid;
      console.log("create_mid:",this.form.mid);//打表
    }
  },
  data() {
    return {
      cinema_screen:[
        {
          cinema:{cid:1,name:'nihao1',address:'金沙江路1234号'},//电影院
          screen:{sid:1,price:'50',room:'3号巨幕厅'}
        },
        {
          cinema:{cid:2,name:'nihao2',address:'金沙江路2234号'},//电影院
          screen:{sid:2,price:'60',room:'4号巨幕厅'}
        },

      ],
      cinemas:[
        {cid:1,name:'nihao1'},
        {cid:2,name:'nihao2'},
        {cid:3,name:'nihao3'},
      ],
      show_date:[
        "2024-7-05","2024-7-06","2024-7-07"
      ],
      show_time:[
        '7:00','8:00','9:00'
      ],
      form: {
          mid:'',
          cid:'',
          show_time: '',
          show_date: '',
        }

    };
  },
  methods:{
    SubmitScreen(rowData){
      console.log("sid:",rowData.screen.sid);
      this.$router.push('/ticket');
    },
    onSubmit(){
      //console.log("mid:",this.form.mid);
      console.log(this.form);
    }
  }
}
</script>

<style>
.inner-select{
   /* 内容向左对齐 */
   display: flex;
   text-align: left;
   margin-left: 100px;
  /* 可选：为内部组件容器添加一些样式以区分或控制宽度 */
  /*margin: 0 auto; /* 使内部容器在水平方向上居中，同时内容保持左对齐 */
}
.el-col{
  margin-left: 10px;
}
.if-movie{
  width: 100%;
}
.if-poster{
  width: 15%;
  justify-content: center; /* 水平居中 */
  align-items: center; /* 垂直居中 */
}
</style>


