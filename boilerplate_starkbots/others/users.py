from database.users_sql import Users, num_users
from database.chats_sql import Chats, num_chats
from pystark.database.postgres import Session
from pyrogram.types import Message
from pystark import Stark, filters


@Stark.cmd(extra_filters=~filters.edited & ~filters.service, group=2)
async def users_sql(_, msg: Message):
    if msg.from_user:
        q = Session.query(Users).get(int(msg.from_user.id))
        if not q:
            Session.add(Users(msg.from_user.id))
            Session.commit()
        else:
            Session.close()


@Stark.cmd(group_only=True, extra_filters=~filters.edited & ~filters.service, group=3)
async def chats_sql(_, msg: Message):
    if msg.chat and msg.chat.id:
        q = Session.query(Chats).get(int(msg.chat.id))
        if not q:
            Session.add(Chats(msg.chat.id))
            Session.commit()
        else:
            Session.close()


@Stark.cmd('stats', owner_only=True)
async def _stats(_, msg: Message):
    users = await num_users()
    chats = await num_chats()
    await msg.reply(f"Total Users : {users} \n\nTotal Chats : {chats}", quote=True)
