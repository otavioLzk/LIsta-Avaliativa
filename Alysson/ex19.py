"""A lanchonete Gostosura vende apenas um tipo de sanduíche, cujo recheio inclui duas fatias de queijo, uma
fatia de presunto e uma rodela de hambúrguer. Sabendo que cada fatia de queijo ou presunto pesa 50 gramas, e
que a rodela de hambúrguer pesa 100 gramas, faz um algoritmo em que o dono dá a quantidade de sanduíches
a fazer, e a máquina informe as quantidades (em quilos) de queijo, presunto e carne necessária para compra"""

sanduíches  =  int ( input ( 'Informe a quantidade de sanduíches a serem feitos: ' ))
queijo  = ( 2  *  sanduíches ) *  0,05
presunto  =  sanduíches  *  0,05
hambúrguer  =  sanduíches  *  0,1

print ( f'Serão necessários: \n { queijo } Kgs de Queijo \n { presunto } Kgs de Presunto \n { hambúrguer } Kgs de hambúrguer.' )