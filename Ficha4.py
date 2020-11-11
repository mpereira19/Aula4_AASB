def ler_seq(FileHandle):
    '''
    Função que introduzida uma diretoria devolve a sequência presente no ficheiro.

    Parameters
    ----------
    FileHandle : str

    Returns
    -------
    seq1 : str

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

def ler_Fasta_seq(FileHandle):
    '''
    Função que introduzida a diretoria do ficheiro FASTA devolve a sequência presente no ficheiro.

    Parameters
    ----------
    FileHandle : str

    Returns
    -------
    seq1 : str

    '''
    with open(FileHandle) as a:
        linhas = [k.strip() for k in a]   
    linhas=[k for k in linhas if len(k)> 0]
    if linhas[0].startswith('>'):
        header = linhas[0]
        seq1= ''.join(linhas[1:])
    return seq1
        


def complemento_inverso(seq):
    ''' 
    Definição que introduzida uma sequência devolve o seu complemento inverso.

    Parameters
    ----------    
    seq: str
    
    Returns
    -------
    comple_inv : str or ValueError
    '''

    seq=seq.upper()
    if valida(seq)==True:
        comple_inv= seq[::-1].lower().replace('a','T').replace('t','A').replace('g','C').replace('c','G')
    else:
        comple_inv = ValueError
    return comple_inv
    
def transcricao(seq):
    '''
    Função que introduzida uma sequência de DNA devolve a sua sequência de RNA.

    Parameters
    ----------
    seq : str
    
    Returns
    -------
    rna : str or ValueError

    '''
    seq=seq.upper()
    if valida(seq)==True:
        rna = seq.replace('T', 'U')
    else:
        rna = ValueError
    return rna

def traducao(seq):

    '''
    Função que introduzida uma sequência DNA devolve uma sequência de aminoácidos.

    Parameters
    ----------
    seq : str

    Returns
    -------
    amino : str or ValueError

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
    if valida(seq)==True:
        for i in range(0, len(seq), 3):
            codao = seq[i : i + 3] 
            if i==0:
                amino=gencode[codao]
            elif len(codao)==3:
                amino += gencode[codao]
            else:
                pass
    else:
        amino = ValueError
    return amino

def valida(seq):
    '''
    Função que verifica se a sequência introduzida é uma sequência de DNA.
    
    Parameters
    ----------
    seq : str

    Returns
    -------
    True/False
    
    '''
    seq = seq.upper()
    for i in range(len(seq)):
        base=seq[i]
        if base=='A' or base=='G' or base=='C' or base=='T':
            pass
        else:
            return False
            break
    return True
    

def contar_bases(seq):
    '''
    Função que introduzida uma sequência devolve o número de bases dessa sequência.

    Parameters
    ----------
    seq : str

    Returns
    -------
    nbases : int or ValueError

    '''
    if valida(seq)==True:
        nbases={}
        seq= seq.strip()
        for base in seq:
            base = base.upper()
            nbases[base]= nbases.get(base, 0) + 1
    else: 
        nbases = ValueError
    return nbases

def reading_frames(seq):
    '''
    Função que dada uma sequência devolve uma lista com todas as reading frames.

    Parameters
    ----------
    seq : str

    Returns
    -------
    lst_read_frame : list or ValueError

    '''
    seq=seq.upper()
    if valida(seq)==True:
        lst_read_frame=[]
        lst_read_frame.append(seq)
        lst_read_frame.append(seq[1:])
        lst_read_frame.append(seq[2:])
    else:
        lst_read_frame = ValueError
    return lst_read_frame


def get_proteins(seq):
    '''
    Função que dada uma sequênciadevolve numa lista todas as proteínas ordenadas por tamanho e por ordem alfabética para as do mesmo tamanho.

    Parameters
    ----------
    seq : str

    Returns
    -------
    result : list or ValueError

    '''

    import re
    seq= seq.upper()
    if valida(seq)==True:
        seq1 = complemento_inverso(seq)
        lst_all_reading_frames = reading_frames(seq) + reading_frames(seq1)
        translation_lst = [traducao(frames) for frames in lst_all_reading_frames]
        lista = [re.findall('M[A-Z]*_',orf) for orf in translation_lst]
        result = sorted({p for lp in lista for p in lp}, key = lambda x: (-len(x), x))
    else:
        result = ValueError
    return result