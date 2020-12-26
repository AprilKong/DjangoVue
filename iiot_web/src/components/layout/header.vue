<template>
  <el-row>
    <el-col :span="2"
      ><div>
        <img src="@/assets/images/logo_2.png" width="150" height="60" /></div
    ></el-col>
    <el-col :span="2" :offset="20">
      <el-dropdown trigger="click">
        <el-avatar
          icon="el-icon-user-solid"
          size="medium"
          style="margin-top: 10px"
        ></el-avatar>
        <el-dropdown-menu slot="dropdown">
          <el-dropdown-item @click.native="logOut">退出</el-dropdown-item>
          <el-dropdown-item>关于</el-dropdown-item>
        </el-dropdown-menu>
      </el-dropdown>
    </el-col>
  </el-row>
</template>
<script>
export default {
    methods: {
        logOut(){
            console.log('user log out');
            this.$store.commit('user/logOut');
        }
    }
}
</script>
<style scoped>
  .el-dropdown {
    font-size: 20px;
    color:rgb(60,143,206);
    text-align: center;
  }
  .el-avatar {
    background:rgb(60,143,206);
  }
</style>