import tkinter as tk
from tkinter import ttk
import dados

def abrir_consulta():

    janela = tk.Toplevel()
    janela.title("Consulta")

    tabela = ttk.Treeview(
        janela,
        columns=("Nome","Preco","Quantidade"),
        show="headings"
    )

    tabela.heading("Nome",text="Nome")
    tabela.heading("Preco",text="Preço")
    tabela.heading("Quantidade",text="Quantidade")

    tabela.pack(fill="both", expand=True)

    for _, linha in dados.produtos.iterrows():

        tabela.insert(
            "",
            "end",
            values=(
                linha["Nome"],
                linha["Preco"],
                linha["Quantidade"]
            )
        )