class Produto:
    def __init__(self,
                 chave: str,
                 codigo: str,
                 nome: str,
                 icms: str,
                 ipi: str,
                 pis: str,
                 cofins: str,
                 tributo: str,
                 valor: str) -> None:
        self.chave = chave
        self.codigo = codigo
        self.nome = nome
        self.icms = icms
        self.ipi = ipi
        self.pis = pis
        self.cofins = cofins
        self.tributo = tributo
        self.valor = valor
        