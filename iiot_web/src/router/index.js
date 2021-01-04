import Vue from 'vue'
import Router from 'vue-router'
import {getToken} from '@/utils/storage'
import Home from '@/components/Home'
import Index from '@/views/index'
import Login from '@/views/login'
import Alarm from '@/views/alarm'
import DeviceManage from '@/views/deviceManagement'
import DeviceDetails from '@/views/deviceDetails'
import PoolInfo from '@/views/SteamPool/PoolInfo'
import store from '@/store'
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
  },
  {
    path: '/Index',
    name: 'Index',
    component: Index,
    meta: {
      requireAuth : true
    },
    children: [
      {
        path: '/views/deviceManage',
        name: 'DeviceManage',
        component: DeviceManage
      },
      {
        path: '/views/alarm',
        name: 'Alarm',
        component: Alarm
      },
      {
        path: '/views/deviceDetails',
        name: 'DeviceDetails',
        component: DeviceDetails
      },
      {
        path: '/views/deviceDetails/poolInfo',
        name: 'PoolInfo',
        component: PoolInfo
      }
    ]
  }
];
const router = new Router({
  routes: routes
});

router.beforeEach(async (to, from, next) => {
  if(to.matched.some(t=>t.meta.requireAuth)){
    if(!store.state.user.isAuthed) // check if isAuthed which means already logged in
    {
        if(store.state.user.token){ //not authed but has token
            try {
              const data = await store.dispatch('user/getUserInfo',store.state.user.token);
              if(data.status === 200) {
                next();
              }
              else {
                Vue.prototype.$message.warning('请先登录');
                store.commit('user/clearToken');
                next({path: '/'});
              }
            }
            catch (error) {
              Vue.prototype.$message.warning('请先登录');
              store.commit('user/clearToken');
              next({path: '/'});

            }
        }
        else {
            Vue.prototype.$message.warning('请先登录');
            next({path: '/'});
        }
    }
    else {
      next();
    }
  }
  else {
    next();
  }
});

export default router
