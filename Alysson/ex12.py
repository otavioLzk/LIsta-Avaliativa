"""A Loja Mamão com Açúcar está vendendo seus produtos em 5 (cinco) prestações sem juros.
Faça um algoritmo que receba um valor de uma compra e mostre o valor das prestações."""

valor  =  float ( input ( 'Valor do produto: R$' ))
prestação  =  valor  /  5

print ( f'O valor de cada prestação será de R$ { ( prestação ) } .' )