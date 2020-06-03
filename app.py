import os
import aiomysql
from aiohttp import web
import combat


async def create_db_pool(app):
    app['pool'] = await aiomysql.create_pool(
            host=os.environ['DB_HOST'],
            user=os.environ['DB_USER'],
            password=os.environ['DB_PASS'],
            db=os.environ['DB_NAME'],
            port=int(os.environ['DB_PORT'])
        )


async def close_db_conn(app):
    await app['pool'].close()

app = web.Application()

app.on_startup.append(create_db_pool)

app.add_routes([
    web.post('/v0/basic-combat', combat.basic_combat)
        ])

if __name__ == "__main__":
    web.run_app(app)
