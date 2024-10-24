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
                    <el-button type="primary" @click="returnAll()">确认选择</el-button>
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
  export default {
    name: 'sysIndex',
    components: {},
    data() {
        return {
            // 返回给后端的数据染的数据
            sendList: [],
            // 页面渲染的数据
            seatList: [],
            // 后端返回的数据
            arrList: [
                {
                    id: 1,
                    seatNo: '1排1座',
                    status: 'N',
                    rowNo: '1',
                    colNo: '1'
                },
                {
                    id: 2,
                    seatNo: '1排2座',
                    status: 'Y',
                    rowNo: '1',
                    colNo: '2'
                },
                {
                    id: 3,
                    seatNo: '1排3座',
                    status: 'N',
                    rowNo: '1',
                    colNo: '3'
                },
                {
                    id: 4,
                    seatNo: '1排4座',
                    status: 'Y',
                    rowNo: '1',
                    colNo: '4'
                },
                {
                    id: 5,
                    seatNo: '1排5座',
                    status: 'Y',
                    rowNo: '1',
                    colNo: '5'
                },
  
                {
                    id: 6,
                    seatNo: '2排2座',
                    status: 'Y',
                    rowNo: '2',
                    colNo: '2'
                },
                {
                    id: 7,
                    seatNo: '2排3座',
                    status: 'Y',
                    rowNo: '2',
                    colNo: '3'
                },
                {
                    id: 8,
                    seatNo: '2排4座',
                    status: 'Y',
                    rowNo: '2',
                    colNo: '4'
                },
                {
                    id: 9,
                    seatNo: '3排4座',
                    status: 'Y',
                    rowNo: '3',
                    colNo: '4'
                },
                {
                    id: 10,
                    seatNo: '3排5座',
                    status: 'Y',
                    rowNo: '3',
                    colNo: '3'
                }
            ]
        };
    },
    mounted() {
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
  
    methods: {
        returnAll(){
          //返回数据项，将数据发送给后端
          this.sendList=this.seatList.flat(Infinity).filter(item => item !== undefined && item !== null);
          this.sendList=this.sendList.filter(item => {
            // 检查对象是否有除Vue添加的__ob__以外的自有属性
            return Object.keys(item).length > 1 || typeof item !== 'object';
          });
          //console.log(this.sendList);
          this.$emit('listReturned', this.sendList);
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
  
  