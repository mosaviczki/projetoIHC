class Aeronave:
    def __init__(self) -> None:
        self.codigoAviao = "PT-GHE"
        self.modelo = "Embraer E-195"
        self.qtdAssento = 120
        self.qtdAssentoEspecial = 16
        self.qtdAssentoTotal = self.qtdAssento + self.qtdAssentoEspecial

    def incluir(self, assentoComprado ):
        self.qtdAssentoTotal -= assentoComprado 
        
    def excluir(self, exclusaoAssentoComprado):
        self.qtdAssentoTotal += exclusaoAssentoComprado

class Voo:
    def __init__(self) -> None:
        self.codigoVoo = "84920498"
        self.dataPartida = "25/02/2023"
        self.valorPassagem = 450
        self.aviao = Aeronave()
    
    def calcularOcupacao(self, assentosOcupados):
        self.assentosOcupados = assentosOcupados
        self.ocupacao = self.aviao.qtdAssentoTotal - self.assentosOcupados
        self.ocupacaoPorcentagem = ((self.ocupacao*100)/self.aviao.qtdAssentoTotal)
    
    def alterar(self):
        alt = input("1 - Alterar data de voo \n 2 - Alterar preço ")
        if alt == 1:
            data = input("Informe nova data: ")
            self.dataPartida = data
        elif alt == 2:
            preco = input("Informe novo preco: ")
            self.valorPassagem = preco
        else:
            print("Entrada invalida!")

    @property
    def __str__(self):
       print(f'==========RELATORIO VOO ==========\n'
             f'Ocupação: {self.ocupacaoPorcentagem:.2f}%\n'
             f'Capacidade máxima: {self.aviao.qtdAssentoTotal}\n'
             f'Cadeiras ocupadas: {self.assentosOcupados}\n')