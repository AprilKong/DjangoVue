import Vue from 'vue'
import Router from 'vue-router'
import {getToken} from '@/utils/storage'
import Home from '@/components/Home'
import Login from '@/views/login'
Vue.use(Router)

var routes = [
  {
    path: '/',
    name: 'Login',
    component: Login
  },
  {
    path: '/Home',
    name: 'Home',
    component: Home,
    meta: {
      requireAuth : true
    }
  }
];
const router = new Router({
  routes: routes
});

router.beforeEach((to, from, next) => {
  let token = getToken();
  if (!token){
      if(to.meta.requireAuth){
          next({
             path: '/'
          })
          Vue.prototype.$message.warning( '请先登录')
      }else {
         next(); 
      }
  }
  else{
    next();
  }
});

export default router
