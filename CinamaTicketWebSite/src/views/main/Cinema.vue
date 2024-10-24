<template>
  <div>
    <div v-if="selectedMovie">
      <h3>您选择的电影：</h3>
      <div class="if-movie">
          <img class="if-poster" :src="selectedMovie.poster" alt="电影海报" />
        <p>{{ selectedMovie.name }}</p>
      </div>
    </div>
    <br><br>
    <!-- 这里是影院筛选器 -->
    <el-form ref="form" :model="form" label-width="80px" class="inner-select">
      <el-form-item label="场次筛选">
        <el-col :span="17">
          <el-select v-model="form.show_date" placeholder="选择观影日期">
            <el-option 
              v-for="(date, index) in show_date"
              :key="index" 
              :label="date"
              :value="date"
            ></el-option>
          </el-select>
        </el-col>
      </el-form-item>

      <el-form-item>
        <el-button type="primary" @click="onSubmit()">立即搜索</el-button>
      </el-form-item>
    </el-form>

    <el-table :data="cinema_screen" style="width: 100%">
      <el-table-column fixed prop="name" label="影院名" width="200"></el-table-column>
      <el-table-column prop="address" label="电影地址" width="350"></el-table-column>
      <el-table-column prop="show_time" label="放映起止时间" width="200"></el-table-column>
      <el-table-column prop="price" label="价格" width="200"></el-table-column>
      <el-table-column fixed="right" label="操作">
        <template slot-scope="scope">
          <el-button @click="SubmitScreen(scope.row)">立即购票</el-button>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
const url = "http://localhost:5006/cinema_ticket";
export default {
  computed: {
    selectedCity() {
       return this.$store.state.selectedCity;
    },
    selectedMovie() {
      return this.$store.state.selectedMovie; // 或者其他数据源
    },
  },
  created() {
    // 当组件创建时,从Vuex中同步selectedMovie的mid到form
    if (this.selectedMovie) {
      this.form.mid = this.selectedMovie.mid;
      //console.log("create mid:", this.form.mid); // 打表
    }
    if (this.selectedCity) {
      this.form.city = this.selectedCity;
    }
  },
  data() {
    return {
      cinema_screen: [],
      show_date: ["2024-06-29", "2024-06-30", "2024-07-01"],
      form: {
        city:'',
        mid: '',
        show_date: '',
      },
    };
  },
  methods: {
    SubmitScreen(rowData) {
      //console.log("sid:", rowData.sid);
      //通过sid从后端获取座位
      //this.$router.push('/ticket');
      this.$router.push({
        path: '/ticket',
        query: { sid: rowData.sid } // 通过查询参数传递sid
      });
    },
    async onSubmit() {
      try {
        if (this.selectedCity) {
          this.form.city = this.selectedCity;
        }
        const response = await this.$axios.post(url, {
          city:this.form.city,
          mid: this.form.mid,
          show_date: this.form.show_date,
        });
        this.cinema_screen = response.data;
        //console.log(this.cinema_screen);
      } catch (error) {
        console.error("Error fetching data:", error);
      }
    },
  },
};
</script>

<style>
.inner-select {
  /* 内容向左对齐 */
  display: flex;
  text-align: left;
  margin-left: 100px;
  /* 可选：为内部组件容器添加一些样式以区分或控制宽度 */
  /*margin: 0 auto; /* 使内部容器在水平方向上居中，同时内容保持左对齐 */
}
.el-col {
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
