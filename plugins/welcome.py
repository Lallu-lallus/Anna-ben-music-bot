import os
from pyrogram import Client, filters
from pyrogram.types import Message, User



@Client.on_message(filters.new_chat_members)
async def welcome(bot,message):
	chatid= message.chat.id
	await bot.send_message(text=f"Welcome {message.from_user.mention} to {message.chat.username} ,  ʙʀᴜʜ ᴛʜɪs ɪs ᴀ ᴍᴜsɪᴄ ɢʀᴏᴜᴘ ᴅᴏɴᴛ ᴀsᴋ ᴍᴏᴠɪᴇs ʜᴇʀᴇ ᴅᴏɴᴛ ᴜsᴇ sᴘᴀᴍ ᴡᴏʀᴅs ᴀsᴋ sᴏɴɢ ɴᴀᴍᴇ ᴡɪᴛʜ ᴄᴏᴍᴍᴀɴᴅ 🙂 ᴇɢ:/song faded, ᴅᴏᴡɴʟᴏᴀᴅ ʏᴛ ᴠɪᴅᴇᴏs🙂 eg: /video yt_link ᴏᴋ ʙʀᴏ ᴇᴊᴏʏ ᴛʜᴇ ᴜɴʟɪᴍɪᴛᴇᴅ ᴍᴜsɪᴄs🙂",chat_id=chatid)
	
@Client.on_message(filters.left_chat_member)
async def goodbye(bot,message):
	chatid= message.chat.id
	await bot.send_message(text=f"Bye ,  {message.from_user.mention} , ɢᴏ ᴀᴡᴀʏ ᴍᴀɴʜ, നീ ചത്തട്ടില്ലേ നമക്ക് പിന്നേം കാണാം😂",chat_id=chatid)
	

