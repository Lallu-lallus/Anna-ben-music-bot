
import random
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import Client, filters



HOME_TEXT = "ππ» **Hi [{}](tg://user?id={})**,\n\nI'm ππππ πππ ** \n  πΈ ππ π πππππ πππ πππ π’π πππππ πππ πππππππ πππ πΈ ππ π πΏπππππ π±ππ π πππ ππ ππ π’πππ πππππ πππ ππππ ππ ππ πππππ πππππ β€οΈ π΅π¦ @Lallu_tg!"
HELP = """π·οΈ **Need Help?** π€
__(Join @RX_BOTZ For Support)__

π·οΈ **Common Commands**:
\u2022 `/play` ITTS A BAD VC PLAY UPDATE LATERπ€§
\u2022 `/help` shows help for admin commands 
\u2022 `/playlist` VC SO BADπ€§
\u2022 `/song` [song name] download the song as audio @music_wrld_grp
\u2022 `/video` [yt video link] download the yt videos  @music_wrld_grp

π·οΈ **Admin Commands**:
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

π·οΈ **Developer: @Lallu_tg** π
"""

@Client.on_message(filters.command('start'))
async def start(client, message):
    buttons = [
        [
        InlineKeyboardButton('α΄Κα΄Ι΄Ι΄α΄Κ', url='https://t.me/team_annaben'),
        InlineKeyboardButton('sα΄α΄α΄α΄Κα΄', url='https://t.me/Annaben_support')
    ],
    [
        InlineKeyboardButton('α΄α΄Κα΄ Κα΄α΄s', url='https://t.me/tg_bots_updates'),
        InlineKeyboardButton('α΄α΄α΄ ', url='https://t.me/lallu_tg')
    ],
    [
        InlineKeyboardButton('Κα΄Κα΄', callback_data='help')
        
    ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply_photo("https://telegra.ph/file/5649d8111f0a45039e282.jpg")
    await message.reply(HOME_TEXT.format(message.from_user.first_name, message.from_user.id), reply_markup=reply_markup)


@Client.on_message(filters.command("help"))
async def help(client, message):
    await message.reply_text(HELP)
