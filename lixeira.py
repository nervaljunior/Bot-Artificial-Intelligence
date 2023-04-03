class lixo:
        def __init__(self, posicao):
                self.posicao = posicao
                self.capacidade = {'orgânico': 0, 'reciclável': 0}

        def receber_lixo(self, tipo_lixo):
                self.capacidade[tipo_lixo] += 1
                
        def potuacao(self):
                pont=0
                quant=self.capacidade.values()
                x,y=quant
                y*=5
                pont=y+x
                
                return pont
        

