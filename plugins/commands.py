
import random
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import Client, filters



HOME_TEXT = "👋🏻 **Hi [{}](tg://user?id={})**,\n\nI'm 𝐀𝐍𝐍𝐀 𝐁𝐄𝐍 ** \n  𝙸 𝚊𝚖 𝚊 𝚖𝚞𝚜𝚒𝚌 𝚋𝚘𝚝 𝚊𝚗𝚍 𝚢𝚝 𝚟𝚒𝚍𝚎𝚘 𝚍𝚘𝚠𝚗𝚕𝚘𝚊𝚍𝚎𝚛 𝚋𝚘𝚝 𝙸 𝚊𝚖 𝚊 𝙿𝚞𝚋𝚕𝚒𝚌 𝙱𝚘𝚝 𝚞 𝚊𝚍𝚍 𝚖𝚎 𝚝𝚘 𝚢𝚘𝚞𝚛 𝚐𝚛𝚘𝚙𝚞 𝚊𝚗𝚍 𝚖𝚊𝚔𝚎 𝚖𝚎 𝚊𝚗 𝚊𝚍𝚖𝚒𝚗 𝚝𝚑𝚎𝚛𝚎 [❤️](https://telegra.ph/file/c3fdb36e73269c2e4d629.jpg) 𝐵𝑦 @Lallu_tg!"
HELP = """🏷️ **Need Help?** 🤔
__(Join @RX_BOTZ For Support)__

🏷️ **Common Commands**:
\u2022 `/play` ITTS A BAD VC PLAY UPDATE LATER🤧
\u2022 `/help` shows help for admin commands 
\u2022 `/playlist` VC SO BAD🤧
\u2022 `/song` [song name] download the song as audio @music_wrld_grp
\u2022 `/video` [yt video link] download the yt videos  @music_wrld_grp

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

@Client.on_message(filters.command('start'))
async def start(client, message):
    buttons = [
        [
        InlineKeyboardButton('ᴄʜᴀɴɴᴇʟ', url='https://t.me/team_annaben'),
        InlineKeyboardButton('sᴜᴘᴘᴏʀᴛ', url='https://t.me/Annaben_support')
    ],
    [
        InlineKeyboardButton('ᴍᴏʀᴇ ʙᴏᴛs', url='https://t.me/tg_bots_updates'),
        InlineKeyboardButton('ᴅᴇᴠ', url='https://t.me/lallu_tg')
    ],
    [
        InlineKeyboardButton('ʜᴇʟᴘ', callback_data='help')
        
    ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply(HOME_TEXT.format(message.from_user.first_name, message.from_user.id), reply_markup=reply_markup)


@Client.on_message(filters.command("help"))
async def help(client, message):
    await message.reply_text(HELP)
