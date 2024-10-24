<template>
  <div>
    <el-table
      :data="tableData"
      style="width: 100%"
      :default-sort = "{prop: 'date', order: 'descending'}">
      <el-table-column
        type="index"
        width="80">
      </el-table-column>
      <el-table-column
        prop="date"
        label="日期"
        sortable
        width="180">
      </el-table-column>
      <el-table-column
        prop="time"
        label="时间"
        sortable
        width="180">
      </el-table-column>
      <el-table-column
        prop="name"
        label="电影名"
        sortable
        width="180">
      </el-table-column>
      <el-table-column
        prop="address"
        label="地址"
        :formatter="formatter">
      </el-table-column>
      <el-table-column
        prop="cinema"
        label="电影院"
        >
      </el-table-column>
      <el-table-column
        prop="room"
        label="放映厅"
       >
      </el-table-column>
      <el-table-column
        prop="seat"
        label="座位"
        >
      </el-table-column>
      
      <!--删除按钮@click="handleDelete(scope.$index, scope.row)"-->
      <el-table-column
      align="right">
      <template slot-scope="scope">
        <el-button
          size="mini"
          type="danger"
          @click="handleDelete(scope.$index, scope.row)">退票</el-button>
      </template>
    </el-table-column>

    </el-table>
  </div>
</template>

<script>
const url="http://localhost:5006/myfilm";
const url2='http://localhost:5006/delete_order';
import { MessageBox } from 'element-ui';
import { Message } from 'element-ui'; // 如果您也在使用 Message 组件，确保一并导入
export default {
  data() {
    return {
      tableData: [] // 初始化为空数组
    };
  },
  async created() { // 或者使用mounted,根据你的需求选择合适的生命周期钩子
    try {
      const response = await this.$axios.get(url); //替换为你的实际后端API地址
      console.log('Response information:', response.data);
      this.tableData = response.data; // 假设后端返回的数据直接是表格数据数组
    } catch (error) {
      console.error('从后端获取数据时出错:', error);
      // 可以在这里处理错误情况，比如提示用户
    }
  },
  methods: {
    handleDelete(index, row){
      MessageBox.confirm('请确认购票信息, 是否继续?', '提示', {
                confirmButtonText: '退票',
                cancelButtonText: '取消',
                type: 'info'
            }).then(() => {
                // Message({
                // type: 'success',
                // message: '退票成功，可刷新后确认订单!'
                // });
                // 在这里添加跳转到 "home" 的代码
                //删除这一行
                this.$axios.post(url2,{
                  fid:row.fid,
                  date:row.date,
                  time:row.time
                })
                .then(response => {       
                    //console.log('Response data:', response.data);
                    if(response.data.success===true){
                        Message({
                          type: 'success',
                          message: '退票成功，可刷新后确认订单!'
                        });
                    }else{
                        Message({
                          type: 'error',
                          message: '退票成功，可刷新后确认订单!'
                        });
                    }
                })
                .catch(error => {
                    // 请求失败时的处理逻辑
                    alert('退票失败!');
                });
                //router.push('/home'); // 假设 "/home" 是您的 home 页面的路径
                //this.$store.dispatch('updateActiveMenu', '/');
                //this.$router.push('/');

            }).catch(() => {
                Message({
                type: 'info',
                message: '已取消退票操作'
                });
            });   
    },
      formatter(row, column) {
        return row.address;
      }
    }
}
</script>

<style>

</style>