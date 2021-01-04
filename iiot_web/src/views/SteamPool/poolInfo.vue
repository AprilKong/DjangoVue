<template>
  <div>
    <el-col :span="24" class= "header">
      <el-button type="text" icon="el-icon-back" @click="goBack"
        >返回</el-button
      >
    </el-col>
    <el-row>
      <el-col :span="6"><status-card title="运行状态" status="就绪" :icon="icon"/></el-col>
      <el-col :span="6"><status-card title="运行状态" status="就绪" :icon="icon"/></el-col>
      <el-col :span="6"><status-card title="运行状态" status="就绪" :icon="icon"/></el-col>
      <el-col :span="6"><status-card title="运行状态" status="就绪" :icon="icon"/></el-col>
    </el-row>
  </div>
</template>
<script>
import statusCard from '@/views/SteamPool/statusCard'
import StatusCard from './statusCard.vue';
export default {
  data(){
    return {
      icon:{icon:"el-icon-check",type:"warning"}
    }
  },
  components:{
    statusCard
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