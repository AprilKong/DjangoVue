import {getToken, setToken, removeToken} from '@/utils/storage'
import {Signin} from '@/api/auth'
import router from '@/router'
const state = {
    token: getToken(),
    isAuthed: false,
    userInfo: {}
};

const mutations = {
    setToken (state,token) {
        state.token = token;
        setToken(token);
    },
    clearToken (state) {
        state.token = '';
        state.isAuthed = false;
        removeToken();
    },
    setUserInfo(state, userInfo) {
        state.userInfo = userInfo;
        state.isAuthed = true;
    }
};

const actions = {
    async login({commit, state},credential) {
        if(state.isAuthed)
            {router.push({name: 'Home'}); return;}
        var response = await Signin(credential);
        console.log(response.data.token);
        commit('setToken',response.data.token);
        commit('setUserInfo',response.data.token); //TODO: should return userInfo in API
        router.push({ name: 'Home' });
    },
    async getUserInfo({commit}, token) {
        setTimeout(()=>{return token;},1000); // should call api to get userinfo
    }
}

export default {
    namespaced: true,
    state,
    mutations,
    actions
}