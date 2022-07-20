import os

from dotenv import load_dotenv
from naff import Intents
from naff.ext.debug_extension import DebugExtension

from core.logging import init_logging
from core.base import CustomClient
from core.extensions_loader import load_extensions



if __name__ == "__main__":
    # load the environmental vars from the .env file
    load_dotenv()

    # initialise logging
    init_logging()

    # create our bot instance
    bot = CustomClient(
        intents=Intents.DEFAULT,  # intents are what events we want to receive from discord, `DEFAULT` is usually fine
        auto_defer=True,  # automatically deferring interactions
        activity="Anaffer bot",  # the status message of the bot
    )

    # load the debug extension if that is wanted
    if os.getenv("LOAD_DEBUG_COMMANDS") == "true":
        DebugExtension(bot=bot)

    # load all extensions in the ./extensions folder
    load_extensions(bot=bot)

    # start the bot
    bot.start(os.getenv("DISCORD_TOKEN"))
