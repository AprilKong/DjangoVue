<template>
  <div>
    <el-row>
      <el-col align="center" :span="6">
        <status-card title="蒸汽压强" :status="caledSystemStatus.caledSteamPressure+' Pa'" :icon="{icon:'el-icon-odometer',type:'primary'}"/>
      </el-col>
      <el-col align="center" :span="6">
        <status-card title="压缩空气压强" :status="caledSystemStatus.caledAirPressure+ ' Pa'" :icon="{icon:'el-icon-time',type:'primary'}"/>
      </el-col>
    </el-row>
    <el-divider>历史记录</el-divider>
    <el-row>
      <el-col align="center" :span="12">
        <chart v-if="chartDataLoaded" :data="chartData" :styles="myStyles"/>
      </el-col>
      <el-col align="center" :span="12">
        <chart v-if="chartDataLoaded" :data="chartData" :styles="myStyles"/>
      </el-col>
    </el-row>
    <el-divider><i class="el-icon-star-on"></i></el-divider>
  </div>
</template>
<script>
import StatusCard from './statusCard.vue';
import Chart from './chart.vue';
import {GetSystemInfo,GetSystemInfoHistory} from '@/api/device'
export default {
  data(){
    return {
      systemStatus:null,
      chartDataLoaded: false,
      caledSystemStatus: {
        caledSteamPressure:null,
        caledAirPressure:null,
      },
      chartData:{
      labels: [],
      datasets: [{
          label: "蒸汽压强",
          borderColor: "#FC2525",
          pointBackgroundColor: "white",
          borderWidth: 1,
          pointBorderColor: "white",
          backgroundColor: this.gradient,
          data: []
      }, {
          label: "压缩空气压强",
          borderColor: "#05CBE1",
          pointBackgroundColor: "white",
          pointBorderColor: "white",
          borderWidth: 1,
          backgroundColor: this.gradient2,
          data: []
      }]
      }
    }
  },
  async mounted() {
      this.chartDataLoaded = false;
      var response = await GetSystemInfo(this.$route.params.pool.id);
      if(response.status === 200)
        {
          this.systemStatus = response.data;
          this.caledSystemStatus.caledSteamPressure = this.systemStatus.steam_pressure * 0.01;
          this.caledSystemStatus.caledAirPressure = this.systemStatus.air_pressure * 0.01;

        }
      var res = await GetSystemInfoHistory();
      if(res.status === 200)
      {
          res.data.forEach(element => {
              this.chartData.labels.push(element.collect_time);
              this.chartData.datasets[0].data.push(element.steam_pressure * 0.01);
              this.chartData.datasets[1].data.push(element.air_pressure * 0.01);
          });
          this.chartDataLoaded = true;
      }
      console.log(res);
      console.log(this.chartData);
  },
  components:{
    StatusCard,
    Chart
  },
  methods: {
    goBack() {
      this.$router.push({ name: "DeviceDetails" });
    },
  },
  computed: {
    myStyles () {
      return {
        height: '500px',
        weight: '500px',
        position: 'relative'
      }
    }
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