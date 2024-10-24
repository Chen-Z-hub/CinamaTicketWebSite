<template>

    <div class="sm">
      <br>
      <br>
        <div class="sm-title"></div>
        <div class="sm-line"></div>
        <div style="display: flex; justify-content: center">
            <div>
                <div style="display: flex" 
                  v-for="(item1, index1) in seatList" :key="index1">
                    <!-- v-if="JSON.stringify(item1) !== '{}'" -->
                    <template>
                        <div @click="seatClk(item)" class="sm-img" 
                            v-for="item in item1" :key="item.id">
                            <img
                                v-if="item.status === 'N'"
                                class="o-w o-h"
                                src="https://hijinka.oss-cn-shanghai.aliyuncs.com/uploads/mall1/20220307/669dde5d9fe28a377c151cadecb8dd65.png"
                                alt=""
                            />
                            <img
                                v-if="item.status === 'Y' && !item.isCheck"
                                class="o-w o-h"
                                src="https://hijinka.oss-cn-shanghai.aliyuncs.com/uploads/mall1/20220307/123044531581e70133020f0265bcabb2.png"
                                alt=""
                            />
                            <img
                                v-if="item.status === 'Y' && item.isCheck"
                                class="o-w o-h"
                                src="https://hijinka.oss-cn-shanghai.aliyuncs.com/uploads/mall1/20220307/899c7f9e0365ce6d97f9d5fe89ffe878.png"
                                alt=""
                            />
                        </div>
                    </template>
                </div>
                <br><br>
                <div style="display: flex; justify-content: center;  align-items: center; ">
                    <el-button type="primary" @click="open()">确认选择</el-button>
                </div>
            </div>
        </div>
    </div>
  </template>
  
  
  <style>
  .sm-img {
    width: 50px;
    height: 50px;
  }
  .sm {
    position: relative;
  }
  .sm-line {
    width: 0;
    height: 200px;
    border: 1px dashed #ccc;
    position: absolute;
    top: 50px;
    left: 50%;
  }
  .sm-title {
    background-color: #dddddd;
    width: 500px;
    height: 17px;
    -webkit-transform: perspective(17px) rotateX(-10deg);
    transform: perspective(17px) rotateX(-10deg);
    margin: 0 auto;
    display: flex;
    align-items: center;
    justify-content: center;
    position: relative;
    z-index: 2;
  }
  </style>
  
  
  <script>
  const url='http://localhost:5006/get_seat';
  const url2='http://localhost:5006/update_seat';
  import { MessageBox } from 'element-ui';
  import { Message } from 'element-ui'; // 如果您也在使用 Message 组件，确保一并导入

  export default {
    name: 'sysIndex',
    components: {},
    async created() {
        this.getSidFromQuery(); // 拿到sid
         try {
             const response = await this.$axios.get(url, {
                 params: {
                     sid: this.sid,
                 },
             });
             this.arrList = response.data;

            // 数据获取完成后再进行二维数组的初始化和填充
            this.initializeSeatList();

         } catch (error) {
             console.error('从后端获取数据时出错:', error);
         }

    },
    data() {
        return {
            sid:'',
            // 返回给后端的数据染的数据
            sendList: [],
            // 页面渲染的数据
            seatList: [],
            // 后端返回的数据
            arrList:[
                // {
                //     id: 1,
                //     seatNo: '1排1座',
                //     status: 'N',
                //     rowNo: '1',
                //     colNo: '1'
                // },
                // {
                //     id: 2,
                //     seatNo: '1排2座',
                //     status: 'N',
                //     rowNo: '1',
                //     colNo: '2'
                // },
            ]
        };
    },
    methods: {
        async initializeSeatList() {
            // 找到行的最大值
            const rowMax = this.findObjInArrMax(this.arrList, 'rowNo', true);
            // 找到列的最大值
            const colMax = this.findObjInArrMax(this.arrList, 'colNo', true);
            const rowNoMax = parseInt(rowMax.rowNo) + 1;
            const colNoMax = parseInt(colMax.colNo) + 1;
            // 将一维数组装成二维数组
            let list = [];
            for (var index = 0; index < rowNoMax; index++) {
                list[index] = [];
                for (var index1 = 0; index1 < colNoMax; index1++) {
                    list[index][index1] = {};
                }
            }
            // 后端返回的数据组合到二维数组里面
            list.forEach((item1, index1) => {
                item1.forEach((item2, index2) => {
                    this.arrList.forEach((item, index) => {
                        item.isCheck = false;
                        list[item.rowNo][item.colNo] = item;
                    });
                });
            });
            console.log('list', list);
            this.seatList = list;
        },
        getSidFromQuery() {
            const sid = this.$route.query.sid;
            this.sid=sid;
            console.log('this.SID from query:', this.sid);
            // 进行后续处理，比如保存到data属性中
        },
        open() {
            MessageBox.confirm('请确认购票信息, 是否继续?', '提示', {
                confirmButtonText: '支付',
                cancelButtonText: '取消',
                type: 'info'
            }).then(() => {

                //返回数据项，将数据发送给后端
                this.sendList=this.seatList.flat(Infinity).filter(item => item !== undefined && item !== null);
                this.sendList=this.sendList.filter(item => {
                    // 检查对象是否有除Vue添加的__ob__以外的自有属性
                    return Object.keys(item).length > 1 || typeof item !== 'object';
                });
                this.$axios.post(url2,{
                    sid: this.sid,
                    list:this.sendList
                }).then(response => {       
                    //处理返回信息
                    if(response.data.success===true){
                        Message({
                        type: 'success',
                        message: '订票成功，可刷新后确认订单!'
                        });
                    //router.push('/home'); // 假设 "/home" 是您的 home 页面的路径
                        this.$store.dispatch('updateActiveMenu', '/');
                        this.$router.push('/');
                    }else{
                        Message({
                        type: 'error',
                        message: '订票失败，可刷新后重新尝试!'
                        });
                    }
                })
                .catch(error => {
                    // 请求失败时的处理逻辑
                    alert('请求失败!');
                });

            }).catch(() => {
                Message({
                type: 'info',
                message: '已取消订单'
                });
            });
        },
        returnAll(){
          //返回数据项，将数据发送给后端
          this.sendList=this.seatList.flat(Infinity).filter(item => item !== undefined && item !== null);
          this.sendList=this.sendList.filter(item => {
            // 检查对象是否有除Vue添加的__ob__以外的自有属性
            return Object.keys(item).length > 1 || typeof item !== 'object';
          });

          this.$axios.post(url2,{
                                sid: this.sid,
                                list:this.sendList
                        })
                        .then(response => {       
                            console.log('Response data:', response.data);
                        })
                        .catch(error => {
                            // 请求失败时的处理逻辑
                            alert('请求失败!');
                        });

        //   try {
        //      const response =await this.$axios.post(url2, {
        //              sid: this.sid,
        //              list:this.sendList
        //      });     
        //         console.log('Response data:', response.data);
            
        //   console.log(
        //     'sid:',this.sid,
        //   'list:',this.sendList);
          //this.$emit('listReturned', this.sendList);
        },
        // 点击座位表
        seatClk(item) {
            // 如果是可以选择，而且没有选中状态
            if (item.status === 'Y' && !item.isCheck) {
                item.isCheck = true;
            } else if (item.status === 'Y' && item.isCheck) {
                item.isCheck = false;
            }
            //console.log(item);
            this.$forceUpdate();
        },
        // 找到数组对象中的最大值
        findObjInArrMax(list, atr, returnVal) {
            let res = Math.max.apply(
                Math,
                list.map((item) => {
                    return item[atr];
                })
            );
            if (returnVal) {
                return list.filter((item) => {
                    return item[atr] == res;
                })[0];
            } else {
                return res;
            }
        },
        // 找到数组对象中的最小值
        findObjInArrMin(list, atr, returnVal) {
            let res = Math.min.apply(
                Math,
                list.map((item) => {
                    return item[atr];
                })
            );
            if (returnVal) {
                return list.filter((item) => {
                    return item[atr] == res;
                })[0];
            } else {
                return res;
            }
        }
    }
  };
  </script>
  
  