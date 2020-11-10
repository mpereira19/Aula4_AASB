def troca (seq):
    '''
    Definição que introduzindo uma sequência devolve essa sequência com as bases trocadas pelo seu par.

    Parameters
    ----------
    seq : str

    Returns
    -------
    comp
    '''
    pares_bases = {'A':'T', 'C':'G', 'T':'A', 'G':'C'}
    comp =''.join(pares_bases[n] for n in (seq))
    return comp
        

def complemento_inverso(seq):
    ''' 
    Definição que introduzida uma sequência devolve o seu complemento inverso.

    Parameters
    ----------    
    seq: str
    inverso : str
    comple_inv : str
    
    Returns
    -------
    comple_inv
    '''
    seq=seq.upper()
    inverso = seq[::-1]
    comple_inv=troca(inverso)
    return comple_inv
    
def transcricao(seq):
    '''
    Função que introduzida uma sequência de DNA devolve a sua sequência de RNA.

    Parameters
    ----------
    seq : str
    seq1 : str
    rna : str
    

    Returns
    -------
    rna

    '''
    seq=seq.upper()
    rna=''
    seq1 = seq.rstrip()
    for i in seq1:
        if i=='T':
            i='U'
            rna += i
        else:
            rna += i
    return rna
<<<<<<< HEAD

    

def traducao(seq):

    '''
    Função que introduzida uma sequência DNA devolve uma sequência de aminoácidos.

    Parameters
    ----------
    seq : str
    amino : str
    gencode : dict
    codao : str

    Returns
    -------
    amino

    '''
    gencode = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M', 'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K', 'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L', 'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q', 'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V', 'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E', 'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S', 'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_', 'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W'}
    
    seq = seq.upper()
    for i in range(0, len(seq), 3):
        codao = seq[i : i + 3] 
        if i==0:
            amino=gencode[codao]
        elif len(codao)==3:
            amino += gencode[codao]
        else:
            pass
    return amino

  


=======
 
=======
def valida(seq):
        '''
    Função que verifica se a sequência introduzida é uma sequência de DNA.
    
    Parameters
    ----------
    seq : str
    base : str

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
>>>>>>> 529ae2ea7479a1ba1beaafd1ebd11f9d18e2255a
>>>>>>> 51ec095b4e699306b298a5ad37a974d5015b462e
