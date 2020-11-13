import unittest
import Ficha4


class testficha4(unittest.TestCase):
    
    
    def test_transcricao(self):
        
        self.assertRaises(TypeError, Ficha4.transcricao, '', 'Sequência inválida')
        result = Ficha4.transcricao('ATGC')
        self.assertEqual(result, 'AUGC', 'Não funciona de todo')
        result = Ficha4.transcricao('AtgC')
        self.assertEqual(result, 'AUGC', 'O programa não distingue minúsculas de Maiúscuas')
        self.assertRaises(TypeError, Ficha4.transcricao, 'ATGC0', 'O programa tem em conta outras letras para além de A, T, G e C')
        self.assertRaises(TypeError, Ficha4.transcricao, 'AUGC', 'O programa não deteta que foi introduzida uma sequência de RNA')
        self.assertRaises(TypeError, Ficha4.transcricao, 'ATM_DE', 'O programa transcreve uma sequência de aminoácidos')
        
    def test_complemento_inverso(self):
        
        self.assertRaises(TypeError, Ficha4.complemento_inverso, '', 'Sequência inválida')
        result = Ficha4.complemento_inverso('ATGC')
        self.assertEqual(result, 'GCAT', 'Não funciona de todo')
        result = Ficha4.complemento_inverso('AtgC')
        self.assertEqual(result, 'GCAT', 'O programa não distingue minúsculas de Maiúscuas')
        self.assertRaises(TypeError, Ficha4.complemento_inverso, 'ATGCMK', 'O programa tem em conta outras letras para além de A, T, G e C')
        self.assertRaises(TypeError, Ficha4.complemento_inverso, 'AAAAAAAG_G0GU', 'A sequência não deveria funcionar')
        
    def test_traducao(self):
        
        self.assertRaises(TypeError, Ficha4.traducao, '', 'Sequência inválida')
        result = Ficha4. traducao('ATGC')
        self.assertEqual(result,'M', 'Não funciona de todo')
        result = Ficha4. traducao('atgc')
        self.assertEqual(result,'M', 'O programa não distingue minúsculas de Maiúscuas')
        result = Ficha4. traducao('AtgC')
        self.assertEqual(result,'M')
        self.assertRaises(TypeError, Ficha4.traducao, 'ATGCop', 'O programa tem em conta outras letras para além de A, T, G e C')
        result = Ficha4. traducao('ATGACCGTAA')
        self.assertEqual(result,'MTV')
        
    
    def test_valida(self):
        
        result = Ficha4.valida('ATG0C')
        self.assertEqual(result, False, 'A função está a identificar números')
        result = Ficha4.valida('ATGC')
        self.assertEqual(result, True, 'O programa não deteta sequências de DNA')
        result = Ficha4.valida('AtgC')
        self.assertEqual(result, True, 'O programa não distingue minusculas e maiusculas')
        result = Ficha4.valida('AUGC')
        self.assertEqual(result, True, 'Não identifica sequências de RNA')
        result = Ficha4.valida('MITNSRGVY_')
        self.assertEqual(result, True, 'O programa não deteta sequências de aminoácidos')
        result = Ficha4.valida('MZTTTTOOOO_RLSV')
        self.assertEqual(result, False, 'O programa ainda deteta outras letras não associadas com aa ')
   
    def test_determina_dna(self):
        
        
        result = Ficha4.determina_dna('ATGC')
        self.assertEqual(result, True, 'A função não deteta sequências de DNA')
        result = Ficha4.determina_dna('AttgC')
        self.assertEqual(result, True, 'A função não distingue minúsculas de maiúsculas')
        result = Ficha4.determina_dna('AUGC')
        self.assertEqual(result, False, 'A função deteta uma sequências de RNA')
        result = Ficha4.determina_dna('MTAR_')
        self.assertEqual(result, False, 'A função deteta uma sequências de aminoácidos')
        result = Ficha4.determina_dna('ATG0C')
        self.assertEqual(result, False, 'A função está a identificar números')
        result = Ficha4.determina_dna('AAAAA')
        self.assertEqual(result, True, 'A função atrapalha-se em sequências repetitivas')
        
    
    def test_determina_rna(self):
        
        result = Ficha4.determina_rna('AUGC')
        self.assertEqual(result, True, 'A função não deteta sequências de RNA')
        result = Ficha4.determina_rna('AuugC')
        self.assertEqual(result, True, 'A função não distingue minúsculas de maiúsculas')
        result = Ficha4.determina_rna('ATGC')
        self.assertEqual(result, False, 'A função deteta uma sequências de DNA')
        result = Ficha4.determina_rna('MTAR_')
        self.assertEqual(result, False, 'A função deteta uma sequências de aminoácidos')
        result = Ficha4.determina_rna('ATG0C')
        self.assertEqual(result, False, 'A função está a identificar números')
        result = Ficha4.determina_rna('AAAAA')
        self.assertEqual(result, True, 'A função deveria assumir esta sequência como DNA')
        
    def test_determina_amino(self):
        
        result = Ficha4.determina_amino('MTIRSLPH_')
        self.assertEqual(result, True, 'A função não deteta sequências de aminoácidos')
        result = Ficha4.determina_amino('MTIrssSLPH_')
        self.assertEqual(result, True, 'A função não distingue minúsculas de maiúsculas')
        result = Ficha4.determina_amino('ATGC')
        self.assertEqual(result, True, 'A função deteta uma sequências de DNA')  
        result = Ficha4.determina_amino('AUGC')
        self.assertEqual(result, False, 'A função deteta uma sequências de RNA')
        result = Ficha4.determina_amino('ATG0C')
        self.assertEqual(result, False, 'A função está a identificar números')
        result = Ficha4.determina_amino('AAAAA')
        self.assertEqual(result, True, 'A função deveria assumir esta sequência como DNA')
        

    def test_complemento_proteina_dna(self):
        
        result = Ficha4.complemento_proteina_dna('ATGCATTGA')
        self.assertEqual(result, [['MH_'], [], [], [], [], []], 'Não funciona de todo')
        result = Ficha4.complemento_proteina_dna('ATGcaTTGA')
        self.assertEqual(result, [['MH_'], [], [], [], [], []], 'Não funciona de todo')
        result = Ficha4.complemento_proteina_dna('ATGCATGCATGC')
        self.assertEqual(result, [[], [], [], [], [], []], 'Deveria dar 1 lista com 6 conjuntos vazios')
        self.assertRaises(TypeError, Ficha4.complemento_proteina_dna, '', 'O programa lê o conjunto vazio')
        self.assertRaises(TypeError, Ficha4.complemento_proteina_dna, 'ATGCATG0CATGC', 'Não deveria realizar a leitura')
        self.assertRaises(TypeError, Ficha4.complemento_proteina_dna, 'AUGCAUGCAUGC', 'Lê sequências e RNA')
        
        
    def test_get_proteins(self):
            
        result = Ficha4.get_proteins('ATGAATTAA')
        self.assertEqual(result, ['MN_'], 'Teste 1')
        result1 = Ficha4.get_proteins('ATGAATTAAATGCAT')
        self.assertEqual(result1, ['MN_'])
        result = Ficha4. get_proteins('ATGCATCATTGAATGCGTCGT')
        self.assertEqual(result, ['MHH_'], 'Teste 5')
        self.assertRaises(TypeError, Ficha4.get_proteins, '', 'O programa lê o conjunto basio')
        self.assertRaises(TypeError, Ficha4.get_proteins, 'ATGCATG00C', 'O programa lê outras letras para além de A, T, G e C')
        self.assertRaises(TypeError, Ficha4.get_proteins, 'AUGACCGUAA', 'O programa lê sequências de RNA')
        self.assertRaises(TypeError, Ficha4.get_proteins, 'ATGACCGTAA', 'O programa não deveria dar nenhum resultado')
        
        
    def test_contar_bases(self):
        
        self.assertRaises(TypeError, Ficha4.contar_bases, '', 'Sequência inválida')
        result = Ficha4.contar_bases('ATGC')
        self.assertEqual(result, {'A': 1, 'T': 1, 'G': 1, 'C': 1}, 'Não funciona de todo')
        result = Ficha4.contar_bases('AtgC')
        self.assertEqual(result, {'A': 1, 'T': 1, 'G': 1, 'C': 1})
        result = Ficha4.contar_bases('AUUUUGC')
        self.assertEqual(result, {'A': 1, 'U': 4, 'G': 1, 'C': 1}, 'Não funciona de todo')
        self.assertRaises(TypeError, Ficha4.contar_bases, '', 'O programa lê o conjunto basio')
        self.assertRaises(TypeError, Ficha4.contar_bases, 'ATUGC', 'O programa mete o U e o T na mesma sequência')
        self.assertRaises(TypeError, Ficha4.contar_bases, 'ATGffC', 'O programa tem em conta outras letras para além de A, T, G e C')
        self.assertRaises(TypeError, Ficha4.contar_bases, 'ATG0C', 'O programa tem em conta outras letras para além de A, T, G e C')
    
    
    def test_reading_frames(self):
        
        result = Ficha4.reading_frames('ATGC')
        self.assertEqual(result, ['ATGC', 'TGC', 'GC'], 'Ele não identifica todas as reading frames')
        result = Ficha4.reading_frames('AtgC')
        self.assertEqual(result, ['ATGC', 'TGC', 'GC'], 'O programa não distingue minusculas de maiusculas')
        self.assertRaises(TypeError, Ficha4.reading_frames, '', 'O programa lê o conjunto basio')
        self.assertRaises(TypeError, Ficha4.reading_frames, 'ATGrrrC', 'O programa não deteta outro tipo de letras')
        self.assertRaises(TypeError, Ficha4.reading_frames, 'ATUGCC', 'O programa assume o T e o U na mesma sequência')
        self.assertRaises(TypeError, Ficha4.reading_frames, 'AUUUUGCC', 'O programa deteta sequências de RNA')
    
    
if __name__== '__main__':
    unittest.main()
    