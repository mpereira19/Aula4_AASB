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

  


