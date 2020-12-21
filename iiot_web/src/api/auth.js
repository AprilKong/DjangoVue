import request from '@/utils/request'

export function Signin(data) {
    return request({
        url: '/api/login/',
        method: 'post',
        data
    })
}