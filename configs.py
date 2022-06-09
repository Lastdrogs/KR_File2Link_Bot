# (c) @LastDrogz

import os


class Config(object):

	ABOUT_TXT = f"""
**╭────[ 𝗔𝗕𝗢𝗨𝗧 𝗠𝗘 ]────⍟
├🤖 𝐌ʏ 𝐍ᴀᴍᴇ : [Fɪʟᴇs Sᴛᴏʀᴇ Bᴏᴛ](https://t.me/{BOT_USERNAME})
├👑 𝐎ᴡɴᴇʀ : [Hᴀᴘᴘʏ ⚡ Kɪᴅ](https://telegram.dog/happy_kid_sk)
├😎 𝐃ᴇᴠs : [Lᴀsᴛ 🐲 Dʀᴏɢᴢ](https://telegram.dog/LastDrogz) 
├📕 𝐋ɪʙʀᴀʀʏ : 𝐘ʀᴏɢʀᴀᴍ
├✏️ 𝐋ᴀɴɢᴜᴀɢᴇ : 𝐏ʏᴛʜᴏɴ 𝟹
├💾 𝐃ᴀᴛᴀ 𝐁ᴀsᴇ : 𝐌ᴏɴɢᴏ ᴅʙ
├🌀 𝐌ʏ 𝐒ᴇʀᴠᴇʀ : 𝐇ᴇʀᴏᴋᴜ
├💡 Cʀᴇᴅɪᴛs : @AbirHasan2005
├📊 𝐁ᴜɪʟᴅ 𝐒ᴛᴀᴜs : 𝟷.𝟸.𝟶 [ 𝐁ᴇᴛᴀ ]              
╰───────────────⍟ **
"""
	DONATE_TXT = f"""
**💗 𝐓𝐡𝐚𝐧𝐤𝐬 𝐟𝐨𝐫 𝐬𝐡𝐨𝐰𝐢𝐧𝐠 𝐢𝐧𝐭𝐞𝐫𝐞𝐬𝐭 𝐢𝐧 𝐝𝐨𝐧𝐚𝐭𝐢𝐨𝐧

Dᴏɴᴀᴛᴇ Us Tᴏ Kᴇᴇᴘ Oᴜʀ Sᴇʀᴠɪᴄᴇs Cᴏɴᴛɪɴᴏᴜsʟʏ Aʟɪᴠᴇ 😢
Yᴏᴜ Cᴀɴ Sᴇɴᴅ Aɴʏ Aᴍᴏᴜɴᴛ 
Of 20₹, 30₹, 50₹, 70₹, 100₹, 200₹ 😊

📨 Pᴀʏᴍᴇɴᴛ Mᴇᴛʜᴏᴅs:
 
GᴏᴏɢʟᴇPᴀʏ / Pᴀʏᴛᴏɴ / PʜᴏɴPᴀʏ / PᴀʏPᴀʟ
 
 Oʀ Dᴏɴᴀᴛᴇ: Mᴇssᴀɢᴇ Mᴇ @LastDrogz **
"""
	HOME_TXT = """
**⍟ ʜᴇʟʟᴏ ᴍʏ ғʀɪᴇɴᴅ [{}](tg://user?id={}) ⍟ 

⍟ ᴍʏ ɴᴀᴍᴇ ɪꜱ Fɪʟᴇs Sᴛᴏʀᴇ Bᴏᴛ I Aᴍ PᴏᴡᴇʀFᴜʟ 🧛‍♂️ Fɪʟᴇs Sᴛᴏʀᴇ Bᴏᴛ + Bᴀᴛᴄʜ Fɪʟᴇs sᴜᴘᴘᴏʀᴛ💞....!  
⍟ Sᴇᴇ Mʏ Pᴏᴡᴇʀ.....!!
⍟ Sʜᴀʀᴇ Aɴᴅ Sᴜᴘᴘᴏʀᴛ Us......!!! **
"""
	HELP_TXT = """
𝐇𝐎𝐖 𝐓𝐎 𝐆𝐄𝐓 𝐒𝐇𝐀𝐑𝐀𝐁𝐋𝐄 𝐋𝐈𝐍𝐊

**🔘  Sᴇɴᴅ Mᴇ Aɴʏ Fɪʟᴇ Oʀ Vɪᴅᴇᴏ I Wɪʟʟ Gɪᴠᴇ Yᴏᴜ A Pᴇʀᴍᴀɴᴇɴᴛ Sʜᴀʀᴀʙʟᴇ Lɪɴᴋ
🔘 Tʜɪs Is Pᴇʀᴍᴀɴᴇɴᴛ Fɪʟᴇs Sᴛᴏʀᴇ Bᴏᴛ!

🔘 Sᴇɴᴅ Mᴇ Aɴʏ Fɪʟᴇ I Wɪʟʟ Sᴀᴠᴇ Iᴛ Iɴ Mʏ Dᴀᴛᴀʙᴀsᴇ. Aʟsᴏ Wᴏʀᴋs Fᴏʀ Cʜᴀɴɴᴇʟ. Aᴅᴅ Mᴇ Tᴏ Cʜᴀɴɴᴇʟ As Aᴅᴍɪɴ Wɪᴛʜ Eᴅɪᴛ Pᴇʀᴍɪssɪᴏɴ, I Wɪʟʟ Aᴅᴅ Sᴀᴠᴇ Uᴘʟᴏᴀᴅᴇᴅ Fɪʟᴇ Iɴ Cʜᴀɴɴᴇʟ & Aᴅᴅ Sʜᴀʀᴀʙʟᴇ Bᴜᴛᴛᴏɴ Lɪɴᴋ.

️ Mᴀᴅᴇ Wɪᴛʜ ❣️ @KR_Botz & @BGM_LinkzZ 
⚜️ Bᴏᴛ Aɴʏ Issᴜᴇs Cᴏɴᴛᴀᴄᴛ Mᴇ
@KR_Admin_bot **
"""







