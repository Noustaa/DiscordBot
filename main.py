import NoussBot
from dotenv import load_dotenv
import os

if __name__ == '__main__':
    load_dotenv(dotenv_path="config")
    bot = NoussBot.NoussBot()
    # noinspection SpellCheckingInspection
    bot.run(os.getenv("TOKEN"))
