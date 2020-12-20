import  axios from 'axios'
import {getToken} from '@/utils/storage'
import {Message} from 'element-ui'

//创建axios实例
const service = axios.create({
    headers: {'token': getToken()},
    baseURL: '', //api的base_url
    withCredentials: true, // send cookies when cross-domain requests
    timeout:50000, //请求超时时间
    validateStatus(status) {
        switch (status) {
        case 400:
            Message.error('请求出错')
            break
        case 401:
            Message.warning({
                message: '授权失败，请重新登录'
            })
            break
        case 403:
            Message.warning({
                message: '拒绝访问'
            })
            break
        case 404:
            Message.warning({
                message: '请求错误,未找到该资源'
            })
            break
        case 500:
            Message.warning({
                message: '服务端错误'
            })
            break
        }
        return status >= 200 && status < 300
    }
});

// service.headers = {
//     'Content-Type': 'application/json;charset=UTF-8'
// };
// service.defaults.headers.post['Content-Type'] = 'application/json;charset=UTF-8';

//http请求拦截器
service.interceptors.request.use(
    config=>{
        if(getToken()){
            config.headers['token'] = getToken();
            config.headers['Content-Type'] = 'application/json; charset=UTF-8';
            config.headers.Authorization = getToken();
        }
        return  config;
    },error => {
        Message.error({
            message:'加载超时',
        });
        return Promise.reject(error)
    });

//http响应拦截器
service.interceptors.response.use(
    response => {
        //拦截响应，做统一处理
        if (response.data.code) {
            switch (response.data.code) {

            }
        }
        return response
    },
    //接口错误状态处理，也就是说无响应时的处理
    error => {
        if(error.response === undefined)
            return Promise.reject(500);//timeout
        const responseCode = error.response.status;
        switch(responseCode){
            // 登录失败
            case 401:
                Message.error({
                    message:'登录失败',
                });
            break;
            // 网络请求不存在
            case 404:
                Message.error({
                    message:'网络请求不存在',
                });
            break;
            default:
                Message.error({
                    message:'网络请求不存在',
                });
            break;
        }
        return Promise.reject(error.response.status) // 返回接口返回的错误信息
    })

export default service

