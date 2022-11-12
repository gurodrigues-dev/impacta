'''
Você deve escrever suas classes no arquivo luta.py, que foi
compartilhado junto desse arquivo luta_testes

Para que as classes do arquivo luta.py fiquem disponíveis nesse arquivo luta_testes.py,
use a linha abaixo
'''

# ESTE ARQUIVO ANTERIORMENTE SE CHAMVA LUTA.PY 

from luta import Pessoa, Mago, Lutador, Barbaro

import unittest

class TesteLutas(unittest.TestCase):
    
   def test_01_pessoa(self):
      marcia = Pessoa('marcia',20)
      self.assertEqual(marcia.get_vida(),20)
      claudius = Pessoa('claudius',22)
      self.assertEqual(claudius.get_vida(),22)

   def test_02_pessoa_ataca(self):
      marcia = Pessoa('marcia',20)
      self.assertEqual(marcia.get_vida(),20)
      claudius = Pessoa('claudius',22)
      self.assertEqual(claudius.get_vida(),22)
      marcia.lutar_com(claudius)
      marcia.atacar()
      self.assertEqual(marcia.get_vida(),20)
      self.assertEqual(claudius.get_vida(),22-7)

   def test_03a_soco(self):
      marcia = Pessoa('marcia',20)
      claudius = Pessoa('claudius',22)
      self.assertEqual(claudius.get_vida(),22)
      marcia.lutar_com(claudius)
      marcia.selecionar_arma('soco')
      marcia.atacar()
      self.assertEqual(marcia.get_vida(),20)
      self.assertEqual(claudius.get_vida(),20)

   def test_03b_adaga(self):
      marcia = Pessoa('marcia',20)
      claudius = Pessoa('claudius',22)
      self.assertEqual(claudius.get_vida(),22)
      marcia.lutar_com(claudius)
      marcia.selecionar_arma('adaga')
      marcia.atacar()
      self.assertEqual(marcia.get_vida(),20)
      self.assertEqual(claudius.get_vida(),15)

   def test_03c_espada(self):
      marcia = Pessoa('marcia',20)
      claudius = Pessoa('claudius',22)
      self.assertEqual(claudius.get_vida(),22)
      marcia.lutar_com(claudius)
      marcia.selecionar_arma('espada')
      marcia.atacar()
      self.assertEqual(marcia.get_vida(),20)
      self.assertEqual(claudius.get_vida(),12)
   
   def test_03d_fogo(self):
      marcia = Pessoa('marcia',20)
      claudius = Pessoa('claudius',22)
      self.assertEqual(claudius.get_vida(),22)
      marcia.lutar_com(claudius)
      marcia.selecionar_arma('bola de fogo')
      marcia.atacar()
      self.assertEqual(claudius.get_vida(),12)
   
   def test_04_ate_a_morte(self):
      marcia = Pessoa('marcia',20)
      claudius = Pessoa('claudius',22)
      self.assertEqual(claudius.get_vida(),22)
      marcia.lutar_com(claudius)
      marcia.selecionar_arma('bola de fogo')
      marcia.atacar()
      self.assertEqual(claudius.get_vida(),12)
      marcia.atacar()
      self.assertEqual(claudius.get_vida(),2)
      marcia.atacar()
      self.assertEqual(claudius.get_vida(),0)

   def test_05_ataque_fogo_contra_mago(self):
      claudius = Pessoa('claudius',120)
      claudius.selecionar_arma('bola de fogo')
      morgana = Mago('morgana')
      claudius.lutar_com(morgana)
      claudius.atacar()#claudius atacou com dola de fogo. Morgana resiste 9 de dano e toma só um
      self.assertEqual(morgana.get_vida(),99)
   
   def test_06_mago_armas(self):
      morgana = Mago('morgana')
      claudius = Pessoa('claudius',120)
      
      
      morgana.lutar_com(claudius)
      morgana.atacar()#morgana atacou com bola de fogo por padrao.
      self.assertEqual(claudius.get_vida(),110)

      morgana.selecionar_arma('adaga')
      morgana.atacar()
      self.assertEqual(claudius.get_vida(),105)

      morgana.selecionar_arma('espada')
      morgana.atacar()
      self.assertEqual(claudius.get_vida(),105)

      morgana.selecionar_arma('soco')
      morgana.atacar()
      self.assertEqual(claudius.get_vida(),103)

    
   def test_07_magos_ate_a_morte(self):
       merlin = Mago('merlin',120)
       morgana = Mago('morgana',20)
       merlin.selecionar_arma('adaga')
       merlin.lutar_com(morgana)
       merlin.atacar()
       self.assertEqual(morgana.get_vida(),15)
       merlin.atacar()
       self.assertEqual(morgana.get_vida(),10)
       merlin.atacar()
       self.assertEqual(morgana.get_vida(),5)
       merlin.selecionar_arma('soco')
       merlin.atacar()
       self.assertEqual(morgana.get_vida(),3)
       merlin.atacar()
       self.assertEqual(morgana.get_vida(),1)
       merlin.atacar()
       self.assertEqual(morgana.get_vida(),0)
       merlin.atacar()
       self.assertEqual(morgana.get_vida(),0)

   def test_08_mago_contra_lutador_tipos_de_dano(self):
       merlin = Mago('merlin',120)
       arthur = Lutador('arthur',150)
       merlin.lutar_com(arthur)
       merlin.atacar()
       self.assertEqual(arthur.get_vida(),140)
       merlin.selecionar_arma('soco')
       merlin.atacar()
       self.assertEqual(arthur.get_vida(),139)
       merlin.selecionar_arma('adaga')
       merlin.atacar()
       self.assertEqual(arthur.get_vida(),134)

   def test_09_lutador_prefere_espada(self):
       arthur = Lutador('arthur',150)
       merlin = Mago('merlin',120)
       arthur.lutar_com(merlin)
       arthur.atacar()
       self.assertEqual(merlin.get_vida(),110)
       

   def test_10_lutador_contra_mago_tipos_de_dano(self):
       merlin = Mago('merlin',120)
       arthur = Lutador('arthur',150)
       arthur.lutar_com( merlin)
       arthur.atacar()
       self.assertEqual(merlin.get_vida(),110)
       arthur.selecionar_arma('bola de fogo')
       arthur.atacar()
       self.assertEqual(merlin.get_vida(),109)
       arthur.selecionar_arma('adaga')
       arthur.atacar()
       self.assertEqual(merlin.get_vida(),102)

   def test_11_mago_contra_barbaro_tipos_de_dano(self):
       merlin = Mago('merlin',120)
       conan = Barbaro('conan',200)
       merlin.lutar_com(conan)
       merlin.atacar()
       self.assertEqual(conan.get_vida(),190)
       merlin.selecionar_arma('soco')
       merlin.atacar()
       self.assertEqual(conan.get_vida(),188)
       merlin.selecionar_arma('adaga')
       merlin.atacar()
       self.assertEqual(conan.get_vida(),183)

   def test_12_barbaro_sem_dano_contra_mago(self):
       merlin = Mago('merlin',120)
       conan = Barbaro('conan',200)
       conan.lutar_com(merlin)
       conan.atacar()
       self.assertEqual(merlin.get_vida(),110)
       conan.selecionar_arma('adaga')
       conan.atacar()
       self.assertEqual(merlin.get_vida(),103)
       conan.selecionar_arma('soco')
       conan.atacar()
       self.assertEqual(merlin.get_vida(),101)
       conan.selecionar_arma('bola de fogo')
       conan.atacar()
       self.assertEqual(merlin.get_vida(),101)

   def test_13_barbaro_com_dano_contra_mago(self):
       merlin = Mago('merlin',120)
       conan = Barbaro('conan',200)
       merlin.lutar_com(conan)
       merlin.atacar()
       conan.lutar_com(merlin)
       conan.atacar()
       self.assertEqual(merlin.get_vida(),100)
       conan.selecionar_arma('adaga')
       conan.atacar()
       self.assertEqual(merlin.get_vida(),86)
       conan.selecionar_arma('soco')
       conan.atacar()
       self.assertEqual(merlin.get_vida(),82)
    
   def test_13a_barbaro_com_dano_contra_mago_2(self):
       merlin = Mago('merlin',120)
       conan = Barbaro('conan',200)
       merlin.lutar_com(conan)
       merlin.atacar() #barbaro dessa vez sofre 2 ataques
       conan.lutar_com(merlin)
       conan.atacar()
       self.assertEqual(merlin.get_vida(),100)
       merlin.atacar() #segundo ataque que o barbaro sofre
       conan.atacar()
       self.assertEqual(merlin.get_vida(),80) #o dano da espada nao pode dobrar 2 vezes

    
   def test_14a_lutador_atacando_com_fogo(self):
       merlin = Mago('merlin',120)
       arthur = Lutador('arthur',150)
       arthur.lutar_com( merlin)
       arthur.selecionar_arma('bola de fogo')
       arthur.atacar()
       self.assertEqual(arthur.get_vida(),130)
    
   def test_14b_barbaro_atacando_com_fogo(self):
       merlin = Mago('merlin',120)
       conan = Barbaro('conan',200)
       conan.lutar_com( merlin)
       conan.selecionar_arma('bola de fogo')
       conan.atacar()
       self.assertEqual(conan.get_vida(),180)
       conan.atacar()
       self.assertEqual(conan.get_vida(),160)
       self.assertEqual(merlin.get_vida(),120)
    
   def test_15a_curar(self):
       merlin = Mago('merlin',120)
       conan = Barbaro('conan',200)
       arthur= Lutador('Arthur',150)
       conan.lutar_com(merlin)
       arthur.lutar_com(conan)
       merlin.lutar_com(arthur)
       conan.atacar()
       arthur.atacar()
       merlin.atacar()
       self.assertTrue(conan.get_vida() < 200)
       self.assertTrue(arthur.get_vida() < 150)
       self.assertTrue(merlin.get_vida() < 120)
       conan.curar()
       self.assertEqual(conan.get_vida(),200)
       arthur.curar()
       self.assertEqual(arthur.get_vida(),150)
       merlin.curar()
       self.assertEqual(merlin.get_vida(),120)

   def test_15b_barbaro_curado_da_menos_dano(self):
       merlin = Mago('merlin',120)
       conan = Barbaro('conan',200)
       conan.lutar_com(merlin)
       merlin.lutar_com(conan)
       merlin.atacar()
       conan.atacar()
       self.assertEqual(merlin.get_vida(),100)
       conan.curar()
       conan.atacar()
       self.assertEqual(merlin.get_vida(),90)

   def test_16_veneno(self):
       merlin = Mago('merlin',120)
       merlin.envenenar()
       conan = Barbaro('conan',200)
       merlin.lutar_com(conan)
       merlin.atacar()
       self.assertEqual(merlin.get_vida(),110)#merlin tomou o dano do veneno
       merlin.atacar()
       self.assertEqual(merlin.get_vida(),100)
    
   def test_17_antidoto(self):
       merlin = Mago('merlin',120)
       merlin.envenenar()
       conan = Barbaro('conan',200)
       merlin.lutar_com(conan)
       merlin.atacar()
       self.assertEqual(merlin.get_vida(),110)#merlin tomou o dano do veneno
       merlin.atacar()
       self.assertEqual(merlin.get_vida(),100)
       merlin.tomar_antidoto()#sem mais dano
       merlin.atacar()
       self.assertEqual(merlin.get_vida(),100)
    
   def test_18_veneno_para_barbaro(self):
       merlin = Mago('merlin',120)
       conan = Barbaro('conan',200)
       conan.envenenar()
       conan.lutar_com(merlin)
       conan.atacar()
       self.assertEqual(conan.get_vida(),200)#conan nao tomou o dano do veneno
       conan.atacar()
       self.assertEqual(conan.get_vida(),200)#idem


def runTests():
            suite = unittest.defaultTestLoader.loadTestsFromTestCase(TesteLutas)
            unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)

runTests()