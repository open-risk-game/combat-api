import combat
import json


class FakeRequest:

    def __init__(self, data):
        self.data = data

    async def json(self):
        return self.data


async def test_basic_combat():
    data = {
        "attacker": {
            "name": "London",
            "tokens": 9
        },
        "defender": {
            "name": "Oxford",
            "tokens": 8
        }
    }
    fake_request = FakeRequest(data)
    response = await combat.basic_combat(fake_request)
    result = json.loads(response.text)

    assert result == {"result": -1}
