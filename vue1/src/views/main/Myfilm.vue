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
        prop="name"
        label="姓名"
        sortable
        width="180">
      </el-table-column>
      <el-table-column
        prop="address"
        label="地址"
        :formatter="formatter">
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
const url="https://run.mocky.io/v3/241f827c-125d-45d6-b2d2-b49a57590886";
export default {
  data() {
    return {
      tableData: [] // 初始化为空数组
    };
  },
  async created() { // 或者使用mounted，根据你的需求选择合适的生命周期钩子
    try {
      const response = await this.$axios.get(url); // 替换为你的实际后端API地址
      console.log('Response information:', response.data);
      this.tableData = response.data.information; // 假设后端返回的数据直接是表格数据数组
    } catch (error) {
      console.error('从后端获取数据时出错:', error);
      // 可以在这里处理错误情况，比如提示用户
    }
  },
  methods: {
      formatter(row, column) {
        return row.address;
      }
    }
}
</script>

<style>

</style>