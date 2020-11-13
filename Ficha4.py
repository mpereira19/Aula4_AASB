fich_vaz = "Ficheiro vazio"

def ler_seq(FileHandle):
    """ Funcao que devolve a sequencia contida numa linha do ficheiro
    Parameters
    ----------
    FileHandle : _io.TextIOWrapper
        Um ficheiro .txt aberto que contém uma sequência de DNA por linha
    Returns
    -------
    
    seq : str
        Sequência de DNA que está contida numa linha   
    """
    
    seq = FileHandle.readline()
    assert seq != '', fich_vaz
    seq= seq.upper()
    return seq

def ler_FASTA_seq(file):
    """Função que devolve a primeira sequência contida num ficheiro FASTA
    Se o ficheiro apresentar mais do que uma sequência, devolve apenas a primeira
    
    Parameters
    ----------
    FileHandle : _io.TextIOWrapper
        Um ficheiro FASTA
        
    Returns
    -------
    seq : str 
        Primeira sequência contida num ficheiro FASTA, sem o cabeçalho
    """
    import re
    linhas = file.readlines()
    assert linhas != [], fich_vaz
    seq = ''
    a = ''.join(linhas)
    header = re.findall('>.+[\n]',a) # para obter a lista dos cabeçalhos
    for l in linhas:
        if l == header[0]:
            continue
        elif l not in header:
            seq+=l.replace('\n','')
        elif l in header: break
    return seq
        


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
    if determina_dna(seq)==True:
        comple_inv= seq[::-1].lower().replace('a','T').replace('t','A').replace('g','C').replace('c','G')
        return comple_inv
    else: raise TypeError('Sequência inválida')
    
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
    if determina_dna(seq)==True:
        rna = seq.replace('T', 'U')
        return rna
    else: raise TypeError

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
    if determina_rna(seq)==True:
        seq = seq.replace('U','T')
    if determina_dna(seq)==True:
        for i in range(0, len(seq), 3):
            codao = seq[i : i + 3] 
            if i==0:
                amino=gencode[codao]
            elif len(codao)==3:
                amino += gencode[codao]
            else: pass
        return amino
    else: raise TypeError('Sequência inválida')

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
    if determina_amino(seq)!=True and determina_rna(seq)!=True and determina_amino(seq)!=True:
        return False
    else: return True

def determina_dna(seq):
    '''
    Função que dada uma sequência determina se é uma sequência de dna ou não

    Parameters
    ----------
    seq : str
            sequência de dna

    Returns
    -------
    bool
            se seq é cadeia de dna retorna True senão retorna False

    '''
    seq=seq.upper()
    x = seq.strip()
    for i in x:
        if i!='A' and i!='T' and i!='C' and i!='G':
            return False
            break
        else: pass
    return True

def determina_rna(seq):
    '''
    Função que determina se a cadeia introduzida é ou não uma cadeia de rna.

    Parameters
    ----------
    seq : str
        cadeia de rna

    Returns
    -------
    bool
        True or False

    '''
    seq = seq.upper()
    x = seq.strip()
    for i in x:
        if i!='A' and i!='U' and i!='G' and i!='C':
            return False
            break
        else: pass
    return True

def determina_amino(seq):
    '''
    Função que determina se a sequência introduzida é ou não uma sequência de aminoácidos.

    Parameters
    ----------
    seq : str
        sequência de aminoácidos

    Returns
    -------
    bool
        True or False

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
    x = seq.strip()
    for i in x:
        if i not in gencode.values():
            return False
            break
        else: pass
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
        return nbases
    else: 
        raise TypeError
    

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

def complemento_proteina_dna(seq):
    '''
    Função que dada uma sequência de dna devolve uma lista de todas as traduções.

    Parameters
    ----------
    seq : str
        Cadeia de DNA.

    Returns
    -------
    lista : list
        Lista da tradução da sequência de DNA.

    '''
    if determina_dna(seq)==True:
        import re
        seq1 = complemento_inverso(seq)
        lst_all_reading_frames = reading_frames(seq) + reading_frames(seq1)
        translation_lst = [traducao(frames) for frames in lst_all_reading_frames]
        seq1 = complemento_inverso(seq)
        lst_all_reading_frames = reading_frames(seq) + reading_frames(seq1)
        translation_lst = [traducao(frames) for frames in lst_all_reading_frames]
        lista = [re.findall('M[A-Z]*_',orf) for orf in translation_lst]
        return lista
    else:
        raise TypeError   



def get_proteins(seq):
    '''
    Função que dada uma sequência devolve numa lista todas as proteínas ordenadas por tamanho e por ordem alfabética para as do mesmo tamanho.

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
        if determina_dna(seq)==True:
            lista = complemento_proteina_dna(seq)
            result = sorted({p for lp in lista for p in lp}, key = lambda x: (-len(x), x))
        elif determina_rna(seq)==True:
            rna = seq.replace('U','T')
            amino = traducao(rna)
            lista = re.findall('M[A-Z]*_',amino)
            result = sorted({p for p in lista}, key = lambda x: (-len(x), x))
        elif determina_amino(seq)=='True':
            lista = re.findall('M[A-Z]*_',seq)
            result = sorted({p for p in lista}, key = lambda x: (-len(x), x))
        return result
    else:
        raise TypeError