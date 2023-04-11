
##### percept######
    
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
