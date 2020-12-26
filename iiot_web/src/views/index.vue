<template>
  <el-container>
    <el-header>
      <Header />
    </el-header>
    <el-container>
      <el-aside width="220px">
        <Aside />
      </el-aside>
      <el-main>
        <router-view />
      </el-main>
    </el-container>
  </el-container>
</template>
<script>
import Aside from "@/components/layout/aside";
import Header from "@/components/layout/header";
export default {
  data() {
    return {};
  },
  mounted() {
      if(this.$route.fullPath != '/views/deviceDetails')
        this.$router.push({ path: "/views/deviceDetails" }); //自动切换到设备详情页面
  },
  methods: {},
  components: {
    Aside,
    Header,
  },
};
</script>
<style>
.el-header,
.el-footer {
  background-color: #f2f6fc;
  color: rgb(60, 143, 206);
  text-align: left;
  line-height: 60px;
  border-bottom: solid 0px #e6e6e6;
}
.el-aside {
  text-align: left;
  height: 100%;
}
.el-main {
  text-align: center;
  line-height: 100px;
  padding: 10px;
}
</style>
