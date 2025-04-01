import requests
from automation_testing.api_testing.APIs.base import Base
import json


# test data is complicated part of test process, sometimes precondition of the system
# is unpredictable, but tests are based on certain test data, the only solution I know for now
# is to generate new data right before test run from zero


# here is example of API that I call to generate data
class SetupBeforeTest(Base):

    # here I get id of user
    def get_sign_up_acc_id(self, search):
        token = self.get_admin_token()
        res = requests.post(f'https://api-stage.api-testing.com/api/administration/Users/List',
                              headers={
                                  "Authorization": token
                              },
                              json={
                                  "searchText": search,
                                    "orderBy": 0,
                                    "orderByDesc": False,
                                    "page": 0,
                                    "pageSize": 10
                                   })
        # print(res.json())
        res = json.loads(res.content)
        res = res["users"]
        res = res[0]
        res = list(res.values())[0]
        print("got acc id - ", res)
        return res

    # this api deletes user by its ID
    def delete_account(self, acc_id):
        token = self.get_admin_token()
        res = requests.delete(f'https://api-stage.api-testing.com/api/administration/Users/DeleteUser/{acc_id}',
                              headers={
                                  "Authorization": token
                              })
        # print(res.json())

    # here I get id of another entity
    def get_property_id(self, search):
        token = self.get_admin_token()
        res = requests.post(f'https://api-stage.api-testing.com/api/administration/Properties',
                              headers={
                                  "Authorization": token
                              },
                              json={
                                    "searchText": search,
                                    "orderBy": 0,
                                    "orderByDesc": False,
                                    "page": 0,
                                    "pageSize": 10
                                   })
        # print(res.json())
        res = json.loads(res.content)
        res = res["properties"]
        items = res
        active_property_id = None
        for item in items:
            status = list(item.values())[3]
            label = list(status.values())[1]
            print(label)
            if label == "Active":
                active_property_id = list(item.values())[0]
                print("active property id -", active_property_id)
            else:
                print('this property already deleted')
        return active_property_id

    # here I delete that entity
    def delete_property(self, property_id):
        token = self.get_admin_token()
        res = requests.put(f'https://api-stage.api-testing.com/api/administration/Properties/{property_id}/Delete',
                              headers={
                                  "Authorization": token
                              })
        # print(res.json())

    # here I get list of id's
    def get_all_widget_ids(self):
        token = self.get_admin_token_prod()
        res = requests.get(f'https://prod.api-testing.com/api/WidgetConfigurations/WidgetList?langId=2',
                              headers={
                                  "Authorization": token
                              },
                              json={
                                   })
        # print(res.json())
        list_ids = []
        res = json.loads(res.content)
        for widget in res:
            # print(widget["id"])
            list_ids.append(widget["id"])
        # print(res)
        return list_ids

