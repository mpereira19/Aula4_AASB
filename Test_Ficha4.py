import unittest
import Ficha4

class testficha4(unittest.TestCase):
    
    
    # def test_transcricao(self):
        
    #     result = Ficha4.transcricao('ATGC')
    #     self.assertEqual(result, 'AUGC', 'Não funciona de todo')
    #     result = Ficha4.transcricao('AtgC')
    #     self.assertEqual(result, 'AUGC', 'O programa não distingue minúsculas de Maiúscuas')
    #     result = Ficha4.transcricao('ATGC0')
    #     self.assertEqual(result, ValueError, 'O programa tem em conta outras letras para além de A, T, G e C')
    #     result = Ficha4.transcricao('AUGC')
    #     self.assertEqual(result, 'AUGC', 'O programa não deteta que foi introduzida uma sequência de RNA')
    #     result = Ficha4.transcricao('ATM_DE')
    #     self.assertEqual(result, ValueError, 'O programa transcreve uma sequência de aminoácidos')
        
        

    # def test_complemento_inverso(self):
        
    #     result = Ficha4.complemento_inverso('ATGC')
    #     self.assertEqual(result, 'GCAT', 'Não funciona de todo')
    #     result = Ficha4.complemento_inverso('AtgC')
    #     self.assertEqual(result, 'GCAT', 'O programa não distingue minúsculas de Maiúscuas')
    #     result = Ficha4.complemento_inverso('atgc')
    #     self.assertEqual(result, 'GCAT')
    #     result = Ficha4.complemento_inverso('ATGCMK')
    #     self.assertEqual(result, ValueError, 'O programa tem em conta outras letras para além de A, T, G e C')
    #     result = Ficha4.complemento_inverso('AAAAAAAGGGU')
    #     self.assertEqual(result, ValueError)
        
    # def test_traducao(self):
        
    #     result = Ficha4. traducao('ATGC')
    #     self.assertEqual(result,'M', 'Não funciona de todo')
    #     result = Ficha4. traducao('atgc')
    #     self.assertEqual(result,'M', 'O programa não distingue minúsculas de Maiúscuas')
    #     result = Ficha4. traducao('AtgC')
    #     self.assertEqual(result,'M')
    #     result = Ficha4. traducao('ATGCop')
    #     self.assertEqual(result, ValueError, 'O programa tem em conta outras letras para além de A, T, G e C')
    #     result = Ficha4. traducao('ATGACCGTAA')
    #     self.assertEqual(result,'MTV')
        
    
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
        self.assertEqual(result, True, 'O programa não deteta sequências de aa')
        result = Ficha4.valida('MZTTTTOOOO_RLSV')
        self.assertEqual(result, False, 'O programa ainda deteta outras letras não associadas com aa ')
   
        
        
        
    # def test_get_proteins(self):
        
        
        #result = Ficha4.get_proteins('ATGAATTAA')
        #self.assertEqual(result, ['MN_'], 'Teste 1')
        #result1 = Ficha4.get_proteins('ATGCAT')
        #self.assertEqual(result1, ['MH'], 'Teste 2')
        # result = Ficha4.get_proteins('ATGAATTAA')
        # self.assertEqual(result, ['MN_'], 'Teste 1')
        # result1 = Ficha4.get_proteins('ATGCAT')
        # self.assertEqual(result1, ['MH'], 'Teste 2')
        # result1 = Ficha4.get_proteins('ATGAATTAAATGCAT')
        # self.assertEqual(result1, ['MN_', 'MH'])
        # result = Ficha4. traducao('ATGACCGTAA')
        # self.assertEqual(result, ['MTV'], 'Teste 3')
        # result = Ficha4. traducao('ATGACCGTAA')
        # self.assertEqual(result, 'MTV', 'Teste 4')
        # result = Ficha4. traducao('ATGCATCATTGAATGCGTCGT')
        # self.assertEqual(result, ['MHH_', 'MRR'], 'Teste 5')
    
    # def test_contar_bases(self):
        
    #     result = Ficha4.contar_bases('ATGC')
    #     self.assertEqual(result, {'A': 1, 'T': 1, 'G': 1, 'C': 1}, 'Não funciona de todo')
    #     result = Ficha4.contar_bases('AtgC')
    #     self.assertEqual(result, {'A': 1, 'T': 1, 'G': 1, 'C': 1})
    #     result = Ficha4.contar_bases('ATGffC')
    #     self.assertEqual(result, ValueError, 'O programa tem em conta outras letras para além de A, T, G e C')
        
    # def test_reading_frames(self):
        
    #     result = Ficha4.reading_frames('ATGC')
    #     self.assertEqual(result, ['ATGC', 'TGC', 'GC'], 'Ele não identifica todas as reading frames')
    #     result = Ficha4.reading_frames('AtgC')
    #     self.assertEqual(result, ['ATGC', 'TGC', 'GC'], 'O programa não distingue minusculas de maiusculas')
        # result = Ficha4.reading_frames('ATGrrrC')
        # self.assertEqual(result, ValueError, 'O programa não deteta outro tipo de letras')
        
    
if __name__== '__main__':
    unittest.main()
    