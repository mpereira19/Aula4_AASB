def troca (seq):
    '''
    Definição que introduzindo uma sequência devolve essa sequência com as bases trocadas pelo seu par.

    Parameters
    ----------
    seq : str

    Returns
    -------
    comp.
    '''
    pares_bases = {'A':'T', 'C':'G', 'T':'A', 'G':'C'}
    comp =''.join(pares_bases[n] for n in (seq))
    return comp
        

def complemento_inverso(seq):
    ''' 
    Definição que introduzindo uma sequência devolve o seu complemento inverso.

    Parameters
    ----------    
    seq: str
    
    Returns
    -------
    comple_inv
    '''
    inverso = seq[::-1]
<<<<<<< HEAD
    comple_inv=troca(inverso)
    return comple_inv
=======
 
    
 
def transcricao(seq):
        '''
    
    
        '''
        
        
>>>>>>> 4eaecc565f676f8095790ffd207becd35dee78c4
