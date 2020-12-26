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
    logOut (state) {
        state.token = '';
        state.isAuthed = false;
        removeToken();
        router.push({path:'/'});
    },
    setUserInfo(state, userInfo) {
        state.userInfo = userInfo;
        state.isAuthed = true;
    }
};

const actions = {
    async login({commit, state},credential) {
        if(state.isAuthed)
            {router.push({name: 'Index'}); return;}
        var response = await Signin(credential);
        console.log(response.data.token);
        commit('setToken',response.data.token);
        commit('setUserInfo',response.data.token); //TODO: should return userInfo in API
        router.push({ name: 'Index' });
    },
    async getUserInfo({commit}, token) {
        commit('setUserInfo',token);
        return {token:token,
            status: 200}
    }
}

export default {
    namespaced: true,
    state,
    mutations,
    actions
}