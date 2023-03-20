from urllib.parse import quote

from nonebot import get_driver, on_message
from nonebot.adapters.onebot.v11 import MessageEvent

from .config import Config

config = Config.parse_obj(get_driver().config)
commands = config.get_commands()

wns = on_message(priority=config.wns_priority, block=config.wns_block)


@wns.handle()
async def wns_handle(event: MessageEvent):
    if event.reply is None:
        await wns.finish()
    command = event.message.extract_plain_text().strip()
    message = event.reply.message
    url = config.get_url(command)

    await wns.finish(
        url.format(quote(message.extract_plain_text().strip(), "utf-8") if "{}" in url else url) if url else None
    )
