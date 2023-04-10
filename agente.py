import random
import time
from os import system
from lixeira import *
from main import *

def react_simples(matriz):
    # Encontra a posição atual do robô
    posicao_lixo=(19,19)
    posicao_atual = None
    for i in range(20):
        for j in range(20):
            if matriz[i][j] =="A":
                posicao_atual = (i, j)
                break
                
    i,j=posicao_atual
    percept(i,j,matriz)
    i_novo,j_novo=direca(i,j)
    i+=i_novo
    j+=j_novo
    
    # Move o robô para a nova posição
    if(posicao_atual==posicao_lixo):
        matriz[posicao_atual[0]][posicao_atual[1]] = "X"
        matriz[i][j] = "A"
        return matriz
    if(matriz[i][j]=="R" or matriz[i][j]=="O"):  # Correção aqui
        if matriz[i][j]=='R':
            lixo='reciclável'
            print(f'levando lixo {lixo} para lixeira')
            matriz[i][j] = "_"
            levar_lixo(lixo,posicao_atual,matriz)
        elif matriz[i][j]=='O':
            lixo='orgânico'
            print(f'levando lixo {lixo} para lixeira')
            matriz[i][j] = "_"
            levar_lixo(lixo,posicao_atual,matriz)
        matriz[posicao_atual[0]][posicao_atual[1]] = "_"
        matriz[19][18] = "A"
    else:
        matriz[posicao_atual[0]][posicao_atual[1]] = "_"
        matriz[i][j] = "A"
        return matriz

def react_based_models(matriz):
    # Encontra a posição atual do robô
    #mantem historicos
    posicao_lixo=(19,19)
    posicao_atual = None
    for i in range(20):
        for j in range(20):
            if matriz[i][j] =="A":
                posicao_atual = (i, j)
                break
                
    i,j=posicao_atual
    percept(i,j,matriz)
    i_novo,j_novo=direca(i,j)
    i+=i_novo
    j+=j_novo
    
    # Move o robô para a nova posição
    if(posicao_atual==posicao_lixo):
        matriz[posicao_atual[0]][posicao_atual[1]] = "X"
        matriz[i][j] = "A"
        return matriz
    if(matriz[i][j]=="R" or matriz[i][j]=="O"):  # Correção aqui
        if matriz[i][j]=='R':
            lixo='reciclável'
            print(f'levando lixo {lixo} para lixeira')
            matriz[i][j] = "_"
            levar_lixo(lixo,posicao_atual,matriz)
        elif matriz[i][j]=='O':
            lixo='orgânico'
            print(f'levando lixo {lixo} para lixeira')
            matriz[i][j] = "_"
            levar_lixo(lixo,posicao_atual,matriz)
        matriz[posicao_atual[0]][posicao_atual[1]] = "_"
        matriz[19][18] = "A"
    else:
        matriz[posicao_atual[0]][posicao_atual[1]] = "_"
        matriz[i][j] = "A"
        return matriz

def based_goals(matriz):
    # Encontra a posição atual do robô
    #por objetivos
    posicao_lixo=(19,19)
    posicao_atual = None
    for i in range(20):
        for j in range(20):
            if matriz[i][j] =="A":
                posicao_atual = (i, j)
                break
                
    i,j=posicao_atual
    percept(i,j,matriz)
    i_novo,j_novo=direca(i,j)
    i+=i_novo
    j+=j_novo
    
    # Move o robô para a nova posição
    if(posicao_atual==posicao_lixo):
        matriz[posicao_atual[0]][posicao_atual[1]] = "X"
        matriz[i][j] = "A"
        return matriz
    if(matriz[i][j]=="R" or matriz[i][j]=="O"):  # Correção aqui
        if matriz[i][j]=='R':
            lixo='reciclável'
            print(f'levando lixo {lixo} para lixeira')
            matriz[i][j] = "_"
            levar_lixo(lixo,posicao_atual,matriz)
        elif matriz[i][j]=='O':
            lixo='orgânico'
            print(f'levando lixo {lixo} para lixeira')
            matriz[i][j] = "_"
            levar_lixo(lixo,posicao_atual,matriz)
        matriz[posicao_atual[0]][posicao_atual[1]] = "_"
        matriz[19][18] = "A"
    else:
        matriz[posicao_atual[0]][posicao_atual[1]] = "_"
        matriz[i][j] = "A"
        return matriz

