import pybase64

from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP, bot
from userbot.utils import zelda_cmd, edit_delete, edit_or_reply

@zelda_cmd(pattern="enc(?: |$)(.*)")
async def endecrypt(query):
    xx = query.pattern_match.group(1)
    if xx:
        msg = xx
    elif event.is_reply:
        msg = await event.get_reply_message()
    else:
        return await edit_delete(event, "**Berikan Sebuah Pesan atau Reply**")
    lething = str(pybase64.b64encode(bytes(msg, "utf-8")))[2:]
    await query.edit("`" + lething[:-1] + "`")
    
        
@zelda_cmd(pattern="dec(?: |$)(.*)")
async def endecrypt(query):
    xx = query.pattern_match.group(1)
    if xx:
        msg = xx
    elif event.is_reply:
        msg = await event.get_reply_message()
    else:
        return await edit_delete(event, "**Berikan Sebuah Pesan atau Reply**")
    lething = str(pybase64.b64decode(bytes(msg, "utf-8"), validate=True))[2:]
    await query.edit(f"**Decoded from** `{msg}` **:**\n`" + lething[:-1] + "`")
        

CMD_HELP.update(
    {
        "encrypt": f"**Plugin : **`base64`\
        \n\n  •  **Syntax :** `{cmd}enc`\
        \n  •  **Function : **Enkripsi pesan dengan base64.**\
        \n\n  •  **Syntax :** `{cmd}dec`\
        \n  •  **Function : **Mentranslate dari Kode base64.**\
    "
    }
)