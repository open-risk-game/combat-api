import json
import combat
import pytest

class FakeRequest():
    
    def __init__(self, _json=None, _raise_exception=None, app={}):
        self._json = _json
        self.app = app or {}
        self._raise_exception = _raise_exception

    async def json(self):
        if self._raise_exception:
            json.loads('None')
        return self._json

async def test_report():
    attacker = {
            "hex_id": 1,
            "player_id": 93,
            "tokens": 34,
            }
    defender = {

            "hex_id": 2,
            "player_id": 54,
            "tokens": 22,
            }

    data = {"attacker": attacker, "defender": defender}
    request = FakeRequest(_json=data)
    response = await combat.basic_combat(request)
    actual = json.loads(response.text)
    expected = {
            "combatReport": {
                "success": True,
            },
            "attackingTIle": {
                "id": 1,
                "owner": 93,
                "currentTokens": 34,
                "lostTokens": 0,
                },
            "defendingTile": {
                "id": 2,
                "owner": 93,
                "currentTokens": 34,
                "lostTokens": 22,
                }
            }
    assert expected == actual
