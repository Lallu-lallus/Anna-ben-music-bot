
import random
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import Client, filters



HOME_TEXT = "👋🏻 **Hi [{}](tg://user?id={})**,\n\nI'm **𝐀𝐧𝐧𝐚 𝐁𝐞𝐧 𝐌𝐮𝐬𝐢𝐜 𝐁𝐨𝐭** \n 𝙸 𝚌𝚊𝚗 𝚙𝚕𝚊𝚢 𝚛𝚊𝚍𝚒𝚘/𝚜𝚝𝚛𝚎𝚊𝚖𝚎 𝙰𝚗𝚍 𝙸 𝚊𝚖 𝚊𝚖𝚞𝚜𝚒𝚌 𝚋𝚘𝚝 𝚊𝚗𝚍 𝚢𝚝 𝚟𝚒𝚍𝚎𝚘 𝚍𝚘𝚠𝚗𝚕𝚘𝚊𝚍𝚎𝚛 𝚋𝚘𝚝 𝙸 𝚊𝚖 𝚘𝚗𝚕𝚢 𝚠𝚘𝚛𝚔 𝚊𝚝 𝚖𝚞𝚜𝚒𝚌 𝚠𝚘𝚛𝚕𝚍 𝚐𝚛𝚘𝚞𝚙 𝑀𝑎𝑑𝑒 𝑤𝑖𝑡ℎ ❤️ 𝐵𝑦 @Lallu_tg!"
HELP = """🏷️ **Need Help?** 🤔
__(Join @Annaben_support For Support)__

🏷️ **Common Commands**:
\u2022 `/play` reply to an audio to play or queue it @music_wrld_grp
\u2022 `/help` shows help for commands 
\u2022 `/playlist` shows the playlist @music_wrld_grp
\u2022 `/current` shows playing time of current track @music_wrld_grp
\u2022 `/song` [song name] download the song as audio @music_wrld_grp
\u2022 `/video` [yt video link] download the yt videos only @music_wrld_grp

🏷️ **Admin Commands**:
\u2022 `/skip` [n] skip current or n where n >= 2
\u2022 `/join` join voice chat of current group
\u2022 `/leave` leave current voice chat
\u2022 `/vc` check which VC is joined
\u2022 `/stop` stop playing music
\u2022 `/radio` start radio stream
\u2022 `/stopradio` stop radio stream
\u2022 `/replay` play from the beginning
\u2022 `/clean` remove unused RAW PCM files
\u2022 `/pause` pause playing music
\u2022 `/resume` resume playing music
\u2022 `/mute` mute the VC userbot
\u2022 `/unmute` unmute the VC userbot
\u2022 `/restart` restart the bot

🏷️ **Developer: @Lallu_tg** 👑
"""
PIC = "https://telegra.ph/file/8f06df481d8722f502855.jpg"

@Client.on_message(filters.command('start'))
async def start(client, message):
    buttons = [
        [
        InlineKeyboardButton('ᴄʜᴀɴɴᴇʟ', url='https://t.me/team_annaben'),
        InlineKeyboardButton('sᴜᴘᴘᴏʀᴛ', url='https://t.me/Annaben_support'),
    ],
    [
        InlineKeyboardButton('ᴍᴏʀᴇ ʙᴏᴛs', url='https://t.me/tg_bots_updates'),
        InlineKeyboardButton('ᴅᴇᴠ', url='https://t.me/lallu_tg'),
    ],
    [
        InlineKeyboardButton('ʜᴇʟᴘ', callback_data='help'),
        
    ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await cmd.reply_photo(photo="https://telegra.ph/file/8f06df481d8722f502855.jpg", caption=HOME_TEXT.format(message.from_user.first_name, message.from_user.id), reply_markup=reply_markup)



@Client.on_message(filters.command("help"))
async def show_help(client, message):
    await message.reply_text(HELP)
