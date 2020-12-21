import request from '@/utils/request'

export function Signin(data) {
    return request({
        url: '/login/',
        method: 'post',
        data
    })
}