<template>
<el-row>
  <el-col :span="4" v-for="(pool, index) in poolStatus" :key="index" :offset="index%4 > 0 ? 2 : 0" style="margin-bottom:40px">
    <el-card :body-style="{ padding: '0px' }">
      <div>
        <el-button type="success" icon="el-icon-check" circle></el-button>
      </div>
      <div style="padding: 4px;">
        <span>{{pool.steampool_id}}</span>
        <div>
          <time class="time">{{ pool.collect_time }}</time>
          <el-button type="text" class="button">查看详情</el-button>
        </div>
      </div>
    </el-card>
  </el-col>
</el-row>
</template>
<script>
import {GetDeviceList} from '@/api/device'
  export default {
    data() {
      return {
        poolStatus: []
      }
    },
    async mounted() {
      var response = await GetDeviceList();
      if(response.status === 200)
        this.poolStatus = response.data;
      console.log(response)
    },
    methods: {
      handleEdit(index, row) {
        console.log(index, row);
      },
      handleDelete(index, row) {
        console.log(index, row);
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
  line-height: 50px;
}
.el-button{
  padding:10px;
  margin-top: 10px;
}
</style>
