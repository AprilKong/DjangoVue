<template>
  <el-menu
    :default-active="this.$route.path"
    class="el-menu-vertical-demo"
    @open="handleOpen"
    @close="handleClose"
    background-color="#F2F6FC"
    text-color="#303133"
    active-text-color="#E6A23C"
    router
  >
    <el-menu-item v-for="(item, i) in navList" :key="i" :index="item.name">
      <template slot="title">
        <i :class="item.icon"></i>
        <span> {{ item.navItem }}</span>
      </template>
    </el-menu-item>
  </el-menu>
</template>
<script>
  export default {
    data() { 
        return { 
            navList:[ 
            {name:'/views/deviceManage',navItem:'设备管理',icon:'el-icon-s-tools'}, 
            {name:'/views/deviceDetails',navItem:'设备详情',icon:'el-icon-info'},
            {name:'/views/alarm',navItem:'报警中心',icon:'el-icon-message-solid'}, 
            ] } 
    },
    methods: {
      handleOpen(key, keyPath) {
        console.log(key, keyPath);
      },
      handleClose(key, keyPath) {
        console.log(key, keyPath);
      }
    }
  }
</script>
<style>
  .el-menu {
  height: 100%;
  border-right: solid 0px #e6e6e6;
}
</style>