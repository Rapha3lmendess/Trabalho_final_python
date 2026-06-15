import tkinter as tk
from tkinter import messagebox
import dados

def abrir_excluir():

    janela = tk.Toplevel()
    janela.title("Excluir")

    tk.Label(
        janela,
        text="Nome do Produto"
    ).pack()

    nome = tk.Entry(janela)
    nome.pack()

    def excluir():

        produto = nome.get()

        if produto in dados.produtos["Nome"].values:

            dados.produtos = dados.produtos[
                dados.produtos["Nome"] != produto
            ]

            messagebox.showinfo(
                "Sucesso",
                "Produto removido!"
            )

        else:

            messagebox.showerror(
                "Erro",
                "Produto não encontrado!"
            )

    tk.Button(
        janela,
        text="Excluir",
        command=excluir
    ).pack(pady=10)