def based_utility(matriz):
    #baseado em utilidades tem felicidade, ou seja, ele liga para pontuação 
    # Encontra a posição atual do robô
    posicao_lixo=(19,19)
    posicao_atual = None
    for i in range(20):
        for j in range(20):
            if matriz[i][j] =="A":
                posicao_atual = (i, j)
                break
                
    i,j=posicao_atual
    percept(i,j,matriz)
    i_novo,j_novo=direca(i,j)
    i+=i_novo
    j+=j_novo
    
    # Move o robô para a nova posição
    if(posicao_atual==posicao_lixo):
        matriz[posicao_atual[0]][posicao_atual[1]] = "X"
        matriz[i][j] = "A"
        return matriz
    if(matriz[i][j]=="R" or matriz[i][j]=="O"):  # Correção aqui
        if matriz[i][j]=='R':
            lixo='reciclável'
            print(f'levando lixo {lixo} para lixeira')
            matriz[i][j] = "_"
            levar_lixo(lixo,posicao_atual,matriz)
        elif matriz[i][j]=='O':
            lixo='orgânico'
            print(f'levando lixo {lixo} para lixeira')
            matriz[i][j] = "_"
            levar_lixo(lixo,posicao_atual,matriz)
        matriz[posicao_atual[0]][posicao_atual[1]] = "_"
        matriz[19][18] = "A"
    else:
        matriz[posicao_atual[0]][posicao_atual[1]] = "_"
        matriz[i][j] = "A"
        return matriz

    
def percept(x, y, matriz):
# Lista para armazenar as percepções do robô
    percepcoes = []

    # Verifica as 8 células ao redor do robô
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            # Verifica se a célula está dentro dos limites da matriz
            if 0 <= i < 20 and 0 <= j < 20:
                # Verifica se há lixo na célula
                if matriz[i][j] in ['R', 'O']:
                    # Adiciona a percepção à lista
                    percepcoes.append(matriz[i][j])

    return percepcoes

def direca(x, y):
    # Verifica as direções possíveis, levando em consideração a posição do robô na matriz
    possiveis_direcoes = []
    #percept()
    if x > 0:  # pode mover para cima
        possiveis_direcoes.append((-1, 0))
    if x < 19:  # pode mover para baixo
        possiveis_direcoes.append((1, 0))
    if y > 0:  # pode mover para a esquerda
        possiveis_direcoes.append((0, -1))
    if y < 19:  # pode mover para a direita
        possiveis_direcoes.append((0, 1))

    # Se não há direções possíveis, retorna (0,0)
    if len(possiveis_direcoes) == 0:
        return (0, 0)
    
    # Escolhe uma direção aleatória dentre as possíveis
    direcao = random.choice(possiveis_direcoes)
    return direcao


def levar_lixo(tipo_lixo, posicao_atual, matriz):
    
    # Observe a posição atual e vá até a posição (19, 19) da matriz
    pos_x_atual, pos_y_atual = posicao_atual
    pos_x_lixo, pos_y_lixo = 19, 19  # Posição do lixo (19, 19) da matriz
    tamanho_matriz = len(matriz)

    while pos_x_atual != pos_x_lixo or pos_y_atual != pos_y_lixo:
        # Move o robô na direção x se ainda não estiver na posição correta
        if pos_x_atual != pos_x_lixo:
            if pos_x_atual < pos_x_lixo:
                pos_x_proximo = min(pos_x_atual + 1, tamanho_matriz - 1)  # Verifica limite superior da matriz
                if matriz[pos_x_proximo][pos_y_atual] != "R" and matriz[pos_x_proximo][pos_y_atual] != "O":
                    pos_x_atual = pos_x_proximo
            else:
                pos_x_proximo = max(pos_x_atual - 1, 0)  # Verifica limite inferior da matriz
                if matriz[pos_x_proximo][pos_y_atual] != "R" and matriz[pos_x_proximo][pos_y_atual] != "O":
                    pos_x_atual = pos_x_proximo
        
        # Move o robô na direção y se ainda não estiver na posição correta
        if pos_y_atual != pos_y_lixo:
            if pos_y_atual < pos_y_lixo:
                pos_y_proximo = min(pos_y_atual + 1, tamanho_matriz - 1)  # Verifica limite superior da matriz
                if matriz[pos_x_atual][pos_y_proximo] != "R" and matriz[pos_x_atual][pos_y_proximo] != "O":
                    pos_y_atual = pos_y_proximo
            else:
                pos_y_proximo = max(pos_y_atual - 1, 0)  # Verifica limite inferior da matriz
                if matriz[pos_x_atual][pos_y_proximo] != "R" and matriz[pos_x_atual][pos_y_proximo] != "O":
                    pos_y_atual = pos_y_proximo

        # Atualiza a matriz com a nova posição do robô
        matriz[posicao_atual[0]][posicao_atual[1]] = "_"  # Limpa a posição anterior do robô
        matriz[pos_x_atual][pos_y_atual] = "A"  # Marca a nova posição do robô

        # Imprime a matriz atualizada na tela
        for i in range(tamanho_matriz):
            for j in range(tamanho_matriz):
                print(matriz[i][j], end=" ")
            print()
        print("")
        print(f'levando lixo {tipo_lixo.upper()} para lixeira')
        
        print()
        point=pontuacao()
        print(f'pontuação: {point}') 
        
        time.sleep(0.1)
        system("cls")

        # Atualiza a posição atual do robô
        posicao_atual = (pos_x_atual, pos_y_atual)

    # Após chegar à posição (19, 19) da matriz, chama a função receber_lixo
    receber_lixo(tipo_lixo)
    
    matriz[pos_x_atual][pos_y_atual] = "X"  # Marca a posição atual do robô com outro lixo

    return matriz
