from aiohttp import web


async def basic_combat(request):
    data = await request.json()
    attacker_tokens = data.get('attacker').get('tokens')
    defender_tokens = data.get('defender').get('tokens')
    result = defender_tokens - attacker_tokens
    return web.json_response({'result': result})
