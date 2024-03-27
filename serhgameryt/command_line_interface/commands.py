"""# Libary for SerhGamerYt
\n
 - Components/Cli/Commands"""
import os

class Arquivo:
    "# Classe do Arquivo"
    def __init__(self) -> None:
        super().__init__()
    
    def criar(nome,extensao) -> str:
        "# Crie um Arquivo\nNome -> Name • Extensão -> Extension"
        arquivo = "{}.{}".format(nome,extensao)
        with open(f"{arquivo}","x") as criado:
            pass
        return "[ARQUIVO] Logger.FileCreate"

    def deletar(arquivo) -> str:
        "# Delete um Arquivo\nArquivo -> File"
        os.remove(arquivo)
        return "[ARQUIVO] Logger.DeleteCreate"
