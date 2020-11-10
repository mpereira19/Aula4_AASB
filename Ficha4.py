<<<<<<< HEAD
gencode = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
    'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W'}

=======
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
        
>>>>>>> faadbed02923efd01ba597da08773ee4ebc57f73

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
 

  
'''
    Definição que introduzida uma sequência de DNA devolve a sua sequência de RNA
    
    Var:
        seq: str
        rna: str
        
    Parameters
    -------------
        seq
    -------------
    Retuns
        rna
'''
def transcricao(seq):
<<<<<<< HEAD
    rna=''
    seq1 = seq.rstrip()
    for i in seq1:
        if i=='T':
            i='U'
            rna += i
        else:
            rna += i
    return rna
 
=======
def valida(seq):
    '''
    Definição que verifica se o input é uma sequência de DNA

    Parameters
    ----------
    seq : str

    Returns
    -------
    True/False

    '''
    for i in range(len(seq)):
        base=seq[i]
        if base=='A' or base=='G' or base=='C' or base=='T':
            pass
        else:
            return False
            break
    return True
>>>>>>> 4eaecc565f676f8095790ffd207becd35dee78c4
>>>>>>> faadbed02923efd01ba597da08773ee4ebc57f73
