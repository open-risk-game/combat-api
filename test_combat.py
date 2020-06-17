import combat


# combat receives http post request from Game service, with territory info
# (attacker/defender) and token info


class FakeRequest:

    def __init__(self, data):
        self.data = data

    async def json(self):
        return self.data


async def test_basic_combat():
    fake_data = {
        "attacker": {
            "name": "London",
            "tokens": 9
            },
        "defender": {
            "name": "Oxford",
            "tokens": 2
            }
    }
    fake_request = FakeRequest(fake_data)

    result = await combat.basic_combat(fake_request)
    assert result.status == 200
    assert result.text == '{"result": -7}'
