import request from '@/utils/request'

export function GetDeviceList(data) {
    return request({
        url: '/api/get_devices',
        method: 'get',
        data
    })
}

export function GetPoolInfo(data) {
    return request({
        url: '/api/get_poolinfo',
        method: 'get',
        data
    })
}

export function GetSteamPool(data) {
    return request({
        url: '/api/get_pools',
        method: 'get',
        data
    })
}