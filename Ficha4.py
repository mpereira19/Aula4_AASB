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
    
    Returns
    -------
    comple_inv : str
    '''

    seq=seq.upper()
    if valida(seq)==True:
        inverso = seq[::-1]
        comple_inv=troca(inverso)
        return comple_inv
    
def transcricao(seq):
    '''
    Função que introduzida uma sequência de DNA devolve a sua sequência de RNA.

    Parameters
    ----------
    seq : str
    
    Returns
    -------
    rna : str

    '''
    seq=seq.upper()
    if valida(seq)==True:
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
    if valida(seq)==True:
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
    nbases : int

    '''
    if valida(seq)==True:
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
    if valida(seq)==True:
        lst_read_frame=[]
        lst_read_frame.append(seq)
        lst_read_frame.append(seq[1::])
        lst_read_frame.append(seq[2::])
        return lst_read_frame

def get_translated_frames(seq):
    '''
    Função que dada uma sequência devolve lista de todas as reading frames de uma sequência.

    Parameters
    ----------
    seq : str

    Returns
    -------
    lst_all_translations : list

    '''
    seq= seq.upper()
    if valida(seq)==True:
        seq1 = complemento_inverso(seq)
        lst_all_reading_frames = reading_frames(seq) + reading_frames(seq1)
        lst_all_translations = []
        for frame in lst_all_reading_frames:
            lst_all_translations.append(traducao(frame))
        return lst_all_translations

def remove_repetidos(lista):
    '''
    Introduzida uma lista é devolvida a mesma lista organizada alfabeticamente e sem valores repetidos.

    Parameters
    ----------
    lista : list

    Returns
    -------
    l : list

    '''
    l = []
    for i in lista:
        if i not in l:
            l.append(i)
    l.sort()
    return l

def dic_protein(seq):
    '''
    Função que dada uma sequência devolve um dicionário com todas as proteínas presentesnessa sequência incluindo repetições.

    Parameters
    ----------
    seq : str

    Returns
    -------
    dic_all_proteins : dict

    '''
    import re
    translation_lst = get_translated_frames(seq)
    dic_all_proteins={}
    for protein in translation_lst:
        prot_found = re.findall('M.*?_',protein)
        for prot in prot_found:
            if len(prot) not in dic_all_proteins:
                dic_all_proteins[len(prot)] = prot
            else:
                dic_all_proteins[len(prot)] += prot
    return dic_all_proteins


def get_proteins(seq):
    '''
    Função que dada uma sequênciadevolve numa lista todas as proteínas ordenadas por tamanho e por ordem alfabética para as do mesmo tamanho.

    Parameters
    ----------
    seq : str

    Returns
    -------
    lst_organized_proteins : list

    '''
    dictionary = dic_protein(seq)
    keys = dictionary.keys()
    keys = sorted (keys, reverse=True)
    
    lst_organized_proteins=[]
    for chave in keys:
        if len(dictionary[chave])==1:
            lst_organized_proteins += dictionary[chave]
        else:
            dictionary[chave] = remove_repetidos(dictionary[chave])
            dictionary[chave] = sorted (dictionary[chave])
            lst_organized_proteins += dictionary[chave]
    return lst_organized_proteins

