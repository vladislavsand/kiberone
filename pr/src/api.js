import './config'
import axios from 'axios'

export async function GetClients(){
    const url = `${global.config.host}/clients/`
    return axios.get(url).then(response => {
        return response.data
    }).catch( error => {
        return null
    })
}