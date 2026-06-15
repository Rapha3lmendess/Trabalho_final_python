import tkinter as tk
from tkinter import messagebox
import dados

def abrir_atualizar():

    janela = tk.Toplevel()
    janela.title("Atualizar Produto")
    janela.geometry("500x400")
    janela.resizable(False, False)

    tk.Label(
        janela,
        text="Atualização de Produtos",
        font=("Arial", 18, "bold")
    ).pack(pady=20)

    tk.Label(
        janela,
        text="Nome do Produto",
        font=("Arial", 12)
    ).pack(pady=5)

    nome = tk.Entry(janela, width=35)
    nome.pack(pady=5)

    tk.Label(
        janela,
        text="Novo Preço",
        font=("Arial", 12)
    ).pack(pady=5)

    preco = tk.Entry(janela, width=35)
    preco.pack(pady=5)

    tk.Label(
        janela,
        text="Nova Quantidade",
        font=("Arial", 12)
    ).pack(pady=5)

    quantidade = tk.Entry(janela, width=35)
    quantidade.pack(pady=5)

    def atualizar():

        produto = nome.get()

        if not produto or not preco.get() or not quantidade.get():
            messagebox.showerror(
                "Erro",
                "Preencha todos os campos!"
            )
            return

        try:

            if produto in dados.produtos["Nome"].values:

                dados.produtos.loc[
                    dados.produtos["Nome"] == produto,
                    "Preco"
                ] = float(preco.get())

                dados.produtos.loc[
                    dados.produtos["Nome"] == produto,
                    "Quantidade"
                ] = int(quantidade.get())

                messagebox.showinfo(
                    "Sucesso",
                    "Produto atualizado!"
                )

                nome.delete(0, tk.END)
                preco.delete(0, tk.END)
                quantidade.delete(0, tk.END)

            else:

                messagebox.showerror(
                    "Erro",
                    "Produto não encontrado!"
                )

        except ValueError:

            messagebox.showerror(
                "Erro",
                "Digite valores válidos!"
            )

    tk.Button(
        janela,
        text="Atualizar Produto",
        width=20,
        height=2,
        command=atualizar
    ).pack(pady=20)