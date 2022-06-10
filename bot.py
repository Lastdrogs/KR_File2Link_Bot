# (1) @Lastdrogz

import os
import asyncio
import traceback
from binascii import (
    Error
)
from pyrogram import (
    Client,
    filters
)
from pyrogram.errors import (
    UserNotParticipant,
    FloodWait,
    QueryIdInvalid
)
from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    CallbackQuery,
    Message
)
from configs import Config
from handlers.database import db
from handlers.add_user_to_db import add_user_to_database
from handlers.send_file import send_media_and_reply
from handlers.helpers import b64_to_str, str_to_b64
from handlers.check_user_status import handle_user_status


@StreamBot.on_callback_query()
async def button(bot: Client, cmd: CallbackQuery):

    cb_data = cmd.data
    if "aboutbot" in cb_data:
        await cmd.message.edit(
            Config.ABOUT_BOT_TEXT,
            parse_mode="Markdown",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("💸 Dᴏɴᴀᴛᴇ", callback_data="aboutdevs")
                    ],
                    [
                        InlineKeyboardButton("⛺ Hᴏᴍᴇ", callback_data="gotohome"),
                        InlineKeyboardButton("🗑 Cʟᴏsᴇ", callback_data="closeMessage")
                    ]
                ]
            )
        )

    elif "aboutdevs" in cb_data:
        await cmd.message.edit(
            Config.ABOUT_DEV_TEXT,
            parse_mode="Markdown",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Pᴀʏ 💰 Aᴍᴏᴜɴᴛ",
                                             url="https://telegram.dog/Lastdrogz")
                    ],
                    [
                        InlineKeyboardButton("⛺ Hᴏᴍᴇ", callback_data="gotohome"),
                        InlineKeyboardButton("🗑 Cʟᴏsᴇ", callback_data="closeMessage")
                    ]
                ]
            )
        )

    elif "help" in cb_data:
        await cmd.message.edit(
            Config.HELP_TXT,
            parse_mode="Markdown",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("💸 Dᴏɴᴀᴛᴇ", callback_data="aboutdevs")
                    ],
                    [
                        InlineKeyboardButton("⛺ Hᴏᴍᴇ", callback_data="gotohome"),
                        InlineKeyboardButton("🗑 Cʟᴏsᴇ", callback_data="closeMessage")
                    ]
                ]
            )
        )

    elif "gotohome" in cb_data:
        await cmd.message.edit(
            Config.HOME_TEXT.format(cmd.message.chat.first_name, cmd.message.chat.id),
            parse_mode="Markdown",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("♡︎ Cᴏɴᴛᴀᴄᴛ 🧛‍♂️ Aᴅᴍɪɴ ♡︎", url='https://t.me/KR_Admin_Bot')
                    ],
                    [
                        InlineKeyboardButton("👨‍💻 Mʏ Fᴀᴛʜᴇʀ", url="https://t.me/Lastdrogz"),
                        InlineKeyboardButton("📢 Uᴘᴅᴀᴛᴇ", url="https://t.me/KR_botz")
                    ],
                    [
                        InlineKeyboardButton("📚 Aʙᴏᴜᴛ", callback_data="aboutbot"),
                        InlineKeyboardButton("💡 Hᴇʟᴘ", callback_data="help")
                    ]
                ]
            )
        )

    elif "closeMessage" in cb_data:
        await cmd.message.delete(True)

    try:
        await cmd.answer()
    except QueryIdInvalid: pass


Bot.run()
