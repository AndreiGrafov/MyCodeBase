import requests
from automation_testing.api_testing.APIs.base import Base
import json

class ApiTestingExample(Base):

    # example step 1
    def get_some_meals(self):
        kitchen_token = self.get_admin_token()
        res = requests.get('https://api-stage.api-testing.com/kitchenDevices/meals',
                                   headers={
                                           "Authorization": kitchen_token
                                    })
        print("Result: ", res.json())
        res = json.loads(res.content)
        return res

    # example step 2
    def get_some_kitchen(self):
        kitchen_token = self.get_admin_token()
        res = requests.get('https://api-stage.api-testing.com/kitchenDevices/kitchen',
                                   headers={
                                           "Authorization": kitchen_token
                                    })
        print("Result: ", res.json())
        res = json.loads(res.content)
        return res

    # example step 3
    def get_next_meal(self):
        kitchen_token = self.get_admin_token()
        res = requests.get('https://api-stage.api-testing.com/kitchenDevices/nextMeal',
                                   headers={
                                           "Authorization": kitchen_token
                                    })
        print("Result: ", res.json())
        res = json.loads(res.content)
        return res

