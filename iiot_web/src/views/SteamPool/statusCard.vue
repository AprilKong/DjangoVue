<template>
    <el-card body-style="padding:0px;height:100%;width:100%">
        <el-row>
          <el-col :span="12" class="center">
              <el-button :type="icon.type" :icon="icon.icon"></el-button>
          </el-col>
          <el-col :span="12">
              <div style="display:block">{{title}}</div>
              <div><el-tag :type="icon.type">{{status}}</el-tag></div>
          </el-col>
        </el-row>
    </el-card>
</template>
<script>
export default {
  props:['title','status','icon'],
  data() {
    return {
    }
  },
  
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