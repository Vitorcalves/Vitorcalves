<?php

function formataValor($valor, $decimais = 2)
{
    return number_format($valor, $decimais, ",", ".");
}

function strNumero($valor)
{
    return str_replace(",", ".", str_replace(".", "", $valor));
}