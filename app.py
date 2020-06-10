from aiohttp import web
import combat

app = web.Application()

app.add_routes([
    web.post('/v0/basic-combat', combat.basic_combat)
        ])

if __name__ == "__main__":
    web.run_app(app)
