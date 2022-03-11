#    Lion - UserBot
#    Copyright (C) 2020 Lion

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.

#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

from telethon.tl.types import Channel

from Lion import *
from Lion import ALIVE_NAME, bot, lionver
from Lion.LionConfig import Config, Var

# stats
log = "Enabled" if Var.PRIVATE_GROUP_ID else "Disabled"
bots = "Enabled" if Config.TG_BOT_USER_NAME_BF_HER else "Disabled"
lyd = "Enabled" if Var.LYDIA_API_KEY else "Disabled"
sudo = "Disabled" if Config.SUDO_USERS else "Enabled"
pm = "Disabled" if Var.PMSECURITY.lower() == "off" else "Enabled"
LIONUSER = str(ALIVE_NAME) if ALIVE_NAME else "@LionXsupport"

lion = f"𝙻𝙸𝙾𝙽 𝚅𝙴𝚁𝚂𝙸𝙾𝙽: {lionver}\n"
lion += f"𝙻𝙾𝙶 𝙶𝚁𝙾𝚄𝙿: {log}\n"
lion += f"𝙼𝚈 𝙰𝚂𝚂𝙸𝚂𝚃𝙰𝙽𝚃 𝙱𝙾𝚃: {bots}\n"
lion += f"𝙻𝚈𝙳𝙸𝙰: {lyd}\n"
lion += f"𝚂𝚄𝙳𝙾 𝚄𝚂𝙴𝚁: {sudo}\n"
lion += f"𝙿𝙼 𝚂𝙴𝙲𝚄𝚁𝙸𝚃𝚈: {pm}\n"
lion += "\\n𝚅𝙸𝚂𝙸𝚃 @LionXsupport 𝙵𝙾𝚁 𝙰𝚂𝚂𝙸𝚂𝚃𝙰𝙽𝚃.\\n"
lionstats = f"{lion}"

LION_NAME = bot.me.first_name
OWNER_ID = bot.me.id

# count total number of groups


async def lion_grps(event):
    a = []
    async for dialog in event.client.iter_dialogs():
        entity = dialog.entity
        if (
            isinstance(entity, Channel)
            and entity.megagroup
            and (entity.creator or entity.admin_rights)
        ):
            a.append(entity.id)
    return len(a), a
