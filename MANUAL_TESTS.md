# Plano de Testes Manuais - Gerenciador de Tarefas

Este documento descreve os testes manuais a serem executados para verificar as funcionalidades básicas do sistema.

## Cenários de Teste

### Cenário 1: Criação de Nova Tarefa
1.  Abrir o arquivo `app.py` e executá-lo (no terminal: `python app.py`).
2.  Verificar no console se a mensagem "Tarefa criada: [Título da Tarefa]" aparece para cada tarefa adicionada no exemplo de uso (`criar_tarefa`).
3.  Verificar se a lista de tarefas exibida (`listar_tarefas()`) inclui as tarefas recém-criadas.

### Cenário 2: Atualização de Tarefa Existente
1.  Executar o `app.py`.
2.  Observar a mensagem de "Tarefa ID X atualizada com sucesso." para a tarefa que foi atualizada.
3.  Verificar na lista final de tarefas se o título, descrição e prioridade da tarefa foram alterados corretamente.

### Cenário 3: Exclusão de Tarefa
1.  Executar o `app.py`.
2.  Observar a mensagem de "Tarefa ID X removida." para a tarefa que foi excluída.
3.  Verificar na lista final de tarefas se a tarefa com o ID removido não aparece mais.

### Cenário 4: Lista de Tarefas Vazia
1.  Comentar (ou remover) todas as chamadas de `criar_tarefa`, `atualizar_tarefa`, `remover_tarefa` no `if __name__ == "__main__":` do `app.py`.
2.  Deixar apenas `listar_tarefas()` no bloco `if __name__ == "__main__":`.
3.  Executar o `app.py`.
4.  Verificar se a mensagem "Nenhuma tarefa cadastrada." é exibida.