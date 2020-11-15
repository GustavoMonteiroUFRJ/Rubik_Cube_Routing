import numpy as np

def createX(Acp, Aep, Aco, Aeo, Bcp, Bep, Bco, Beo):
    
    # Declarando as estruturas de dados do estado auxiliar
    Xcp = np.zeros_like(Acp)
    Xep = np.zeros_like(Aep)
    Xco = np.zeros_like(Aco)
    Xeo = np.zeros_like(Aeo)
    
    # Pre computando o index das quinas.
    Bcp_index = np.zeros_like(Bcp)
    for i in range(len(Bcp)):
        Bcp_index[Bcp[i]]=i
    
    # Criando o vetor de posicao das quinas do estado auxiliar
    for i in range(len(Acp)):
        Xcp[i] = Bcp_index[Acp[i]]
    
    # Pre computando o index dos meios.
    Bep_index = np.zeros_like(Bep)
    for i in range(len(Bep)):
        Bep_index[Bep[i]]=i
    
    # Criando o vetor de posicao dos meios do estado auxiliar
    for i in range(len(Aep)):
        Xep[i] = Bep_index[Aep[i]]
        
    # Criando o vetor de orientacao das quinas do estado auxiliar
    for i in range(len(Aco)):
        posicao_final = Bcp_index[Acp[i]]
        
        orientacao_inicial = Aco[i]
        orientacao_final = Bco[posicao_final]
        Xco[i] = (orientacao_inicial - orientacao_final) %3

    # Criando o vetor de orientacao dos meios do estado auxiliar
    for i in range(len(Aeo)):
        posicao_final = Bep_index[Aep[i]]
        
        orientacao_inicial = Aeo[i]
        orientacao_final = Beo[posicao_final]
        Xeo[i] = (orientacao_inicial - orientacao_final) %2

    return (Xcp, Xep, Xco, Xeo)