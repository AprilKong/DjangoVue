import request from '@/utils/request'

export function GetDeviceList(data) {
    return request({
        url: '/api/get_poolinfo',
        method: 'get',
        data
    })
}