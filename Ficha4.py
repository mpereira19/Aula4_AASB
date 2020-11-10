def ler_seq(FileHandle):
    '''
    Parameters
    ----------
    FileHandle : str
        O user introduz a localização do ficheiro.

    Returns
    -------
    seq1 : str
        Devolve a sequência que está presente no ficheiro.
    '''
    with open(FileHandle) as a:
        linhas = [k.strip() for k in a]   
    linhas=[k for k in linhas if len(k)> 0]
    if linhas[0].startswith('>'):
        header = linhas[0]
        seq1= ''.join(linhas[1:])
    else:
        header=''
        seq1= ''.join(linhas)
    return seq1


def troca (seq):
    '''
    Definição que introduzindo uma sequência devolve essa sequência com as bases trocadas pelo seu par.

    Parameters
    ----------
    seq : str

    Returns
    -------
    comp : str
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
    
    Returns
    -------
    rna : str

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
    gencode : dict
    codao : str

    Returns
    -------
    amino : str

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
        

def get_proteins(seq):    
    a=seq.split()
    for l in a:
        g=len(l)
        if g in seq:
            seq[g]+=[l]
        else:
            seq[g]=[l]

    b=sorted(seq, reverse=True)

    for z in range(len(b)):
        if len(seq[b[z]])==1:
            y=seq[b[z]]
    
        else:
            y=sorted(seq[b[z]])
  

def contar_bases(seq):
    '''
    Função que introduzida uma sequência devolve o número de bases dessa sequência.

    Parameters
    ----------
    seq : str

    Returns
    -------
    nbases : int

    '''
    nbases={}
    for i in seq:
        i = i.upper()
        nbases[i]= nbases.get(i,0) + 1
    return nbases


def reading_frames(seq):
    '''
    Função que dada uma sequência devolve uma lista com todas as reading frames.

    Parameters
    ----------
    seq : str

    Returns
    -------
    lst_read_frame : list

    '''
    seq=seq.upper()
    lst_read_frame=[]
    lst_read_frame.append(seq)
    lst_read_frame.append(seq[1::])
    lst_read_frame.append(seq[2::])
    return lst_read_frame


