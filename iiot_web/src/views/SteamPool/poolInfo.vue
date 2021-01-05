<template>
  <div>
    <el-row>
    <el-col :span="24" class= "header">
      <el-button type="text" icon="el-icon-back" @click="goBack">返回</el-button>
    </el-col>
    </el-row>
    <el-row>
      <el-col align="center" :span="6">
        <status-card :title="caledPoolStatus.caledRunStatus.title" :status="caledPoolStatus.caledRunStatus.val" :icon="caledPoolStatus.caledRunStatus.icon"/>
      </el-col>
    </el-row>
  </div>
</template>
<script>
import StatusCard from './statusCard.vue';
import {GetPoolInfo} from '@/api/device'
export default {
  data(){
    return {
      icon:{icon:"el-icon-check",type:"warning"},
      poolStatus:null,
      caledPoolStatus: {
        caledRunStatus:{},
        caledTempStatus:{},
        caledScheduleStatus:{},
        caledSensorStatus:{}
      }
    }
  },
  async mounted() {
      var response = await GetPoolInfo();
      if(response.status === 200)
        {
          this.poolStatus = response.data;
          var runVal = this.poolStatus.auto_run == 1? "正在运行": this.poolStatus.complete == 1? "已完成" : "就绪";
          var tempVal = this.poolStatus.temp_hold == 0? "升温": "保温";
          var scheduleVal = this.poolStatus.enable_schedule == 1? "已预约":"未预约";
          var alarmVal = this.poolStatus.sensor_alarm == 1? "传感器异常":"正常";
          this.caledPoolStatus.caledRunStatus = {val: runVal ,title: "运行状态", icon:{
            type:this.auto_run == 1? "success":"warning", icon:this.auto_run == 1?"el-icon-check":"el-icon-close"
          }};
          this.caledPoolStatus.caledTempStatus = {val: tempVal, title:"保温状态"};
          this.caledPoolStatus.caledScheduleStatus = {val: scheduleVal, title: "预约状态"};
          this.caledPoolStatus.caledSensorStatus = {val: alarmVal,title: "报警信息"};
        }
      console.log(response)
  },
  components:{
    StatusCard
  },
  methods: {
    goBack() {
      this.$router.push({ name: "DeviceDetails" });
    },
  },
};
</script>
<style scoped>
.el-col {
    align-content: center;
}
.header {
    text-align: left;
    line-height: 50px;
}

</style>