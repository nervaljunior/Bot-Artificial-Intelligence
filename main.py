from array import *
import time
from os import system
from matriz import *
from agente import *
from lixeira import lixo




if __name__=="__main__":
    ambiente = gerar_ambiente()
    
    while True:
        imprime(ambiente)
        time.sleep(0)
        system("cls")
        robocop(ambiente)
        lixo.potuacao()
    
    
    

    

    
        
    
    

