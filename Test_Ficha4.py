import unittest
import Ficha4

class testficha4(unittest.TestCase):
    
    
    
    def test_transcricao(self):
        
        result = Ficha4.transcricao('ATGC')
        self.assertEqual(result, 'AUGC')


    def test_troca(self):
        
        result = Ficha4.troca('ATGC')
        self.assertEqual(result,'TACG')
        
    def test_complemento_inverso(self):
        
        result = Ficha4.complemento_inverso('ATGC')
        self.assertEqual(result, 'GCAT')
        
    def test_traducao(self):
        
        result = Ficha4. traducao('ATGC')
        self.assertEqual(result,'M')
    
    def test_valida(self):
        
        result = Ficha4.valida('ATG0C')
        self.assertEqual(result, False)
        
    # def test_get_proteins(self):
        
    #     result = Ficha4.get_proteins('ATGCATGC')
    #     self.assertEqual(result, '')
    
    def test_contar_bases(self):
        
        result = Ficha4.contar_bases('ATGC')
        self.assertEqual(result, {'A': 1, 'T': 1, 'G': 1, 'C': 1})
     
    
    
        
if __name__== '__main__':
    unittest.main()
    