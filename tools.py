import random


class Tools():
    def __init__(self):
        self.choosenWord = None
        self.words = [
            {"word": "processador", "tip": "Unidade central de processamento de um computador"},
            {"word": "memória", "tip": "Armazena dados temporariamente para acesso rápido"},
            {"word": "placa-mãe", "tip": "Componente principal que conecta todos os dispositivos"},
            {"word": "monitor", "tip": "Dispositivo de saída de vídeo"},
            {"word": "teclado", "tip": "Dispositivo de entrada para digitação"},
            {"word": "mouse", "tip": "Dispositivo de entrada para apontar e clicar"},
            {"word": "impressora", "tip": "Dispositivo para imprimir documentos"},
            {"word": "ssd", "tip": "Unidade de armazenamento de estado sólido"},
            {"word": "hd", "tip": "Disco rígido para armazenamento de dados"},
            {"word": "gabinete", "tip": "Estrutura que abriga os componentes do computador"},
            {"word": "fonte", "tip": "Fonte de alimentação do computador"},
            {"word": "cooler", "tip": "Dispositivo para resfriamento de componentes"},
            {"word": "usb", "tip": "Porta de conexão universal para periféricos"},
            {"word": "ethernet", "tip": "Tecnologia de rede cabeada"},
            {"word": "wifi", "tip": "Tecnologia de rede sem fio"},
            {"word": "bluetooth", "tip": "Comunicação sem fio de curto alcance"},
            {"word": "firewall", "tip": "Sistema de proteção de rede"},
            {"word": "antivírus", "tip": "Software de proteção contra malware"},
            {"word": "backup", "tip": "Cópia de segurança de dados"},
            {"word": "cloud", "tip": "Armazenamento e serviços na nuvem"},
            {"word": "linux", "tip": "Sistema operacional de código aberto"},
            {"word": "windows", "tip": "Sistema operacional da Microsoft"},
            {"word": "macos", "tip": "Sistema operacional da Apple"},
            {"word": "android", "tip": "Sistema operacional para dispositivos móveis"},
            {"word": "ios", "tip": "Sistema operacional móvel da Apple"},
            {"word": "router", "tip": "Dispositivo que direciona o tráfego de rede"},
            {"word": "switch", "tip": "Dispositivo que conecta vários computadores em rede"},
            {"word": "servidor", "tip": "Computador dedicado a fornecer serviços"},
            {"word": "cliente", "tip": "Computador que acessa serviços de um servidor"},
            {"word": "programa", "tip": "Conjunto de instruções executáveis"},
            {"word": "aplicativo", "tip": "Software para realizar tarefas específicas"},
            {"word": "banco de dados", "tip": "Sistema para armazenar e gerenciar dados"},
            {"word": "sql", "tip": "Linguagem de consulta para bancos de dados"},
            {"word": "python", "tip": "Linguagem de programação popular"},
            {"word": "java", "tip": "Linguagem de programação multiplataforma"},
            {"word": "javascript", "tip": "Linguagem de programação para web"},
            {"word": "html", "tip": "Linguagem de marcação para páginas web"},
            {"word": "css", "tip": "Folhas de estilo para páginas web"},
            {"word": "php", "tip": "Linguagem de programação para web"},
            {"word": "git", "tip": "Sistema de controle de versões"},
            {"word": "github", "tip": "Plataforma de hospedagem de código"},
            {"word": "terminal", "tip": "Interface de linha de comando"},
            {"word": "console", "tip": "Interface para comandos de texto"},
            {"word": "rede", "tip": "Conjunto de computadores conectados"},
            {"word": "vpn", "tip": "Rede privada virtual"},
            {"word": "domínio", "tip": "Nome que identifica um site na internet"},
            {"word": "url", "tip": "Endereço de um recurso na web"},
            {"word": "cookie", "tip": "Arquivo de dados armazenado pelo navegador"},
            {"word": "cache", "tip": "Memória de acesso rápido"},
            {"word": "driver", "tip": "Software que permite comunicação com hardware"},
            {"word": "interface", "tip": "Meio de interação entre sistemas"},
            {"word": "compilador", "tip": "Programa que traduz código fonte"},
            {"word": "framework", "tip": "Estrutura para desenvolvimento de software"},
            {"word": "api", "tip": "Interface de programação de aplicativos"},
            {"word": "algoritmo", "tip": "Sequência de passos para resolver um problema"},
            {"word": "array", "tip": "Estrutura de dados para armazenar elementos"},
            {"word": "variável", "tip": "Espaço para armazenar valores"},
            {"word": "função", "tip": "Bloco de código reutilizável"},
            {"word": "classe", "tip": "Estrutura para criar objetos"},
            {"word": "objeto", "tip": "Instância de uma classe"},
            {"word": "método", "tip": "Função associada a uma classe"},
            {"word": "herança", "tip": "Reutilização de código entre classes"},
            {"word": "polimorfismo", "tip": "Capacidade de objetos assumirem diferentes formas"},
            {"word": "encapsulamento", "tip": "Ocultação de detalhes internos"},
            {"word": "debug", "tip": "Processo de encontrar e corrigir erros"},
            {"word": "exception", "tip": "Erro detectado durante a execução"},
            {"word": "thread", "tip": "Fluxo de execução paralelo"},
            {"word": "processo", "tip": "Programa em execução"},
            {"word": "sistema operacional", "tip": "Software que gerencia recursos do computador"},
            {"word": "virtualização", "tip": "Execução de sistemas em ambientes simulados"},
            {"word": "docker", "tip": "Plataforma de containers"},
            {"word": "container", "tip": "Ambiente isolado para execução de aplicações"},
            {"word": "cloud computing", "tip": "Computação em nuvem"},
            {"word": "machine learning", "tip": "Aprendizado de máquina"},
            {"word": "inteligência artificial", "tip": "Simulação de inteligência humana"},
            {"word": "big data", "tip": "Grande volume de dados"},
            {"word": "data science", "tip": "Ciência de dados"},
            {"word": "segurança", "tip": "Proteção de sistemas e dados"},
            {"word": "criptografia", "tip": "Técnica de proteção de informações"},
            {"word": "token", "tip": "Elemento de autenticação"},
            {"word": "login", "tip": "Acesso a sistemas"},
            {"word": "senha", "tip": "Código secreto para autenticação"},
            {"word": "firewall", "tip": "Barreira de proteção de rede"},
            {"word": "proxy", "tip": "Servidor intermediário de rede"},
            {"word": "dns", "tip": "Sistema de nomes de domínio"},
            {"word": "http", "tip": "Protocolo de transferência de hipertexto"},
            {"word": "https", "tip": "Protocolo seguro de transferência de hipertexto"},
            {"word": "ftp", "tip": "Protocolo de transferência de arquivos"},
            {"word": "smtp", "tip": "Protocolo de envio de e-mails"},
            {"word": "pop3", "tip": "Protocolo de recebimento de e-mails"},
            {"word": "ssh", "tip": "Protocolo seguro de acesso remoto"},
            {"word": "json", "tip": "Formato de dados leve"},
            {"word": "xml", "tip": "Formato de dados estruturado"},
            {"word": "yaml", "tip": "Formato de dados legível"},
            {"word": "script", "tip": "Arquivo de comandos executáveis"},
            {"word": "batch", "tip": "Processamento em lote"},
            {"word": "pipeline", "tip": "Fluxo de processamento de dados"},
            {"word": "deploy", "tip": "Publicação de aplicações"},
            {"word": "frontend", "tip": "Parte visual de uma aplicação"},
            {"word": "backend", "tip": "Parte lógica de uma aplicação"},
            {"word": "fullstack", "tip": "Desenvolvedor que atua no frontend e backend"},
            {"word": "devops", "tip": "Integração entre desenvolvimento e operações"},
            {"word": "agile", "tip": "Metodologia de desenvolvimento ágil"},
            {"word": "scrum", "tip": "Framework ágil para gestão de projetos"},
            {"word": "kanban", "tip": "Método visual de gestão de tarefas"},
            {"word": "jira", "tip": "Ferramenta de gestão de projetos"},
            {"word": "trello", "tip": "Aplicativo de organização de tarefas"},
        ]

    def sortWord(self):
        randomWord = random.choice(self.words)
        self.words.remove(randomWord)
        varWord = ''

        for char in randomWord["word"]:
            if char == ' ':
                varWord += '- '
            else:
                varWord += '_ '
        
        self.choosenWord = {
            "hiddenWord": varWord,
            "word": randomWord["word"],
            "tip": randomWord["tip"],
        }
        return self.choosenWord

    def validateCharacter(self, char):

        if char in self.choosenWord['word']:
            indices = [i for i, c in enumerate(' '.join(self.choosenWord['word'])) if c == char]
            return {
                "isValid": True,
                "indices": indices 
            }
        else:
            print(f"A letra '{char}' não está na palavra.")
            return {
                "isValid": False,
                "indices": []
            }
