# tests/test_crud.py
import unittest
# Importar as funções do seu app.py (assumindo que app.py está na raiz)
from app import criar_tarefa, listar_tarefas, atualizar_tarefa, remover_tarefa, tarefas, id_atual

class TestCrudTarefas(unittest.TestCase):

    def setUp(self):
        # Limpa a lista de tarefas e reseta o ID antes de cada teste
        # Isso garante que cada teste comece com um estado limpo
        global tarefas, id_atual
        tarefas = []
        id_atual = 1

    def test_criar_tarefa(self):
        criar_tarefa("Tarefa Teste", "Descrição Teste", "Baixa")
        self.assertEqual(len(tarefas), 1)
        self.assertEqual(tarefas[0]['titulo'], "Tarefa Teste")
        self.assertEqual(tarefas[0]['id'], 1)

        criar_tarefa("Outra Tarefa", "Detalhe", "Alta")
        self.assertEqual(len(tarefas), 2)
        self.assertEqual(tarefas[1]['id'], 2)

    def test_listar_tarefas(self):
        # Testa com lista vazia
        self.assertEqual(listar_tarefas(), None) # A função printa, mas retorna None

        criar_tarefa("Tarefa 1", "Desc1", "Média")
        criar_tarefa("Tarefa 2", "Desc2", "Alta")
        # Para testar o print, você precisaria de output capturing,
        # mas podemos testar o estado da lista interna
        import io
        from unittest.mock import patch

        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            listar_tarefas()
            output = fake_stdout.getvalue()
            self.assertIn("Tarefa 1", output)
            self.assertIn("Tarefa 2", output)
            self.assertIn("Lista de Tarefas:", output)

    def test_atualizar_tarefa(self):
        criar_tarefa("Tarefa Velha", "Desc Velha", "Baixa")
        atualizar_tarefa(1, "Tarefa Nova", "Desc Nova", "Alta")
        self.assertEqual(tarefas[0]['titulo'], "Tarefa Nova")
        self.assertEqual(tarefas[0]['descricao'], "Desc Nova")
        self.assertEqual(tarefas[0]['prioridade'], "Alta")

        # Testa atualização de ID inexistente
        import io
        from unittest.mock import patch
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            atualizar_tarefa(99, "Inexistente", "", "")
            output = fake_stdout.getvalue()
            self.assertIn("Tarefa ID 99 não encontrada.", output)

    def test_remover_tarefa(self):
        criar_tarefa("Tarefa A", "Desc A", "Alta")
        criar_tarefa("Tarefa B", "Desc B", "Média")
        remover_tarefa(1)
        self.assertEqual(len(tarefas), 1)
        self.assertEqual(tarefas[0]['titulo'], "Tarefa B") # Verifica se a correta foi removida

        remover_tarefa(99) # Tenta remover tarefa inexistente (não deve dar erro)
        self.assertEqual(len(tarefas), 1)

if __name__ == '__main__':
    unittest.main()