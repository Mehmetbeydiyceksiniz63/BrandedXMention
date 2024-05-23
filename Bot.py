# A Powerful Music And Management Bot
# Property Of Branded Indian Largest Support Group
# Rocks © @BRANDRD_BOT © BRANDRD
# Owner BRANDED + BRANDRD_BOT + BRANDED_WORLD 


import os, logging, asyncio
from telethon import Button
from telethon import TelegramClient, events
from telethon.tl.types import ChannelParticipantAdmin
from telethon.tl.types import ChannelParticipantCreator
from telethon.tl.types import ChannelParticipantsAdmins
from telethon.tl.functions.channels import GetParticipantRequest
from telethon.errors import UserNotParticipantError
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


logging.basicConfig(
    level=logging.INFO, format="%(name)s - [%(levelname)s] - %(message)s"
)
LOGGER = logging.getLogger(__name__)

api_id = int(os.environ.get("APP_ID", "20584104"))
api_hash = os.environ.get("API_HASH", "f325ee578444d70ad2d02b0673f94d3a")
bot_token = os.environ.get("BOT_TOKEN", "6908027707:AAE-9EmhhZ3JeiF-pDLzOs357OhEHo-Lbbs")
client = TelegramClient("client", api_id, api_hash).start(bot_token=bot_token)
spam_chats = []


@client.on(events.NewMessage(pattern="^/start$"))
async def start(event):
    chat_id = event.chat_id
    if not event.is_private:
        return await event.respond("Hayattayım 🥺")
    
    await event.client.send_file(
        event.chat_id,
        file="https://graph.org/file/6c7f4daee043fd1f0347b.jpg",
        caption="━━━━━━━━━━━━━━━━━━━━━━━━\n\nben kumsal'ım telgrafta tüm grup üyelerinden bahsedeceğim\n. /help komutunu kullarak komutları oğrenebilirsinis..\n\n┏━━━━━━━━━━━━━━━━━┓\n SAHİBİ🍃    : [rangar bey](http://t.me/RAGNARbeyy)\n yazılımcı 1 › : [zeytin hanım](https://t.me/Expfedai)┓\n yazılımcı 2› : [mehmet bey](https://t.me/Mehmettbeydiyeceksinizz)\n┗━━━━━━━━━━━━━━━━━┛\n\n💞 herhangi bir sorunuz varsa o zaman\n bana ulaşın [sahibi](https://t.me/RAGNARbeyy) ...\n\n━━━━━━━━━━━━━━━━━━━━━━━━",
        link_preview=False,
        buttons=[
            [Button.url("❤️‍🔥 beni grubuna ekle 💫", "https://t.me/Kumsaletiketbot?startgroup=true")],
            [Button.url("❤️‍🔥 müzik botu💫", "https://t.me/kumsalmuzikbot"), Button.url("❤️‍🔥 SAHİBİ 💫", "https://t.me/RAGNARbeyy")],
            [Button.url("❤️‍🔥 destek grubu 💫", "https://t.me/https://t.me/masaldestek"), Button.url("❤️‍🔥 yönetim botu❤️‍🔥", "https://t.me/uyuyanprensesinki_bot")]
        ]
    )


@client.on(events.NewMessage(pattern="^/help$"))
async def help(event):
    chat_id = event.chat_id
    if not event.is_private:
        return await event.respond("Sayın bu komutu kullanmak için pm'den başlayın 🥺")
    helptext = "kumsal bahsetme yardım menüsü\n\nkomutlar: /utag\netiket atar: /cancel etiketlemeyi durdurur.\nkomutlar /admin Grubunuzun tüm yöneticilerinden bahsetmek için\n✪ bu komutu başkalarından bahsetmek istediğiniz bir metinle kullanabilirsiniz.\n✪ `Example: /utag Günaydın!`\nBu komutu herhangi bir mesaja yanıt olarak kullanabilirsiniz, bot kullanıcıları söz konusu replide mesajına etiketleyecektir."
    await event.reply(
        helptext,
        link_preview=False,
        buttons=(
            [
                Button.url("❤️‍🔥 destek kanalı 💫", "https://t.me/masaldestekkanal"),
                Button.url("❤️‍🔥 yönetim botu 💫", "https://t.me/uyuyanprensesinki_bot"),
            ]
        ),
    )


@client.on(events.NewMessage(pattern="^/owner$"))
async def help(event):
    chat_id = event.chat_id
    if not event.is_private:
        return await event.respond("canım bu komutu kullanmak için beni pm ile başlat 🥺")
    helptext = "kumsal'ın sahibi menüsünden bahsetmek\n\nBenim sahibim [RANGAR BEY](https://t.me/RAGNARbeyy)\n made ın kumsal [kumsal kanal](https://t.me/masaldestek)\n✪ feuture anestezisi."
    await event.reply(
        helptext,
        link_preview=False,
        buttons=(
            [
                Button.url("❤️‍🔥 yazılımcı  1 💫", "https://tme./Expfedai"),
                Button.url("❤️‍🔥 yazılımcı  2 💫", "https://tme./Mehmettbeydiyeceksinizz"),
            ]
        ),
    )


