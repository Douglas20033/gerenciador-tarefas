# app.py
# Adicionando campo de data de criacao

tarefas = []
id_atual = 1

def criar_tarefa(titulo, descricao, prioridade):
    global id_atual
    tarefa = {
        'id': id_atual,
        'titulo': titulo,
        'descricao': descricao,
        'prioridade': prioridade
    }
    tarefas.append(tarefa)
    print(f"Tarefa criada: {titulo}")
    id_atual += 1

def listar_tarefas():
    print("\n📋 Lista de Tarefas:")
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
    for tarefa in tarefas:
        print(f"ID: {tarefa['id']}, Título: {tarefa['titulo']}, Prioridade: {tarefa['prioridade']}")

def atualizar_tarefa(id_tarefa, novo_titulo, nova_descricao, nova_prioridade):
    for tarefa in tarefas:
        if tarefa['id'] == id_tarefa:
            tarefa['titulo'] = novo_titulo
            tarefa['descricao'] = nova_descricao
            tarefa['prioridade'] = nova_prioridade
            print(f"Tarefa ID {id_tarefa} atualizada com sucesso.")
            return
    print(f"Tarefa ID {id_tarefa} não encontrada.")

def remover_tarefa(id_tarefa):
    global tarefas
    tarefas = [t for t in tarefas if t['id'] != id_tarefa]
    print(f"Tarefa ID {id_tarefa} removida.")

# -------- Exemplo de uso --------
if __name__ == "__main__":
    criar_tarefa("Estudar Python", "Fazer exercícios", "Alta")
    criar_tarefa("Revisar README", "Melhorar descrição do projeto", "Média")

    listar_tarefas()

    atualizar_tarefa(1, "Estudar Python Avançado", "Fazer projeto CRUD", "Alta")
    remover_tarefa(2)

    listar_tarefas()
