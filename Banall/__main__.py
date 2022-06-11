import os
from pyrogram import filters, idle
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from . import bot 
from Banall import START, FINISH, ERROR


@bot.on_message(filters.group & filters.command("banall"))
def main(_, msg: Message):
    chat = msg.chat
    me = chat.get_member(bot.get_me().id)
    if chat.get_member(msg.from_user.id).can_manage_chat and me.can_restrict_members and me.can_delete_messages:
        try:
            msg.reply(STARTED.format(chat.members_count))
            count_kicks = 0
            for member in chat.iter_members():
                if not member.can_manage_chat:
                    bot.ban_chat_member(chat_id=message.chat.id, user_id=member.user.id)
                    count_kicks += 1
            msg.reply(FINISH.format(count_kicks))
        except Exception as e:
            msg.reply(ERROR.format(str(e)))
    else:
        msg.reply("أحتاج إلى أن أكون مسؤولا في هذه المجموعة لتنفيذ هذا الإجراء!")


@bot.on_message(filters.group & filters.service, group=2)
def service(c, m):
    m.delete()


@bot.on_message(filters.private)
def start(_, msg: Message):
    msg.reply("مرحبا ، أنا روبوت لمساعدتك في إزالة جميع المستخدمين من مجموعتك.\nالآن أضفني إلى مجموعة ولا تنس أن تعطيني الصلاحيات.\nبعدها ارسل /banall في الكروب و سوف ابدء بعملي.", 
    reply_markup=InlineKeyboardMarkup(
                                      [
                                        [
                                           InlineKeyboardButton("قناه البوت", url="https://t.me/S8Y8S"), 
                                           InlineKeyboardButton("قناه التحديثات", url="https://t.me/N_B_10")                                      
                                        ]
                                      ]
                                     )
)


bot.run()
idle()
