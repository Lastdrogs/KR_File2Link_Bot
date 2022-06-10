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
    if "about" in cb_data:
        await cmd.message.edit(
            Config.ABOUT_TXT,
            parse_mode="Markdown",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("💸 Dᴏɴᴀᴛᴇ", callback_data="donate")
                    ],
                    [
                        InlineKeyboardButton("⛺ Hᴏᴍᴇ", callback_data="home"),
                        InlineKeyboardButton("🗑 Cʟᴏsᴇ", callback_data="close")
                    ]
                ]
            )
        )

    elif "donate" in cb_data:
        await cmd.message.edit(
            Config.DONATE_TXT,
            parse_mode="Markdown",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Pᴀʏ 💰 Aᴍᴏᴜɴᴛ",
                                             url="https://telegram.dog/Lastdrogz")
                    ],
                    [
                        InlineKeyboardButton("⛺ Hᴏᴍᴇ", callback_data="home"),
                        InlineKeyboardButton("🗑 Cʟᴏsᴇ", callback_data="close")
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
                        InlineKeyboardButton("💸 Dᴏɴᴀᴛᴇ", callback_data="donate")
                    ],
                    [
                        InlineKeyboardButton("⛺ Hᴏᴍᴇ", callback_data="home"),
                        InlineKeyboardButton("🗑 Cʟᴏsᴇ", callback_data="close")
                    ]
                ]
            )
        )

    elif "home" in cb_data:
        await cmd.message.edit(
            Config.HOME_TXT.format(cmd.message.chat.first_name, cmd.message.chat.id),
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
