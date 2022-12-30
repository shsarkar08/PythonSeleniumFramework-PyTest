import logging
import logging.config
import yaml
from Configs.Config import TestData


class Pylog:

    DEFAULT_LEVEL = logging.INFO

    @staticmethod
    def logr(__name__):
        try:
            with open(TestData.LOG_CONFIG_PATH, 'r') as cfg_file:
                config = yaml.safe_load(cfg_file.read())
                logging.config.dictConfig(config)

        except Exception as e:
            print(f'Error: {e},\nNeed to use Default logging')
            logging.basicConfig(filename='.\\Logs\\BaseConfigLog',
                                format='%(asctime)s %(levelname)s: %(message)s',
                                level=Pylog.DEFAULT_LEVEL
                                )

        logger = logging.getLogger(__name__)
        # logger.info('Logger setup successful')
        return logger
