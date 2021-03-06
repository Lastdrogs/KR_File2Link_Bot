# (c) @AbirHasan2005 | @PredatorHackerzZ

from WebStreamer.bot import StreamBot
from configs import Config 
from WebStreamer.vars import Var
from WebStreamer.utils.human_readable import humanbytes
from WebStreamer.utils.database import Database
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, Message
from pyrogram.errors import UserNotParticipant
db = Database(Var.DATABASE_URL, Var.SESSION_NAME)
from pyrogram import Client


@StreamBot.on_message(filters.command('start') & filters.private & ~filters.edited)
async def start(b, m):
    if not await db.is_user_exist(m.from_user.id):
        await db.add_user(m.from_user.id)
        await b.send_message(
            Var.BIN_CHANNEL,
            f"#NEW_USER: \n\nNew User [{m.from_user.first_name}](tg://user?id={m.from_user.id}) Started !!"
        )
    usr_cmd = m.text.split("_")[-1]
    if usr_cmd == "/start":
        if Var.UPDATES_CHANNEL is not None:
            try:
                user = await b.get_chat_member(Var.UPDATES_CHANNEL, m.chat.id)
                if user.status == "banned":
                    await b.send_message(
                        chat_id=m.chat.id,
                        text="Sorry Sir, You are Banned to use me. Contact my [Support Group](https://t.me/kr_join).",
                        parse_mode="markdown"
                    )
                    return
            except UserNotParticipant:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="**Sᴏʀʀʏ Bʀᴏ Yᴏᴜ Hᴀᴠᴇ Nᴏᴛ Jᴏɪɴᴇᴅ Mʏ Uᴘᴅᴀᴛᴇs Cʜᴀɴɴᴇʟ Cʟɪᴄᴋ Oɴ Tʜᴇ Bᴜᴛᴛᴏɴ Bᴇʟᴏᴡ Aɴᴅ Jᴏɪɴ Tʜᴇɴ Sᴛᴀʀᴛ Aɢᴀɪɴ**",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("🔔 Jᴏɪɴ Mʏ Uᴘᴅᴀᴛᴇ Cʜᴀɴɴᴇʟ 🔔", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                            ]
                        ]
                    ),
                    parse_mode="markdown"
                )
                return
            except Exception:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="Something went Wrong. Contact my [Support Group](https://t.me/kr_join).",
                    parse_mode="markdown"
                )
                return
        await m.reply_photo(
            photo="https://telegra.ph/file/e954574ef60c1790caa79.jpg",
            caption=Config.HOME_TXT.format(m.from_user.first_name, m.from_user.id),
            parse_mode="Markdown",
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
    else:
        if Var.UPDATES_CHANNEL is not None:
            try:
                user = await b.get_chat_member(Var.UPDATES_CHANNEL, m.chat.id)
                if user.status == "banned":
                    await b.send_message(
                        chat_id=m.chat.id,
                        text="Sorry Sir, You are Banned to use me. Contact my [Support Group](https://t.me/kr_join).",
                        parse_mode="markdown",
                        disable_web_page_preview=True
                    )
                    return
            except UserNotParticipant:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="**Sᴏʀʀʏ Bʀᴏ Yᴏᴜ Hᴀᴠᴇ Nᴏᴛ Jᴏɪɴᴇᴅ Mʏ Uᴘᴅᴀᴛᴇs Cʜᴀɴɴᴇʟ Cʟɪᴄᴋ Oɴ Tʜᴇ Bᴜᴛᴛᴏɴ Bᴇʟᴏᴡ Aɴᴅ Jᴏɪɴ Tʜᴇɴ Sᴛᴀʀᴛ Aɢᴀɪɴ**",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("🔔 Jᴏɪɴ Mʏ Uᴘᴅᴀᴛᴇ Cʜᴀɴɴᴇʟ 🔔", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                            ],
                            [
                                InlineKeyboardButton("♻️ 𝐑𝐞𝐟𝐫𝐞𝐬𝐡 ♻️",
                                                     url=f"https://t.me/all_test_by_kr_bot?start=KRBotz_{usr_cmd}")
                            ]
                        ]
                    ),
                    parse_mode="markdown"
                )
                return
            except Exception:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="Something went Wrong. Contact my [Support Group](https://t.me/kr_join).",
                    parse_mode="markdown",
                    disable_web_page_preview=True)
                return

        get_msg = await b.get_messages(chat_id=Var.BIN_CHANNEL, message_ids=int(usr_cmd))

        file_size = None
        if get_msg.video:
            file_size = f"{humanbytes(get_msg.video.file_size)}"
        elif get_msg.document:
            file_size = f"{humanbytes(get_msg.document.file_size)}"
        elif get_msg.audio:
            file_size = f"{humanbytes(get_msg.audio.file_size)}"

        file_name = None
        if get_msg.video:
            file_name = f"{get_msg.video.file_name}"
        elif get_msg.document:
            file_name = f"{get_msg.document.file_name}"
        elif get_msg.audio:
            file_name = f"{get_msg.audio.file_name}"

        stream_link = "https://{}/{}".format(Var.FQDN, get_msg.message_id) if Var.ON_HEROKU or Var.NO_PORT else \
            "http://{}:{}/{}".format(Var.FQDN,
                                     Var.PORT,
                                     get_msg.message_id)

        msg_text = "**𝗬𝗼𝘂𝗿 𝗟𝗶𝗻𝗸 𝗚𝗲𝗻𝗲𝗿𝗮𝘁𝗲𝗱 !** 🤓\n\n📂 ** Fɪʟᴇ ɴᴀᴍᴇ :** `{}`\n\n📦**Fɪʟᴇ ꜱɪᴢᴇ :** `{}`\n\n📥 **Dᴏᴡɴʟᴏᴀᴅ :** `{}`\n\n🚸** Nᴏᴛᴇ : Tʜɪs ᴘᴇʀᴍᴀɴᴇɴᴛ Lɪɴᴋ , Nᴏᴛ Exᴘɪʀᴇᴅ**\n\n© **@KR_Botz**"
        await m.reply_text(
            text=msg_text.format(file_name, file_size, stream_link),
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Download Now", url=stream_link)]])
        )

