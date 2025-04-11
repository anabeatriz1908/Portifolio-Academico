import requests
import unittest


class TestStringMethods(unittest.TestCase):
    def test_alunos_read_alunos_01(self):
        r = requests.get('http://localhost:5036/alunos')
        self.assertEqual(r.status_code,200)
        
        
    def test_alunos_read_aluno_por_id_02(self):
        r = requests.post('http://localhost:5036/alunos',json={
            "id": 93,
            "nome": "Jonas Adalberto",
            "idade": 47, 
            "turma_id": 310, 
            "data_nascimento": "27/03/1979", 
            "nota_primeiro_semestre": 8.4, 
            "nota_segundo_semestre": 9.2
        })
        resposta = requests.get('http://localhost:5036/alunos/93')
        self.assertEqual(resposta.status_code,200)
        dict_retornado = resposta.json() 
        self.assertEqual(type(dict_retornado),dict)
        self.assertIn("nome",dict_retornado)
        self.assertEqual(dict_retornado["nome"], "Jonas Adalberto")


    def test_alunos_update_03(self):

        r_reset = requests.delete('http://localhost:5036/alunos')
        self.assertEqual(r_reset.status_code,200)

        r_post = requests.post('http://localhost:5036/alunos',json={
            "id": 87, 
            "nome": "Cícero", 
            "idade": 47, 
            "turma_id": 310, 
            "data_nascimento": "26/03/1978", 
            "nota_primeiro_semestre": 8.4, 
            "nota_segundo_semestre": 9.2
        })

        self.assertEqual(r_post.status_code, 200, f"Erro ao criar aluno: {r_post.text}")

        r_antes = requests.get('http://localhost:5036/alunos/87')
        self.assertEqual(r_antes.status_code,200)
        requests.put('http://localhost:5036/alunos/87', json={ "nome": "Cícero Gonçalves"})

        r_depois = requests.get('http://localhost:5036/alunos/87')
        self.assertEqual(r_depois.json()["nome"],"Cícero Gonçalves")


    def test_alunos_deleta_todos_alunos_04(self):
        r = requests.post('http://localhost:5036/alunos',json={
            "id": 87, 
            "nome": "Cícero Gonçalves", 
            "idade": 47, 
            "turma_id": 310, 
            "data_nascimento": "26/03/1978", 
            "nota_primeiro_semestre": 8.4, 
            "nota_segundo_semestre": 9.2
        })
        r_lista = requests.get('http://localhost:5036/alunos')
        r_reset = requests.delete('http://localhost:5036/alunos')
        self.assertEqual(r_reset.status_code,200)

        r_lista_depois = requests.get('http://localhost:5036/alunos')
        self.assertEqual(len(r_lista_depois.json()),0)


    def test_alunos_deleta_por_id_05(self):

        r_reset = requests.delete('http://localhost:5036/alunos')
        self.assertEqual(r_reset.status_code,200)

        requests.post('http://localhost:5036/alunos',json={
            "id": 87, 
            "nome": "Cícero Gonçalves", 
            "idade": 47, "turma_id": 310, 
            "data_nascimento": "26/03/1978", 
            "nota_primeiro_semestre": 8.4, 
            "nota_segundo_semestre": 9.2
        })
        r_lista = requests.get('http://localhost:5036/alunos')
        lista_retornada = r_lista.json()
        self.assertEqual(len(lista_retornada),1)

        requests.delete('http://localhost:5036/alunos/87')
        self.assertEqual(r_reset.status_code,200)

        r_lista2 = requests.get('http://localhost:5036/alunos')
        self.assertEqual(r_lista2.status_code,200)

def runTests():
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
        unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)


if __name__ == '__main__':
    runTests()