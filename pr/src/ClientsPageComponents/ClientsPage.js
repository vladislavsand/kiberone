import React, {Component} from 'react'
import { GetClients } from '../api'


export class ClientsPageComponent extends Component {
    constructor() {
        super()
        this.state = {
            clients: ['1', '2', '3']
        }
    }

    componentDidMount() {
        GetClients().then(res => {
            console.log(res)
            this.setState({clients: res})
        })
    }

    render() {
        return(
            <div>
                {this.state.clients.map(c => (
                    <p key={c.id}>{c.full_name}</p>
                ))}
            </div>
        )
    }
}