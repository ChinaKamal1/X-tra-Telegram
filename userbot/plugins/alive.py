"""Check if userbot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "**No Name set yet.** [Check Guide.](https://how2techy.com/xtra-guide1/)"

@command(outgoing=True, pattern="^.alive$")
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    await alive.edit("`Online Now🤑, My lord Is Back ` 💎 Respect(｀∇´)ψ**\n\n"
                     "`Talk politely else Gand Far Ke M chod denge`"
                     # Don't change this else you a TikTok loser, Son of Jinping. Add your own.
                     "`My Lord♟`: {DEFAULTUSER}\n\n"
                     "Ready to help✅")
