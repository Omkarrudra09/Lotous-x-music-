import asyncio
import importlib

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from LotousXMusic import LOGGER, app, userbot
from LotousXMusic.core.call import Hotty
from LotousXMusic.misc import sudo
from LotousXMusic.plugins import ALL_MODULES
from LotousXMusic.utils.database import get_banned_users, get_gbanned
from config import LOTOUS_USERS


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("Assistant client variables not defined, exiting...")
        exit()
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            LOTOUS_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            LOTOUS_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("LotousXMusic.plugins" + all_module)
    LOGGER("LotousXMusic.plugins").info("Successfully Imported Modules...")
    await userbot.start()
    await Hotty.start()
    try:
        await Hotty.stream_call("https://graph.org/file/e999c40cb700e7c684b75.mp4")
    except NoActiveGroupCall:
        LOGGER("LotousXMusic").error(
            "Please turn on the videochat of your log group\channel.\n\nStopping Bot..."
        )
        exit()
    except:
        pass
    await Hotty.decorators()
    LOGGER("LotousXMusic").info(
        "ᴅʀᴏᴘ ʏᴏᴜʀ ɢɪʀʟꜰʀɪᴇɴᴅ'ꜱ ɴᴜᴍʙᴇʀ ᴀᴛ @LotousIpsitaMusic ᴊᴏɪɴ @angle_Lotous1_bot , @friends_chat_groupz ꜰᴏʀ ᴀɴʏ ɪꜱꜱᴜᴇꜱ"
    )
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("LotousXMusic").info("Stopping Lotous Music Bot...")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
