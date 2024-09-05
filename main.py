import logging
import time

from api import parametros
from processing.processor import retornar_mensagem, executar_processamento
from utils.utils import setup_logging, log_error


def main():
    setup_logging()
    start_time = time.time()
    logging.info("Início da execução")

    try:
        mods = executar_processamento(parametros.MOD_ER)
        retornar_mensagem(mods)
    except Exception as e:
        log_error(f"Erro ao processar dados: {e}")

    end_time = time.time()
    total_time = end_time - start_time
    logging.info(f"Fim da execução - Tempo total: {total_time:.2f} segundos")


if __name__ == "__main__":
    main()
