/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package matematica;

import static java.lang.Float.parseFloat;

/**
 *
 * @author vitor
 */
public class Calculadora2 {
    
    public static void main(String[] args){
        float v1, v2, resultado = 0;
        
        String operacao;
        
        v1 = Float.parseFloat(
                JOtionPane.showInputDialog(null, "Informe um valor real")
        
        );
        v2 = Float.parseFloat(
            JOptionPane.showInputDialog(null,"informe outro valor real")
        );

        OperacaoAritmetica objeto = new OperacaoAritmetica(v1, v2);

        operacao = JOptionPane.showInputDialog(null, "Informe a operacao (+ - * /)");

        if (operacao.equals("+")){
            resultado = objeto.some();
        }

        if (operacao.equals("-")) {
            resultado = objeto.subtraia();           
        }
        if (operacao.equals("*")) {
            resultado = objeto.multiplique();            
        }
        if (operacao.equals("/")) {
            resultado = objeto.divida();
            
            JOptionPane.showMessageDialog(null, resultado);
        }


        



    }
    
}