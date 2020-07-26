from aiohttp import web


async def basic_combat(request):
    data = await request.json()
    attacker = data.get('attacker')
    defender= data.get('defender')
    attacker_tokens = int(attacker.get('tokens'))
    defender_tokens = int(defender.get('tokens'))
    result = defender_tokens - attacker_tokens
    print(result, 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')

    success = True
    defender_owner = attacker.get('player_id')
    attacker_current_tokens = 0
    attacker_lost_tokens = 0
    defender_current_owner = attacker.get('player_id')
    defender_lost_tokens = 0
    if result > 0:
        success = False
        defender_current_owner = defender.get('player_id')
        defender_owner = defender.get('player_id')
        defender_current_tokens = result
        

    combat_report = report(
            success,
            attacker.get('hex_id'),
            attacker.get('player_id'),
            attacker_current_tokens,
            attacker_lost_tokens,
            defender.get('hex_id'),
            defender_current_owner,
            defender_current_tokens,
            defender_lost_tokens,
            )
    return web.json_response(combat_report)

def report(
        success,
        attacking_id,
        attacker_owner,
        attacker_current_tokens,
        attacker_lost_tokens,
        defending_id,
        defender_owner,
        defender_current_tokens,
        defender_lost_tokens,
        ):

    report = {
            "combatReport": {
                "success": success,
            },
            "attackingTIle": {
                "id": attacking_id,
                "owner": attacker_owner,
                "currentTokens": attacker_current_tokens,
                "lostTokens": attacker_lost_tokens,
                },
            "defendingTile": {
                "id": defending_id,
                "owner": defender_owner, 
                "currentTokens": defender_current_tokens,
                "lostTokens": defender_lost_tokens
                }
            }
    return report
