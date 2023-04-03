import random

def robocop(matriz):
    # Encontra a posição atual do robô
    posicao_atual = None
    for i in range(20):
        for j in range(20):
            if matriz[i][j] =="A":
                posicao_atual = (i, j)
                break
    i,j=posicao_atual
    i_novo,j_novo=direca(i,j)
    i+=i_novo
    j+=j_novo
    
    # Move o robô para a nova posição
    matriz[posicao_atual[0]][posicao_atual[1]] = "_"
    matriz[i][j] = "A"
    return matriz
import random

def direca(x, y):
    # Verifica as direções possíveis, levando em consideração a posição do robô na matriz
    possiveis_direcoes = []
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

    
def coletar_lixo(self, tipo_lixo):
        if self.lixo is None:
            if self.ambiente[self.posicao[0]-1][self.posicao[1]-1][tipo_lixo] > 0:
                self.lixo = tipo_lixo
                return True
        return False
    
def pegar_lixo():
    '''x, y = posicao_robo[0], posicao_robo[1]
    if matriz[x][y] != 0:
        return matriz[x][y]'''
        
def soltar_lixo():
    '''x, y = posicao_robo[0], posicao_robo[1]
    if matriz[x][y] == 0:
        matriz[x][y] = " "
        return True'''
def voltar_lixeira(self):
        if self.lixo is not None:
            if self.posicao == self.lixeira.posicao:
                self.largar_lixo()
                return True
            else:
                caminho = self.caminho_livre(self.lixeira.posicao)
                if caminho:
                    self.andar(caminho[0])
                    return True
        return False

def caminho_livre(self, destino):
    fila = [[self.posicao]]
    visitados = set()
    while fila:
        caminho = fila.pop(0)
        posicao_atual = caminho[-1]
        if posicao_atual == destino:
            return caminho[1:]
        elif posicao_atual not in visitados:
            for direcao in self.movimentos:
                nova_pos = self.proxima_posicao(posicao_atual, direcao)
                if nova_pos and self.ambiente[nova_pos[0]-1][nova_pos[1]-1]['vazio']:
                    nova_caminho = list(caminho)
                    nova_caminho.append(direcao)
                    fila.append(nova_caminho)
            visitados.add(posicao_atual)
    return None 
 
def run(self, num_iteracoes):
        # Executa o ambiente por um determinado número de iterações
        for i in range(num_iteracoes):
            # Imprime o ambiente e a pontuação atual
            print(f"\nIteração {i+1}:")
            self.imprimir_ambiente()
            print(f"Pontuação: {self.robo.pontuacao}")
            
            # Verifica se o robô está com lixo e tenta levá-lo para a lixeira
            if self.robo.lixo is not None:
                self.robo.voltar_lixeira()
            
            # Coleta lixo da posição atual do robô
            self.robo.coletar_lixo('orgânico')
            self.robo.coletar_lixo('reciclável')
            
            # Decide a próxima ação do robô aleatoriamente
            acao = random.choice(['andar', 'largar_lixo'])
            if acao == 'andar':
                # Tenta andar para uma direção aleatória
                direcao = random.choice(list(self.robo.movimentos.keys()))
                self.robo.andar(direcao)      
        
        

        
        
