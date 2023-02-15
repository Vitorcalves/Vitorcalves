package matematica;

public class OperacaoAritmetica {

    // atributos da classe OperacaoAritmetica
    protected float operadorUm;
    protected float operadorDois;

    // método construtor irá inicializar os atributos
    public OperacaoAritmetica(float v1, float v2) {
        this.operadorUm = v1;
        this.operadorDois = v2;
    }

    // métodos ou comportamentos da classe
    protected float some() {
        return this.operadorUm + this.operadorDois;
    }

    protected float subtraia() {
        return this.operadorUm - this.operadorDois;
    }

    protected float multiplique() {
        return this.operadorUm * this.operadorDois;
    }

    protected float divida() {
        return this.operadorUm / this.operadorDois;
    }
}
