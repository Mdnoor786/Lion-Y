"""Pins the replied message
Syntax: .cpin [LOUD]"""
from telethon.tl import functions

from Lion import CMD_HELP
from Lion.utils import admin_cmd


@Lion.on(admin_cmd(pattern="cpin ?(.*)"))
@Lion.on(sudo_cmd(pattern="cpin ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    silent = not input_str
    if event.message.reply_to_msg_id is not None:
        message_id = event.message.reply_to_msg_id
        try:
            await borg(
                functions.messages.UpdatePinnedMessageRequest(
                    event.chat_id, message_id, silent
                )
            )
        except Exception as e:
            await eor(event, str(e))
        else:
            await event.delete()
    else:
        await eor(event, "Reply to a message to pin the message in this Channel.")


CMD_HELP.update({"pin_message": ".cpin <reply to mssg>\nUse - Pin the message."})
