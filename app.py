from aiogram.utils import executor
from create import dp

from handlers import start, part1, part2, menuVvodPer, menuVvodBlank
from database import create_db

async def on_startup(dp):
    await create_db()

start.register_handlers_start(dp)
part1.register_handlers_part1(dp)
part2.register_handlers_part2(dp)
menuVvodPer.register_handlers_start1(dp)

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)