import time
import random
from pyrogram import Client, filters

CMD = ["/", "."]

@Client.on_message(filters.command("alive", CMD))
async def check_alive(_, message):
    await message.reply_text("ℕ𝕠𝕥 𝕕𝕖𝕒𝕕 𝕓𝕦𝕥 𝕤𝕥𝕚𝕝𝕝 𝕙𝕖𝕣𝕖.. 𝕐𝕠𝕦 𝕙𝕒𝕧𝕖 𝕟𝕠 𝕝𝕠𝕧𝕖 𝕗𝕠𝕣 𝕞𝕖 𝕟𝕠𝕨. 𝔾𝕠𝕠𝕕.. 𝕐𝕠𝕦 𝕒𝕣𝕖 𝕟𝕠𝕥 𝕥𝕙𝕖 𝕤𝕒𝕞𝕖 𝕒𝕤 𝕪𝕠𝕦 𝕨𝕖𝕣𝕖 𝕓𝕖𝕗𝕠𝕣𝕖... /start")


@Client.on_message(filters.command("ping", CMD))
async def ping(_, message):
    start_t = time.time()
    rm = await message.reply_text("...")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await rm.edit(f"Pong!\n{time_taken_s:.3f} ms")
