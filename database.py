from gino import Gino
from gino.schema import GinoSchemaVisitor
import add_to_database

POSTGRESURI = f"postgresql://postgres:posgrtes@localhost/bot"
db = Gino()


async def create_db():
    await db.set_bind(POSTGRESURI)
    db.gino: GinoSchemaVisitor

    # await db.gino.drop_all()
    await db.gino.create_all()
    # await add_to_database.add_items()