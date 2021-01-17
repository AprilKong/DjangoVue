import request from '@/utils/request'

export function GetDeviceList(data) {
    return request({
        url: '/api/get_devices',
        method: 'get',
        data
    })
}

export function GetPoolInfo(poolId,data) {
    return request({
        url: '/api/get_poolinfo?q='+poolId,
        method: 'get',
        data
    })
}

export function GetSystemInfo(data) {
    return request({
        url: '/api/get_systeminfo?q=1',
        method: 'get',
        data
    })
}

export function GetAllSteamPool(deviceId,data) {
    return request({
        url: '/api/get_allpoolinfo',
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

export function GetSystemInfoHistory(data) {
    return request({
        url: '/api/get_systeminfohistory?q=7&d=1',
        method: 'get',
        data
    })
}

export function GetPoolInfoHistory(poolId,offSet=7,data) {
    return request({
        url: '/api/get_poolinfohistory?offSet='+offSet+'&poolId='+poolId,
        method: 'get',
        data
    })
}