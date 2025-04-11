from pyrogram import Client, filters
from _date import rexButton
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

likes_count = 0
liked_users = set()

@rexButton('corazon')
async def gaters(client, msg):
    
    user_id = msg.from_user.id
    global likes_count
    if user_id not in liked_users:
        liked_users.add(user_id)
        likes_count += 1        
        keyboard =InlineKeyboardMarkup([[InlineKeyboardButton(f"🤍 {likes_count}", callback_data="corazon")],[InlineKeyboardButton(f"{msg.message.reply_to_message.from_user.first_name}",url=f"t.me/{msg.message.reply_to_message.from_user.username}")]])
        
        await msg.message.edit_reply_markup(reply_markup=keyboard)
    else:
        liked_users.remove(user_id)
        likes_count -= 1        
        keyboard = InlineKeyboardMarkup([[InlineKeyboardButton(f"🤍 {likes_count}", callback_data="corazon")],[InlineKeyboardButton(f"{msg.message.reply_to_message.from_user.first_name}",url=f"t.me/{msg.message.reply_to_message.from_user.username}")]])
        await msg.message.edit_reply_markup(reply_markup=keyboard)
    