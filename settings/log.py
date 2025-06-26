import logging
import os

# English: Directory for log files
# Português: Diretório para arquivos de log
LOG_DIR = os.path.join(os.path.dirname(__file__), "..", "logs")
os.makedirs(
    LOG_DIR, exist_ok=True
)  # English: Create log directory if it doesn't exist | Português: Cria o diretório de logs se não existir

# English: Path to the log file
# Português: Caminho para o arquivo de log
LOG_FILE = os.path.join(LOG_DIR, "app.log")

logging.basicConfig(
    level=logging.INFO,  # English: Set log level to INFO | Português: Define o nível de log para INFO
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",  # English: Log format | Português: Formato do log
    handlers=[
        logging.FileHandler(LOG_FILE, encoding="utf-8")
    ],  # English: Log to file | Português: Log em arquivo
)

# English: Logger instance for the application
# Português: Instância do logger para a aplicação
logger = logging.getLogger(__name__)
