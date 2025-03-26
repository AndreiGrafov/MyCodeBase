import json

import requests

# here is small example of API testing
# this example is not conventional way of API testing, but it helps
# this is analog of UI 'base' class, here I store API's that provide jwt tokens
# other words this is realization of authentication process

class Base:
    # different tokens for different environments
    def get_admin_token(self):
        res = requests.post('https://api-stage.api-testing.com/api/Users/PasswordSignIn',
                            json={
                                "email": "grafov137@gmail.com",
                                "password": "1SuQ97dv98",
                            })
        # print("TOKEN HAS BEEN GOT: ", res.json())
        res = json.loads(res.content)
        res = res.get("accessToken")
        # res = str(res)
        res = "Bearer " + res
        # print(res)
        return res

    def get_admin_token_prod(self):
        res = requests.post('https://prod.api-testing.com/api/Users/PasswordSignIn',
                            json={
                                "email": "grafov137+owner@gmail.com",
                                "password": "1SuQ97dv98",
                            })
        # print("TOKEN HAS BEEN GOT: ", res.json())
        res = json.loads(res.content)
        res = res.get("accessToken")
        # res = str(res)
        res = "Bearer " + res
        # print(res)
        return res
