import json  # lidar com arquivo JSON 
from pathlib import Path # lidar com caminhos do WIN

class BancoFake:
    
    def __init__(self, arquivo_db="banco.json"):
        self.arquivo_db = arquivo_db
        self.dados = {"clientes": [], "produtos": []}
        self._carregar()
        
    def _carregar(self):
        """ 
        Carrega dados do arquivo json, se existir.
        caso não exista, inicia com dados vazios
        """
        caminho = Path(self.arquivo_db)
        if caminho.is_file():
            # abrindo arquivo no modo leitura em utf-8 (PT-BR)
            with open(caminho, "r", encoding="utf-8") as data:
                # salvando dados que ja existem no arquivo 
                # na variavel dados 
                self.dados = json.load(data)
        else:
            self._salvar()
            
    def _salvar(self):
        """
        Salvar o conteúdo de self. dados no arquivo json 
        """
        with open(self.arquivo_db, 'w', encoding="utf-8") as data:
            # realizando DUMP (Python para json) para salvar no banco 
            json.dump(self.dados, data, ensure_ascii=False, indent=4)   
            
    def adicionar_cliente(self, cliente_dict):
        self.dados["clientes"].append(cliente_dict)
        self._salvar()
        
    def listar_clientes(self):
        return self.dados["clientes"]