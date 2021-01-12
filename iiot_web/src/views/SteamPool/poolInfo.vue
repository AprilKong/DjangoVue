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
      <el-col align="center" :span="6">
        <status-card :title="caledPoolStatus.caledTempStatus.title" :status="caledPoolStatus.caledTempStatus.val" :icon="caledPoolStatus.caledTempStatus.icon"/>
      </el-col>
      <el-col align="center" :span="6">
        <status-card :title="caledPoolStatus.caledScheduleStatus.title" :status="caledPoolStatus.caledScheduleStatus.val" :icon="caledPoolStatus.caledScheduleStatus.icon"/>
      </el-col>
      <el-col align="center" :span="6">
        <status-card :title="caledPoolStatus.caledSensorStatus.title" :status="caledPoolStatus.caledSensorStatus.val" :icon="caledPoolStatus.caledSensorStatus.icon"/>
      </el-col>
    </el-row>
    <el-row>
      <el-col align="center" :span="6">
        <status-card title="当前温度" :status="caledPoolStatus.caledTemp+' ℃'" :icon="{icon:'el-icon-odometer',type:'primary'}"/>
      </el-col>
      <el-col align="center" :span="6">
        <status-card title="保温时间" :status="caledPoolStatus.caledTempHoldTime+ ' min'" :icon="{icon:'el-icon-time',type:'primary'}"/>
      </el-col>
      <el-col align="center" :span="6">
        <status-card title="预计完成时间" :status="caledPoolStatus.caledETA+' min'" :icon="{icon:'el-icon-alarm-clock',type:'primary'}"/>
      </el-col>
      <el-col align="center" :span="6">
        <status-card title="当前工艺" :status="caledPoolStatus.caledCurrentCraft" :icon="{icon:'el-icon-truck',type:'primary'}"/>
      </el-col>
    </el-row>
    <el-divider><i class="el-icon-star-on"></i></el-divider>
    <system-info/>
    <craft-table/>
  </div>
</template>
<script>
import StatusCard from './statusCard.vue';
import SystemInfo from './systeminfo.vue';
import CraftTable from './craftTable.vue';
import {GetPoolInfo} from '@/api/device';
import Systeminfo from './systeminfo.vue';
export default {
  data(){
    return {
      icon:{icon:"el-icon-check",type:"warning"},
      poolStatus:null,
      caledPoolStatus: {
        caledRunStatus:{},
        caledTempStatus:{},
        caledScheduleStatus:{},
        caledSensorStatus:{},
        caledTemp:null,
        caledTempHoldTime:null,
        caledETA:null,
        caledCurrentCraft:null
      }
    }
  },
  async mounted() {
      var response = await GetPoolInfo(this.$route.params.pool.id);
      if(response.status === 200)
        {
          this.poolStatus = response.data;
          var runVal = this.poolStatus.auto_run == 1? "正在运行": this.poolStatus.complete == 1? "已完成" : "就绪";
          var tempVal = this.poolStatus.temp_hold == 1? "升温": "保温";
          var scheduleVal = this.poolStatus.enable_schedule == 1? "已预约":"未预约";
          var alarmVal = this.poolStatus.sensor_alarm == 1? "传感器异常":"正常";
          this.caledPoolStatus.caledRunStatus = {val: runVal ,title: "运行状态", icon:{
            type:this.poolStatus.auto_run == 1? "success":"warning", icon:this.poolStatus.auto_run == 1?"el-icon-check":"el-icon-close"
          }};
          this.caledPoolStatus.caledTempStatus = {val: tempVal, title:"保温状态",icon:{
            type:this.poolStatus.temp_hold == 1? "success":"warning", icon:this.poolStatus.temp_hold == 1?"el-icon-top":"el-icon-minus"
          }};
          this.caledPoolStatus.caledScheduleStatus = {val: scheduleVal, title: "预约状态",icon:{
            type:this.poolStatus.enable_schedule == 1? "success":"warning", icon:this.poolStatus.enable_schedule == 1?"el-icon-alarm-clock":"el-icon-close"
          }};
          this.caledPoolStatus.caledSensorStatus = {val: alarmVal,title: "报警信息",icon:{
            type:this.poolStatus.sensor_alarm == 0? "success":"warning", icon:this.poolStatus.sensor_alarm == 0?"el-icon-check":"el-icon-bell"
          }};
          this.caledPoolStatus.caledTemp = this.poolStatus.temp*0.1; // 0.1 ℃
          this.caledPoolStatus.caledTempHoldTime = this.poolStatus.temp_time_count; // 1 min
          this.caledPoolStatus.caledETA = this.poolStatus.target_time;
          this.caledPoolStatus.caledCurrentCraft = this.poolStatus.craft_selection;

        }
      console.log(response)
  },
  components:{
    StatusCard,
    SystemInfo,
    CraftTable
  },
  methods: {
    goBack() {
      this.$router.push({ name: "DeviceDetails" });
    },
    
  }
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
.el-row {
    margin-bottom: 20px;
    &:last-child {
      margin-bottom: 0;
    }
  }

</style>