@client.on(events.NewMessage(pattern="^/utag|/tag ?(.*)"))
async def mentionall(event):
    chat_id = event.chat_id
    if event.is_private:
        return await event.respond(
            "Bu komut grup ve kanalda kullanılabilir."
        )

    is_admin = False
    try:
        partici_ = await client(GetParticipantRequest(event.chat_id, event.sender_id))
    except UserNotParticipantError:
        is_admin = False
    else:
        if isinstance(
            partici_.participant, (ChannelParticipantAdmin, ChannelParticipantCreator)
        ):
            is_admin = True
    if not is_admin:
        return await event.respond("yalnızca yöneticiler hepsinden bahsedebilir")

    if event.pattern_match.group(1) and event.is_reply:
        return await event.respond("bana bir argüman ver")
    elif event.pattern_match.group(1):
        mode = "text_on_cmd"
        msg = event.pattern_match.group(1)
    elif event.is_reply:
        mode = "text_on_reply"
        msg = await event.get_reply_message()
        if msg == None:
            return await event.respond(
                "eski mesajlar için üyelerden bahsedemiyorum! (Gruba eklenmeden önce gönderilen mesajlar)"
            )
    else:
        return await event.respond(
            "Bir mesajı yanıtlayın veya başkalarından bahsetmem için bana bir mesaj gönderin"
        )

    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(chat_id):
        if not chat_id in spam_chats:
            break
        usrnum += 1
        usrtxt += f"[{usr.first_name}](tg://user?id={usr.id}) "
        if usrnum == 5:
            if mode == "text_on_cmd":
                txt = f"{usrtxt}\n\n{msg}"
                await client.send_message(chat_id, txt)
            elif mode == "text_on_reply":
                await msg.reply(usrtxt)
            await asyncio.sleep(2)
            usrnum = 0
            usrtxt = ""
    try:
        spam_chats.remove(chat_id)
    except:
        pass


@client.on(events.NewMessage(pattern="^/admins|/admin|@admin|@admins ?(.*)"))
async def _(event):
    chat_id = event.chat_id
    if event.is_private:
        return await event.respond("kusura bakmayın sadece grupta yöneticiden bahsedebilirsiniz")

    is_admin = False
    try:
        partici_ = await client(GetParticipantRequest(event.chat_id, event.sender_id))
    except UserNotParticipantError:
        is_admin = False
    else:
        if isinstance(
            partici_.participant, (ChannelParticipantAdmin, ChannelParticipantCreator)
        ):
            is_admin = True
    if not is_admin:
        return await event.respond("yalnızca yönetici grup yöneticilerinden bahsedebilir")

    if event.pattern_match.group(1) and event.is_reply:
        return await event.respond("bahsetmek için bir metin verin")
    elif event.pattern_match.group(1):
        mode = "text_on_cmd"
        msg = event.pattern_match.group(1)
    elif event.is_reply:
        mode = "text_on_reply"
        msg = await event.get_reply_message()
        if msg == None:
            return await event.respond(
                "eski mesajlar için üyelerden bahsedemiyorum! (Gruba eklenmeden önce gönderilen mesajlar)"
            )
    else:
        return await event.respond(
            "Bir mesajı yanıtlayın veya bahsedeceğiniz bir metin verin!"
        )

    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    chat = await event.get_input_chat()
    async for x in client.iter_participants(chat, filter=ChannelParticipantsAdmins):
        if not chat_id in spam_chats:
            break
        usrnum += 1
        usrtxt += f" \n [{x.first_name}](tg://user?id={x.id})"
        if usrnum == 5:
            if mode == "text_on_cmd":
                txt = f"{usrtxt}\n\n{msg}"
                await client.send_message(chat_id, txt)
            elif mode == "text_on_reply":
                await msg.reply(usrtxt)
            await asyncio.sleep(2)
            usrnum = 0
            usrtxt = ""
    try:
        spam_chats.remove(chat_id)
    except:
        pass


@client.on(events.NewMessage(pattern="^/cancel$"))
async def cancel_spam(event):
    if not event.chat_id in spam_chats:
        return await event.respond("Devam eden bir süreç yok...")
    else:
        try:
            spam_chats.remove(event.chat_id)
        except:
            pass
        return await event.respond("etiketleme durduruldu.")


print(">> kumsal etiket BOT WORKING <<")
client.run_until_disconnected()


# A Powerful Music And Management Bot
# Property Of Branded Indian Largest Support Group
# Rocks © @BRANDRD_BOT © BRANDRD
# Owner BRANDRD + BRANDRD_BOT + BRANDED_WORLD + BRANDRD SUPPORT CHAT 
