package matematica;

import javax.swing.JOptionPane;

public class Calculadora1 {

    // implementação do método principal que no Java torna a classe executável
    public static void main(String[] args) {
        // cria um objeto da clsse OperacaoAritmetica
        OperacaoAritmetica objeto1 = new OperacaoAritmetica(32, 74);

        JOptionPane.showMessageDialog(null, objeto1.some());
    }
}