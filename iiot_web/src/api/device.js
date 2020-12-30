import request from '@/utils/request'

export function GetDeviceList(data) {
    return request({
        url: '/api/get_devices',
        method: 'get',
        data
    })
}