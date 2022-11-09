listaDeDias = ['domingo', 'segunda', 'terca', 'quarta', 'quinta', 'sexta', 'sabado']

def verificaDiaEntrada(entrada, lista):
    
    if entrada in lista:
        return True
    else:
        return False

def verificaQuantDeDias(dias):
    
    if dias > 6 or dias < 0:
        return False
    else:
        return True 

ds = False

while(not ds):
    de = input('')
    ds = verificaDiaEntrada(de, listaDeDias)
    
prazoDeEspera = False

while(not prazoDeEspera):
    quantDias = int(input(''))
    prazoDeEspera = verificaQuantDeDias(quantDias)
    

if quantDias == 0:
    print('chega hoje!')
else:
    indexDoDiaSemana = listaDeDias.index(de)
    novaLista = listaDeDias[indexDoDiaSemana + 1:len(listaDeDias)] + listaDeDias[0:indexDoDiaSemana]

    diaEntrega = novaLista[quantDias - 1]

    print(f'sera entregue {diaEntrega}')