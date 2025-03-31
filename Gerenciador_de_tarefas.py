import tkinter as tk

def criar_tarefa_ui():
    descricao = descricao_entry.get()
    criar_tarefa(tarefas, descricao)
    atualizar_lista_tarefas()

def atualizar_lista_tarefas():
    lista_pendentes.delete(0, tk.END)
    lista_concluidas.delete(0, tk.END)
    for tarefa in tarefas:
        if tarefa["status"] == "pendente":
            lista_pendentes.insert(tk.END, f"[ ] {tarefa['descricao']}")
        else:
            lista_concluidas.insert(tk.END, f"[X] {tarefa['descricao']}")

def criar_tarefa(tarefas, descricao):
    tarefa = {"descricao": descricao, "status": "pendente"}
    tarefas.append(tarefa)
    return tarefas

def visualizar_tarefas(tarefas):
    return [
        f"[{'X' if tarefa['status'] == 'concluida' else ' '}] {tarefa['descricao']}"
        for tarefa in tarefas
    ]

def excluir_tarefa_ui():
        indice_selecionado = lista_pendentes.curselection()
        if indice_selecionado:
            indice = indice_selecionado[0]
            descricao_tarefa = lista_pendentes.get(indice).split("] ")[1]
            for i, tarefa in enumerate(tarefas):
                if tarefa["descricao"] == descricao_tarefa and tarefa["status"] == "pendente":
                    excluir_tarefa(tarefas, i)
                    break
            atualizar_lista_tarefas()

def concluir_tarefa_ui():
    indice_selecionado = lista_pendentes.curselection()
    if indice_selecionado:
        indice = indice_selecionado[0]
        descricao_tarefa = lista_pendentes.get(indice).split("] ")[1]
        for i, tarefa in enumerate(tarefas):
            if tarefa["descricao"] == descricao_tarefa and tarefa["status"] == "pendente":
                atualizar_tarefa(i, status="concluida")
                break
        atualizar_lista_tarefas()

#Início do código da lista de tarefas:

def criar_atualizador_tarefa(tarefas):
    def atualizar_tarefa(indice, status=None, descricao=None):
        try:
            if 0 <= indice < len(tarefas):
                if status:
                    tarefas[indice]["status"] = status
                if descricao:
                    tarefas[indice]["descricao"] = descricao
            else:
                raise IndexError("Índice de tarefa inválido.")
        except IndexError as e:
            print(f"Erro ao atualizar tarefa: {e}")
        return tarefas
    return atualizar_tarefa

def excluir_tarefa(tarefas, indice):
    try:
        if 0 <= indice < len(tarefas):
            del tarefas[indice]
        else:
            raise IndexError("Índice de tarefa inválido.")
    except IndexError as e:
        print(f"Erro ao excluir tarefa: {e}")
    return tarefas

def filtrar_tarefas(tarefas, status):
    return list(filter(lambda tarefa: tarefa["status"] == status, tarefas))

def aplicar_funcao_tarefas(tarefas, funcao):
    return [funcao(tarefa) for tarefa in tarefas]

# Exemplo de uso
tarefas = []
tarefas = criar_tarefa(tarefas, "Comprar pão")
tarefas = criar_tarefa(tarefas, "Agendar consulta com o dentista")
tarefas = criar_tarefa(tarefas, "Enviar o e-mail com o relatório semanal")
tarefas = criar_tarefa(tarefas, "Fazer compras no mercado")
tarefas = criar_tarefa(tarefas, "Pagar a fatura do cartão")
print(visualizar_tarefas(tarefas))

atualizar_tarefa = criar_atualizador_tarefa(tarefas)
tarefas = atualizar_tarefa(0, status="concluida")
tarefas = atualizar_tarefa(2, status="concluida")
print(visualizar_tarefas(tarefas))

tarefas = excluir_tarefa(tarefas, 1)
print(visualizar_tarefas(tarefas))

tarefas_concluidas = filtrar_tarefas(tarefas, "concluida")
print(visualizar_tarefas(tarefas_concluidas))

def formatar_tarefa_resumida(tarefa):
    return tarefa['descricao']

def formatar_tarefa(tarefa):
    return f"{tarefa['descricao']} - {tarefa['status']}"

tarefas_resumidas = aplicar_funcao_tarefas(tarefas, formatar_tarefa_resumida)
print(tarefas_resumidas)

tarefas_formatadas = aplicar_funcao_tarefas(tarefas, formatar_tarefa)
print(tarefas_formatadas)

# Testes adicionais

# Teste de atualização com índice inválido
print("\n--- Teste de atualização com índice inválido ---")
tarefas_atualizadas = atualizar_tarefa(10, status="concluida")
print(tarefas_atualizadas)

# Teste de exclusão com índice inválido
print("\n--- Teste de exclusão com índice inválido ---")
tarefas_excluidas = excluir_tarefa(tarefas, 10)
print(tarefas_excluidas)

# Teste de filtragem sem tarefas com o status especificado
print("\n--- Teste de filtragem sem tarefas com status inexistente ---")
tarefas_canceladas = filtrar_tarefas(tarefas, "cancelada")
print(tarefas_canceladas)

# Teste de criação de tarefas com descrições longas e caracteres especiais
print("\n--- Teste de criação com descrições longas e caracteres especiais ---")
tarefas = criar_tarefa(tarefas, "Tarefa com descrição muito longa e caracteres especiais: !@#$%^&*()")
print(visualizar_tarefas(tarefas))

# Teste da função aplicar_funcao_tarefas com função de formatação complexa
print("\n--- Teste de aplicar_funcao_tarefas com formatação complexa ---")
def formatar_tarefa_complexa(tarefa):
    return f"Tarefa: {tarefa['descricao']} - Status: {tarefa['status'].upper()}"

tarefas_complexas = aplicar_funcao_tarefas(tarefas, formatar_tarefa_complexa)
print(tarefas_complexas)

# Teste de atualização com índice inválido
print("\n--- Teste de atualização com índice inválido ---")
tarefas = atualizar_tarefa(10, status="concluida")
print(tarefas)

# Teste de exclusão com índice inválido
print("\n--- Teste de exclusão com índice inválido ---")
tarefas = excluir_tarefa(tarefas, 10)
print(tarefas)

# Interface gráfica
janela = tk.Tk()
janela.title("Gerenciador de Tarefas")

descricao_label = tk.Label(janela, text="Descrição:")
descricao_label.pack()

descricao_entry = tk.Entry(janela)
descricao_entry.pack()

criar_button = tk.Button(janela, text="Criar Tarefa", command=criar_tarefa_ui)
criar_button.pack()

pendentes_label = tk.Label(janela, text="Tarefas Pendentes:")
pendentes_label.pack()

lista_pendentes = tk.Listbox(janela, width=60, height=10)
lista_pendentes.pack()

concluidas_label = tk.Label(janela, text="Tarefas Concluídas:")
concluidas_label.pack()

lista_concluidas = tk.Listbox(janela, width=60, height=10)
lista_concluidas.pack()

concluir_button = tk.Button(janela, text="Concluir Tarefa", command=concluir_tarefa_ui)
concluir_button.pack()

excluir_button = tk.Button(janela, text="Excluir Tarefa", command=excluir_tarefa_ui)
excluir_button.pack()

atualizar_lista_tarefas()

janela.mainloop()