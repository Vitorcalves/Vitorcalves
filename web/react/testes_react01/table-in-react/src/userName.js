import React, { Component } from 'react'
import './userName.css'

class userName extends Component {
    render() {
        const name = this.props.name

        return <span className='name'>{name}</span>
    }
}

export default userName