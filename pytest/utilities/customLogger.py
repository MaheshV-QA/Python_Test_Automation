import logging
from pathlib import Path

class LogGen:
    @staticmethod
    def loggen():
        log_file = Path(__file__).resolve().parents[1] / "Logs" / "automation.log"
        log_file.parent.mkdir(parents=True, exist_ok=True)

        logger = logging.getLogger("automationLogger")
        if not logger.handlers:
            fhandler = logging.FileHandler(filename=log_file, mode='a')
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            fhandler.setFormatter(formatter)
            logger.addHandler(fhandler)
            logger.setLevel(logging.INFO)
        return logger