# (1) @Lastdrogz

import os
from pyrogram.errors import (
    UserNotParticipant,
    FloodWait,
    QueryIdInvalid
)
from configs import Config

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
