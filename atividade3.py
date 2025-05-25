class Cliente:
    def __init__(self, nome, senha, email, plano):
        self.nome = nome
        self.senha = senha
        self.email = email
        self.lista_planos = ["básico", "premium"]
        if plano in self.lista_planos:
            self.plano = plano
        else:
            raise Exception("plano inválido")

    def muda_plano(self, novo_plano):
        if novo_plano in self.lista_planos:
            self.plano = novo_plano
        else:
            print("plano inválido")

    def ver_filme(self, filme, plano_filme):
        if self.plano == plano_filme:
            print(f"Filme {filme} disponível em baixa qualidade")
        elif self.plano == "premium":
            print(f"Filme {filme} disponível em qualidade alta")
        elif self.plano == "básico" and plano_filme == "premium":
            print("Faça atualização para o Premium")
        else:
            print("Filme inválido")