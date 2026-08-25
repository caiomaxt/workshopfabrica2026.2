class produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque


    def adicionar_estoque(self, quantidade):
        self.estoque += quantidade
        print(f"Adicionado {quantidade} unidades de {self.nome}. Estoque atual: {self.estoque}")

    def valor_total_em_estoque(self):
        return self.preco * self.estoque

class produto_perecivel(produto):
    def __init__(self, nome, preco, estoque, validade):
        super().__init__(nome, preco, estoque)
        self.validade = validade

    def verificar_validade(self):
        print(f"O produto {self.nome} tem validade até {self.validade}.")


arroz = produto("Arroz", 5.0, 100)
cafe = produto("Café", 10.0, 50)
leite = produto_perecivel("Leite", 3.0, 30, "2023-12-31")

leite.verificar_validade()

arroz.adicionar_estoque(20)
total_arroz = arroz.valor_total_em_estoque()
print(f"Valor total em estoque de {arroz.nome}: R${total_arroz:.2f}")

cafe.adicionar_estoque(10)
total_cafe = cafe.valor_total_em_estoque()
print(f"Valor total em estoque de {cafe.nome}: R${total_cafe:.2f}")
