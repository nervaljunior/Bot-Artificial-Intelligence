import random
import time
from os import system
from lixeira import *
from main import *

def react_simples(matriz):
    #aqui falta fazer a percepção do entorno que ta com bug
    #a primeira coisa que ele tem que fazer é verificaar se tem alguem no entorno
    # Encontra a posição atual do robô
    posicao_lixo=(19,19)
    posicao_atual = None
    for i in range(20):
        for j in range(20):
            if matriz[i][j] =="A":
                #pegar o lixo que ta ao redor 
                '''posicao_atual=percept(i,j,matriz)
                if posicao_atual==None:'''
                posicao_atual = (i, j)
                break
                
    i,j=posicao_atual  
    #começa andar aleatoriaente
    i_novo,j_novo=aleatorio(i,j)
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

def aleatorio(x, y):
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

def percept(x, y, matriz):
    # Verifica as 8 células ao redor do robô
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            # Verifica se a célula está dentro dos limites da matriz
            if 0 <= i < 20 and 0 <= j < 20:
                # Verifica se há lixo na célula
                if matriz[i][j] =='R':
                    lixo = 'reciclável'
                    
                    # Calcula o deslocamento da matriz necessário para chegar à célula com lixo
                    deslocamento_i = i - x
                    deslocamento_j = j - y

                # Função para fazer o movimento do robô de acordo com o deslocamento necessário
                    if deslocamento_i < 0:
                        # Movimento para cima
                        matriz[x-1][y] = "A"
                        matriz[x][y] = "_"
                        x -= 1
                    elif deslocamento_i > 0:
                        # Movimento para baixo
                        matriz[x+1][y] = "A"
                        matriz[x][y] = "_"
                        x += 1
                    elif deslocamento_j < 0:
                        # Movimento para a esquerda
                        matriz[x][y-1] = "A"
                        matriz[x][y] = "_"
                        y -= 1
                    elif deslocamento_j > 0:
                        # Movimento para a direita
                        matriz[x][y+1] = "A"
                        matriz[x][y] = "_"
                        y += 1
                        
                  # Coloca o robô na posição do lixo
                    levar_lixo(lixo, (i, j), matriz)
                    return (19,18)
                
                elif matriz[i][j] =='O':
                    lixo = 'orgânico'

                    # Calcula o deslocamento da matriz necessário para chegar à célula com lixo
                    deslocamento_i = i - x
                    deslocamento_j = j - y

                # Função para fazer o movimento do robô de acordo com o deslocamento necessário
                    if deslocamento_i < 0:
                        # Movimento para cima
                        matriz[x-1][y] = "A"
                        matriz[x][y] = "_"
                        x -= 1
                    elif deslocamento_i > 0:
                        # Movimento para baixo
                        matriz[x+1][y] = "A"
                        matriz[x][y] = "_"
                        x += 1
                    elif deslocamento_j < 0:
                        # Movimento para a esquerda
                        matriz[x][y-1] = "A"
                        matriz[x][y] = "_"
                        y -= 1
                    elif deslocamento_j > 0:
                        # Movimento para a direita
                        matriz[x][y+1] = "A"
                        matriz[x][y] = "_"
                        y += 1
                        
                    # Coloca o robô na posição do lixo

                    # Chama a função para fazer o movimento do robô
                    levar_lixo(lixo, (i, j), matriz)
                    return (19,18)

                else:
                    return None

def react_based_models(matriz):
    # Encontra a posição atual do robô
    #mantem historicos
    #if ele ja passou por algum lugar e nao encontrou o lixo ele evita de passar por ali, ou seja, nao vai ter tanta aleatoriedade 
    #guarda ambiente em que ele passou e se nao tiver mais lixo , nao vai naquela direção 
    posicao_lixo=(19,19)
    posicao_atual = None
    for i in range(20):
        for j in range(20):
            if matriz[i][j] =="A":
                posicao_atual = (i, j)
                break
                
    i,j=posicao_atual
    percept(i,j,matriz)
    
    #começa andar aleatoriaente
    i_novo,j_novo=ainda_nao_passei(i,j)
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
    
