<template>
<el-row>
  <el-col :span="4" v-for="(pool, index) in poolStatus" :key="index" :offset="index%4 > 0 ? 2 : 0" style="margin-bottom:40px">
    <el-card :body-style="{ padding: '0px' }">
      <div>
        <el-button :type="getButtonType(pool)" :icon="getButtonIcon(pool)" circle></el-button>
      </div>
      <div style="padding: 4px;">
        <span>编号：{{pool.id}}</span>
        <div>
          <div><el-tag :type="pool.status == 'A'?'':'warning'">{{ pool.status == 'A'?'正在运行':'离线' }}</el-tag></div>
          <el-button type="text" class="button" @click="goToDetails(pool)">查看详情</el-button>
        </div>
      </div>
    </el-card>
  </el-col>
</el-row>
</template>
<script>
import {GetSteamPool} from '@/api/device'
  export default {
    data() {
      return {
        poolStatus: []
      }
    },
    async mounted() {
      var response = await GetSteamPool();
      if(response.status === 200)
        this.poolStatus = response.data;
      console.log(response)
    },
    methods: {
      getButtonType(pool) {
        return pool.status == 'O'?"danger":"success"
      },
      getButtonIcon(pool) {
        return pool.status == 'O'?"el-icon-close":"el-icon-check"
      },
      goToDetails(pool){
        this.$router.push({name:'PoolInfo',params:{
          pool:pool
    }})
      }

    }
  }
</script>
<style scoped>
.el-avatar {
    background:rgb(60,143,206);
  }
.el-card {
  height: 200px;
  width: 200px;
  line-height: 45px;
}
.el-button{
  margin-top: 10px;
}
/* .button {
  margin-bottom: 14px;
} */
</style>
