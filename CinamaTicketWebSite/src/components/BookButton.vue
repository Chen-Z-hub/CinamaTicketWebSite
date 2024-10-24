<template>

  <el-popover
    placement="right"
    width="600"
    v-model="visible">
    <!-- <Booking/>-->
    <Booking/>
    <el-button slot="reference">购票</el-button>
  </el-popover>
</template>

<script>
import Booking from './Booking.vue';

export default {
  components:{
    Booking
  },
  data() {
    return {
      visible: false,
    };
  }
}


</script>

<style>

</style>