import React, { Component } from 'react'
class userOtherInfo extends Component {
    render() {
        const email = this.props.email
        const id = this.props.id

        return <span>{email}{id}</span>
    }
}

export default userOtherInfo