def ainda_nao_passei(x,y):
    #nessa função ele verifica as possições que ele ja passou, se ja onde ele passou nao tiver lixo , ele te que evitar ir novamente lá
    pass

def prever_lixo(matriz, posicao_atual):
    # Função que utiliza um modelo ou estimador para prever o tipo de lixo em uma determinada posição
    # Essa função pode ser substituída pelo uso de modelos de aprendizado de máquina treinados para prever o tipo de lixo
    # com base em dados do ambiente
    # Neste exemplo, usaremos uma função aleatória para simular a previsão
    lixos_possiveis = ["reciclável", "orgânico"]
    lixo_predito = random.choice(lixos_possiveis)
    return lixo_predito
    
def based_goals(matriz):
    # Encontra a posição atual do robô
    #por objetivos
    #o objetivo dele é pegar todos os lixos
    posicao_lixo=(19,19)
    posicao_atual = None
    for i in range(20):
        for j in range(20):
            if matriz[i][j] == "A":
                posicao_atual = (i, j)
                break

    i, j = posicao_atual
    
    i_novo, j_novo = andar_vertical(i, j)
    i += i_novo
    j += j_novo

    # Move o robô para a nova posição
    if posicao_atual == posicao_lixo:
        matriz[posicao_atual[0]][posicao_atual[1]] = "X"
        matriz[i][j] = "A"
        return matriz
    if matriz[i][j] == "R" or matriz[i][j] == "O":
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

    
def andar_vertical(x,y):
    #o robo por objetivo anda na vertical ate pegar um lixo, assim que pegar o lixo ele chama a função para levar a lixeira
    #depois de andar na vertical ele volta para posição inicial
    #se ja tiver percorrido toda linha coluna 1 ele pula para coluna dois e assim sucessivamente
    # O robô anda na vertical até pegar um lixo, e então retorna para a posição inicial da linha seguinte
    if x == 19:  # Se estiver na última linha
        return (1, +y)  # Volta para a posição inicial da próxima linha
    else:
        return (1, 0)  # Anda para baixo na mesma coluna


def based_utility(matriz):
    #começa como simples e se tiver um lixo reciclavel ele armazena na memoria e depois vai buscar 
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
    adjacent=percept_r(i,j,matriz)
    if adjacent:
        melhor_lixo = None
        for i_novo, j_novo in adjacent:
            melhor_lixo = (i_novo, j_novo)
        # Move o robô para a posição do lixo com a maior pontuação
        i_novo, j_novo = melhor_lixo
        matriz[posicao_atual[0]][posicao_atual[1]] = "_"
        matriz[i_novo][j_novo] = "A"
        
    i_novo,j_novo=aleatorio(i,j)
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
    
    #a percepção do de utilidade é que ele tem que dar preferencia para os lixos com maior pontuação 

def percept_r(i, j, matriz):
    #aqui eu tenho que dar uma percepção para ele dar preferencia aos lixos reciclaveis
    # Verifica se o lixo na posição atual é reciclável
    # Lista com as posições adjacentes ao robô
    adjacents = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]

    # Verifica se há lixo reciclável nas posições adjacentes
    for x, y in adjacents:
        if x >= 0 and x < 20 and y >= 0 and y < 20:  # Verifica se a posição está dentro dos limites da matriz
            if matriz[x][y] == "R":
                return (x, y)  # Retorna a posição do lixo reciclável se encontrado

    # Se não houver lixo reciclável nas posições adjacentes, procura por lixo orgânico
    for x, y in adjacents:
        if x >= 0 and x < 20 and y >= 0 and y < 20:  # Verifica se a posição está dentro dos limites da matriz
            if matriz[x][y] == "O":
                return (x, y)  # Retorna a posição do lixo orgânico se encontrado

    # Se não houver lixo reciclável nem orgânico nas posições adjacentes, retorna None
    return None

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