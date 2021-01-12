<template>
    <el-table
      :data="tableData"
      :span-method="objectSpanMethod"
      border
      style="width: 100%; margin-top: 20px">
      <el-table-column
        prop="id"
        label=""
        width="180">
      </el-table-column>
      <el-table-column
        prop="name"
        label="">
      </el-table-column>
      <el-table-column
        prop="amount1"
        label="工艺一">
      </el-table-column>
      <el-table-column
        prop="amount2"
        label="工艺二">
      </el-table-column>
      <el-table-column
        prop="amount3"
        label="工艺三">
      </el-table-column>
    </el-table>
</template>
<script>
import { GetSystemInfo, GetSystemInfoHistory,GetPoolInfoHistory } from "@/api/device";
export default {

  props:['deviceId'],
  data() {
    return {
        tableData: [],
    }
  },
  async mounted() {
      var sysInfo = await GetSystemInfo(1);
      var names = ['温度','升温速率','保持时间'];
      var steps =['first','second','third'];
      if(sysInfo.status === 200) {
          for(var i = 0; i < 9; i++){
            var obj = {
                id: '第'+(parseInt(i/3)+1)+'阶段',
                name: names[i%3],
                amount1: sysInfo.data['temp_'+steps[parseInt(i/3)]+'_step_craft_'+(i%3+1)]*0.1,
                amount2: sysInfo.data['temp_rate_'+steps[parseInt(i/3)]+'_step_craft_'+(i%3+1)]*0.1,
                amount3: sysInfo.data['duration_'+steps[parseInt(i/3)]+'_step_craft_'+(i%3+1)]*0.1
            }
            this.tableData.push(obj);
        }
      }
  },
  methods: {
      objectSpanMethod({ row, column, rowIndex, columnIndex }) {
        if (columnIndex === 0) {
          if (rowIndex % 3 === 0) {
            return {
              rowspan: 3,
              colspan: 1
            };
          } else {
            return {
              rowspan: 0,
              colspan: 0
            };
          }

  }}
  }
  
};
</script>
<style scoped>
.el-row {
  height:100%;
}
.el-col {
  height:100%;
  line-height: 50px;
  text-align: center;
}
.el-card {
  width: 200px;
  height: 100px;
  padding: 0px;
}
.center {
  display: flex;
  align-items: center;
  justify-content: center;
  height:100%;
}
</style>