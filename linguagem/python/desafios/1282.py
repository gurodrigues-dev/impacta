def cc(qtd_de_canais):

    listas = []

    for _ in range(qtd_de_canais):
        nome, inscritos, monetizacao, premium = input().split(';')
        inscritos = int(inscritos)
        monetizacao = float(monetizacao)
        premium = premium == 'sim'
        
        listas.append([nome,inscritos,monetizacao,premium])
        
    return listas

def bonificacao(listas,fpremium, fnpremium):
    bonus = []
    for lista in listas:
        valor = lista[2]
        
        if lista[3]:
            valor += lista[1] // 1000 * fpremium
        else:
            valor += lista[1] // 1000 * fnpremium
        bonus.append([lista[0],valor])
    return bonus

def mostrar(bonus):
    print(5*'-')
    print('BÔNUS')
    print(5*'-')
    for registro in bonus:
        print(f'{registro[0]}: R$ {registro[1]:.2f}')
        
qtd_de_canais = int(input())
listas = cc(qtd_de_canais)
fpremium = float(input())
fnpremium = float(input())
bonus = bonificacao(listas, fpremium, fnpremium)
mostrar(bonus)