@StreamBot.on_message(filters.command('help') & filters.private & ~filters.edited)
async def help_handler(bot, message):
    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(message.from_user.id)
        await bot.send_message(
            Var.BIN_CHANNEL,
            f"#NEW_USER: \n\nNew User [{message.from_user.first_name}](tg://user?id={message.from_user.id}) Started !!"
        )
    if Var.UPDATES_CHANNEL is not None:
        try:
            user = await bot.get_chat_member(Var.UPDATES_CHANNEL, message.chat.id)
            if user.status == "banned":
                await bot.send_message(
                    chat_id=message.chat.id,
                    text="Sorry Sir, You are Banned to use me. Contact my [Support Group](https://t.me/TeleRoid14).",
                    parse_mode="markdown",
                    disable_web_page_preview=True
                )
                return
        except UserNotParticipant:
            await bot.send_message(
                chat_id=message.chat.id,
                text="**Please Join My Updates Channel to use this Bot!**\n\nDue to Overload, Only Channel Subscribers can use the Bot!",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("🔔 Jᴏɪɴ Mʏ Uᴘᴅᴀᴛᴇ Cʜᴀɴɴᴇʟ 🔔", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                        ]
                    ]
                ),
                parse_mode="markdown"
            )
            return
        except Exception:
            await bot.send_message(
                chat_id=message.chat.id,
                text="Something went Wrong. Contact my [Support Group](https://t.me/kr_join).",
                parse_mode="markdown",
                disable_web_page_preview=True)
            return
    await message.reply_photo(
        photo="https://telegra.ph/file/e954574ef60c1790caa79.jpg",
        caption=Config.HELP_TXT, 
  parse_mode="Markdown",
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

@StreamBot.on_message(filters.command('about') & filters.private & ~filters.edited)
async def about_handler(bot, message):
    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(message.from_user.id)
        await bot.send_message(
            Var.BIN_CHANNEL,
            f"#NEW_USER: \n\nNew User [{message.from_user.first_name}](tg://user?id={message.from_user.id}) Started !!"
        )
    if Var.UPDATES_CHANNEL is not None:
        try:
            user = await bot.get_chat_member(Var.UPDATES_CHANNEL, message.chat.id)
            if user.status == "banned":
                await bot.send_message(
                    chat_id=message.chat.id,
                    text="Sorry Sir, You are Banned to use me. Contact my [Support Group](https://t.me/TeleRoid14).",
                    parse_mode="markdown",
                    disable_web_page_preview=True
                )
                return
        except UserNotParticipant:
            await bot.send_message(
                chat_id=message.chat.id,
                text="**Sᴏʀʀʏ Bʀᴏ Yᴏᴜ Hᴀᴠᴇ Nᴏᴛ Jᴏɪɴᴇᴅ Mʏ Uᴘᴅᴀᴛᴇs Cʜᴀɴɴᴇʟ Cʟɪᴄᴋ Oɴ Tʜᴇ Bᴜᴛᴛᴏɴ Bᴇʟᴏᴡ Aɴᴅ Jᴏɪɴ Tʜᴇɴ Sᴛᴀʀᴛ Aɢᴀɪɴ**",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("🔔 Jᴏɪɴ Mʏ Uᴘᴅᴀᴛᴇ Cʜᴀɴɴᴇʟ 🔔", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                        ]
                    ]
                ),
                parse_mode="markdown"
            )
            return
        except Exception:
            await bot.send_message(
                chat_id=message.chat.id,
                text="Something went Wrong. Contact my [Support Group](https://t.me/kr_join).",
                parse_mode="markdown",
                disable_web_page_preview=True)
            return
    await message.reply_photo(
        photo="https://telegra.ph/file/e954574ef60c1790caa79.jpg",
        caption=Config.ABOUT_TXT,
  parse_mode="html",
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

@StreamBot.on_callback_query()
async def button(bot: Client, cmd: CallbackQuery):

    cb_data = cmd.data
    if "aboutbot" in cb_data:
        await cmd.message.edit(
            Config.ABOUTCB_TXT,
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

    elif "closeMessage" in cb_data:
        await cmd.message.delete(True)

    try:
        await cmd.answer()
    except QueryIdInvalid: pass



