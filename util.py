import os

class Utils:
    
    CORES = {
        'vermelho': '\033[91m',
        'verde': '\033[92m',
        'amarelo': '\033[93m',
        'azul': '\033[94m',
        'magenta': '\033[95m',
        'ciano': '\033[96m',
        'branco': '\033[97m',
        "cinza": "\033[90m",
        "vermelho_claro": "\033[91m",
        "verde_claro": "\033[92m",
        "amarelo_claro": "\033[93m",
        "azul_claro": "\033[94m",
        "magenta_claro": "\033[95m",
        "ciano_claro": "\033[96m",
        "branco_brilhante": "\033[97m",
        
        'reset': '\033[0m',
        'negrito': '\033[1m',
        'sublinhado': '\033[4m'
    }    
    
    def limpar_tela():
        os.system('cls' if os.name == 'nt' else 'clear')

    def pinta(texto, cor):
        cod_cor = Utils.CORES.get(cor, Utils.CORES['reset'] )
        return f"{cod_cor}{texto}{Utils.CORES['reset']}"
    
    
        
    