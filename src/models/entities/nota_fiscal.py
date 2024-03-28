class NotaFiscal:
    def __init__(self,
                 chave: str,
                 numero: str,
                 status: str,
                 nomeEmit: str,
                 cnpjEmit: str,
                 nomeDest: str,
                 cnpjDest: str,
                 icms: str,
                 valor: str) -> None:
        self.chave = chave
        self.numero = numero
        self.status = status
        self.nomeEmit = nomeEmit
        self.cnpjEmit = cnpjEmit
        self.nomeDest = nomeDest
        self.cnpjDest = cnpjDest
        self.icms = icms
        self.valor = valor
    