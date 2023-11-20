import './App.css';
import React from 'react';


class App extends React.Component {
  constructor() {
    super()
    this.handleClick = this.handleClick.bind(this)
    this.state = {
      numeroClique: 0
    }
    console.log('Construiu o componente!')
  }

  handleClick() {
    this.setState((estadoAnterior, _props) => ({
      numeroClique: estadoAnterior.numeroClique + 1
    }))

    console.log(this)
    console.log('Clicou no botão!')
  }

  render() {
    return (
      console.log(this),
      <button onClick={this.handleClick}>{this.state.numeroClique}</button>
    );
  }
}

export default App
