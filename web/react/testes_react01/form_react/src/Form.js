import React from "react";
import "./Form.css";

class Form extends React.Component {
    constructor() {
        super()
        this.state = {
            estadoFavorito: '',
            nome: '',
            email: '',
            idade: 0,
            vaiComparecer: false,
            palavraChaveFavorita: ''
        }
    }

    handleTextChange(event){
        console.log(event.target.value)
    }
            
    render() {
        return (
            <div>
                <h1>Estados e React: ferramenta incrivel ou reagindo a regionalismo</h1>
                <form className="form">

                    <label>
                        Diga qual o seu estado favorito! De React ou do Brasil, você decide! =)
                        <textarea name="estadoFavorito" onChange={this.handleTextChange} />
                    </label>

                    <label>
                        Email
                        <input name="email" type="email" />
                    </label>

                    <label>
                        Nome
                        <input name="nome" type="text" />
                    </label>
                </form>

                <label>
                    Idade
                    <input name="idade" type="number" />
                </label>

                <label>
                    Vai comparecer a conferencia?
                    <input name="vaiComparecer" type="checkbox" />
                </label>

                <label>
                    Escolha sua palavra chave favorita:
                    <select name="palavraChaveFavorita">
                        <option value="estado">Estado</option>
                        <option value="evento">Evento</option>
                        <option value="props">Props</option>
                        <option value="hooks">Hooks</option>
                    </select>
                </label>
                
            </div>
        );
    }
}

export default Form;
