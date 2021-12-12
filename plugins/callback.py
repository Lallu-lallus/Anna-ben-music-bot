

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram import Client, emoji
from datetime import datetime, timedelta
from utils.vc import mp
from config import Config

@Client.on_callback_query()
async def cb_handler(client: Client, query: CallbackQuery):
    if query.from_user.id not in Config.ADMINS and query.data != "help" and query.data != "close":
        await query.answer(
            "You're Not Allowed! 🤣",
            show_alert=True
            )
        return
    if query.data == "replay":
        group_call = mp.group_call
        if not mp.playlist:
            return
        group_call.restart_playout()
        await mp.update_start_time()
        start_time = mp.start_time
        playlist = mp.playlist
        if not start_time:
            await query.edit_message_text(f"{emoji.PLAY_BUTTON} **Nothing Playing!**")
            return
        utcnow = datetime.utcnow().replace(microsecond=0)
        if mp.msg.get('current') is not None:
            playlist=mp.playlist
            if not playlist:
                pl = f"{emoji.NO_ENTRY} **Empty Playlist!**"
            else:
                if len(playlist) == 1:
                    pl = f"{emoji.REPEAT_SINGLE_BUTTON} **Playlist**:\n"
                else:
                    pl = f"{emoji.PLAY_BUTTON} **Playlist**:\n"
                pl += "\n".join([
                    f"**{i}**. **{x.audio.title}**"
                    for i, x in enumerate(playlist)
                    ])
            await mp.msg['current'].delete()
            mp.msg['current'] = await playlist[0].reply_text(
                f"{pl}\n\n{emoji.PLAY_BUTTON}  {utcnow - start_time} / "
                f"{timedelta(seconds=playlist[0].audio.duration)}",
                parse_mode="Markdown",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("🔄", callback_data="replay"),
                            InlineKeyboardButton("⏸", callback_data="pause"),
                            InlineKeyboardButton("⏭", callback_data="skip")
                            
                        ],
                    ]
                )
            )

    elif query.data == "pause":
        mp.group_call.pause_playout()
        await mp.update_start_time(reset=True)
        playlist = mp.playlist
        if not playlist:
            pl = f"{emoji.NO_ENTRY} **Empty Playlist!**"
        else:
            if len(playlist) == 1:
                pl = f"{emoji.REPEAT_SINGLE_BUTTON} **Playlist**:\n"
            else:
                pl = f"{emoji.PLAY_BUTTON} **Playlist**:\n"
            pl += "\n".join([
                f"**{i}**. **{x.audio.title}**"
                for i, x in enumerate(playlist)
                ])
        reply = await query.edit_message_text(f"{emoji.PLAY_OR_PAUSE_BUTTON} **Paused Playing!**\n\n{pl}",
        reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("🔄", callback_data="replay"),
                            InlineKeyboardButton("▶️", callback_data="resume"),
                            InlineKeyboardButton("⏭", callback_data="skip")
                            
                        ],
                    ]
                )
            )

    
    elif query.data == "resume":
        mp.group_call.resume_playout()
        playlist=mp.playlist
        if not playlist:
            pl = f"{emoji.NO_ENTRY} **Empty Playlist!**"
        else:
            if len(playlist) == 1:
                pl = f"{emoji.REPEAT_SINGLE_BUTTON} **Playlist**:\n"
            else:
                pl = f"{emoji.PLAY_BUTTON} **Playlist**:\n"
            pl += "\n".join([
                f"**{i}**. **{x.audio.title}**"
                for i, x in enumerate(playlist)
                ])
        await query.edit_message_text(f"{emoji.PLAY_OR_PAUSE_BUTTON} **Resumed Playing!**\n\n{pl}",
        reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("🔄", callback_data="replay"),
                            InlineKeyboardButton("⏸", callback_data="pause"),
                            InlineKeyboardButton("⏭", callback_data="skip")
                            
                        ],
                    ]
                )
            )

    elif query.data=="skip":
        playlist = mp.playlist
        await mp.skip_current_playing()
        if not playlist:
            pl = f"{emoji.NO_ENTRY} **Empty Playlist!**"
        else:
            if len(playlist) == 1:
                pl = f"{emoji.REPEAT_SINGLE_BUTTON} **Playlist**:\n"
            else:
                pl = f"{emoji.PLAY_BUTTON} **Playlist**:\n"
            pl += "\n".join([
                f"**{i}**. **{x.audio.title}**"
                for i, x in enumerate(playlist)
                ])

        try:
            await query.edit_message_text(f"⏭ **Skipped Track!**\n\n{pl}",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔄", callback_data="replay"),
                        InlineKeyboardButton("⏸", callback_data="pause"),
                        InlineKeyboardButton("⏭", callback_data="skip")
                            
                    ],
                ]
            )
        )
        except:
            pass
    elif query.data=="help":
        await query.edit_message_text("🙋‍♂️ **Hi Bruh**, \n Here is the command for my help text! 😌\n\nCheck /help To Know More ...",
        reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("ʏᴛ ᴠɪᴅᴇᴏ", callback_data="yt"),
                        InlineKeyboardButton("ᴅᴇᴠ", url="https//t.me/lallu_tg")
                    ],
                    [
                        InlineKeyboardButton("sᴏɴɢ", callback_data="song"),
                        InlineKeyboardButton("⚠︎ᴄʟᴏsᴇ", callback_data="close")
                    ],
                ]
            )      
        )          
                       
    elif query.data=="close":
        await query.message.delete()
                  
    elif query.data=="song":
        await query.edit_message_text("🙋‍♂️ **Hi Bruh**, \n Here is the commands for song \n\n Download your fav songs🙂 \n\n 𝐔𝐒𝐔𝐀𝐋 𝐂𝐎𝐌𝐌𝐀𝐍𝐃𝐒 \n\n /song (song name) or /mp3",
        reply_markup=InlineKeyboardMarkup(
               [ 
                   [
                        InlineKeyboardButton("⚠︎ᴄʟᴏsᴇ", callback_data="close")
                   ],
               ]
            )
         )
