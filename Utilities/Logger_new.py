import yaml
import logging
import logging.config
from Configs.Config import TestData
from datetime import datetime


class Pylog:
    DEFAULT_LEVEL = logging.INFO

    @staticmethod
    def logr(__name__):
        now = datetime.now()
        log_filename = 'Logs/' + f"TestLog_{now.strftime('%d-%m-%Y %H-%M-%S')}" + '.log'

        try:
            with open(TestData.LOG_CONFIG_PATH, 'r') as cfg_file:
                config = yaml.safe_load(cfg_file)
                # print(f"\nBefore: {config['handlers']['file_handler']['filename']}")

            config['handlers']['file_handler']['filename'] = log_filename

            with open(TestData.LOG_CONFIG_PATH, 'w') as cfg_file:
                yaml.safe_dump(config, cfg_file)
                # print(f"\nAfter: {config['handlers']['file_handler']['filename']}")
            logging.config.dictConfig(config)

        except Exception as e:
            print(f'Error: {e},\nNeed to use Default logging')
            logging.basicConfig(level=Pylog.DEFAULT_LEVEL)

            # logging.basicConfig(filename='Test.log',
            #                     format='%(asctime)s %(levelname)s: %(message)s',
            #                     level=Pylog.DEFAULT_LEVEL
            #                     )

        logger = logging.getLogger(__name__)
        # logger.info('Logger setup successful')
        return logger
