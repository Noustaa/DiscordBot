import noussbot
from dotenv import load_dotenv
import os
import logging
import sys

# main function
if __name__ == '__main__':
    # check if config file argument is there and verify that the config file exists
    assert os.path.exists(sys.argv[1]), "Config file is needed. Usage: python runbot.py config_file_path"
    # activate logging and define logging configuration
    logging.basicConfig(filename='noussbot.log', encoding='utf-8', level=logging.INFO, format='%(asctime)s'
                                                                                              ' %(levelname)s'
                                                                                              ' %(name)s'
                                                                                              ' %(message)s')
    # loads config file variables to environment variables
    load_dotenv(dotenv_path=sys.argv[1])

    # instantiate the bot
    bot = noussbot.NoussBot()
    # runs the bot with the token from config file (loaded from environment variable)
    bot.run(os.getenv("TOKEN"))
