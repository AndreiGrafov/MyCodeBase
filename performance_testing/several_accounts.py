# the test that I manage to make is usually sequence of action that go one by one and doesn't
# effect on other parallel sessions.

# what is sequence here:
# 1 - take credentials,
# 2 - login,
# 3 - check if order exists (if exists then cancel it),
# 4 - create order,
# 5 - cancel it,
# 6 - create order,
# 7 - approve it,
# 8 - cancel it by admin

# it is a primitive realisation. Good realised tests simulate user action more realistic, with delays
# and "HttpUser" session has several different behaviour patterns, but due to lack of time and knowledge and
# because this simple sample was enough to fulfill needs, I stopped on that

import json
from datetime import date, timedelta

from locust import HttpUser, task, constant
from config import *


class Test(HttpUser):
    #https://develop-api.com
    #https://develop-api.com
    host = 'https://develop-api.com'
    wait_time = constant(0.5)
    token = ''
    user_id = ''

    def on_start(self):
        if len(USER_WORKEAT_SALARY) > 0:
            self.email, self.password = USER_WORKEAT_SALARY.pop()
        self.login()

        try:
            order_id = self.check_for_not_cancelled_order()
            print(order_id)

            self.cancel_by_order_id(order_id)
        except:
            print("nothing to cancel")
        # check for non cancelled tasks


    def login(self):
        print(self.email, self.password)
        res = self.client.post("/users/authenticate?lang=en",
                        headers={
                              "X-Org-Id": "1"
                        },
                         json={
                             "identifier": self.email,
                             "password": self.password,
                         })

        # print("Ya tut!!!!", res.content)
        res = json.loads(res.content)
        token = res["token"]
        user_id = res["id"]
        self.token = token
        self.user_id = user_id


    def check_for_not_cancelled_order(self):
        load_token = "Bearer " + self.token
        res = self.client.get(f'https://develop-api.com/kitchens/110/employeeLobby2?lang=en',
                           headers={
                               "Authorization": load_token,
                               "X-Org-Id": "1"
                           },
                           json={
                           })
        res = json.loads(res.content)
        order_id = ''
        today = date.today()
        tomorrow = today + timedelta(days=1)
        next_meal = res['nextMeal']
        for meals in next_meal:
            print(meals['date'])
            if meals['date'] == str(tomorrow):
                main_order = meals['order']
                # order_0 = main_order[0]
                order_id = main_order['id']
        print(order_id)
        return order_id

    def cancel_by_order_id(self, cancel_id):
        load_token = "Bearer " + self.token
        res = self.client.put(f'/orders/{cancel_id}/cancel?lang=en',
                              headers={
                                  "Authorization": load_token,
                                  "X-Org-Id": "1"
                              },
                              json={
                              })
        print("deleted")
        # print(res.json())

    @task
    def join(self):
        token = "Bearer " + self.token
        #https://develop-api.com/kitchens/110/employeeLobby2?lang=en
        res = self.client.get(f'https://develop-api.com/kitchens/110/employeeLobby2?lang=en',
                              headers={
                                  "Authorization": token,
                                  "X-Org-Id": "1"
                              },
                              json={
                              })
        res = json.loads(res.content)
        # print(res)
        print("gotcha")

        print('hello')
        token = "Bearer " + self.token
        res = self.client.post('/orders/create?lang=en',
                            headers={
                                "Authorization": token,
                                "X-Org-Id": "1"
                            },
                            json={
                                "orderMealDishData": [
                                    {"mealDishId": 34472, "quantity": 1, "price": 0},
                                    {"mealDishId": 34471, "quantity": 1, "price": 0}
                                ],
                                "mealExtraId": [],
                                "paymentType": 4
                            })
        res = json.loads(res.content)
        order_id = res["id"]
        # print(order_id)

        res = self.client.put(f'/orders/{order_id}/cancel?lang=en',
                           headers={
                               "Authorization": token,
                               "X-Org-Id": "1"
                           },
                           json={
                           })
        print("deleted")
        # print(res.json())

        res = self.client.get(
            f'https://develop-api.com/orders/getAllOrders?lang=en&kitchenId=110&userId={self.user_id}&reservationType=Reservations&page=1&limit=25',
            headers={
                "Authorization": token,
                "X-Org-Id": "1"
            },
            json={
            })
        res = json.loads(res.content)
        # print(res)
        print("gotcha2")

        # make order with new mealdish id's (for day after tommorow)
        res = self.client.post('https://develop-api.workeat.co.il/orders/create?lang=en',
                            headers={
                                "Authorization": token,
                                "X-Org-Id": "1"
                            },
                            json={
                                "orderMealDishData": [
                                    {"mealDishId": 31711, "quantity": 1, "price": 1},
                                    {"mealDishId": 31712, "quantity": 1, "price": 1}
                                ],
                                "mealExtraId": [],
                                "paymentType": 4,
                            })
        res = json.loads(res.content)
        order_id = res["id"]
        print(order_id)

        # from orders/create take reservation id https://develop-api.workeat.co.il/orders/{id}?lang=en
        res = self.client.get(f'https://develop-api.workeat.co.il/orders/{order_id}?lang=en',
                           headers={
                               "Authorization": token,
                               "X-Org-Id": "1"
                           },
                           json={
                           })
        print('order info start')
        res = json.loads(res.content)
        hash = res["hash"]
        print('hash - ', hash)
        orderMealDishes = res['orderMealDishes']
        orderMealDishes = orderMealDishes[0]
        mealDIsh = orderMealDishes['mealDish']
        meal = mealDIsh['meal']
        mealID = meal['id']
        print('meal id - ', mealID)
        print('order info end')
        # get hash and meal id

        # realize order (token: kitchen device token)
        kitchen_device = 'Bearer ' + 't1kjOtPxKpPPvjLZjuXJ5S7aKQTXcd4U'
        res = self.client.post(f'https://develop-api.workeat.co.il/kitchenDevices/realizeByHash',
                            headers={
                                "Authorization": kitchen_device,
                                "X-Org-Id": "1"
                            },
                            json={
                                "hash": hash,
                                "mealId": mealID
                            })
        res = json.loads(res.content)
        orderId = res["id"]
        userId = res["userId"]
        print('realized')

        #get admin token
        res = self.client.post('https://develop-api.workeat.co.il/users/authenticate?lang=en',
                            json={
                                "identifier": "1900",
                                "password": "12345678",
                                # "_csrf": crfs
                            })
        res = json.loads(res.content)
        res = res.get("token")
        shay_token = "Bearer " + res

        # cancel order
        res = self.client.put(f'https://develop-api.workeat.co.il/orders/{orderId}/cancelByAdmin?lang=en',
                           headers={
                               "Authorization": shay_token,
                               "X-Org-Id": "1"
                           },
                           json={
                               "userId": userId
                           })
        res = json.loads(res.content)
        orderId = res["id"]
        print(orderId)
        print('deleted by admin')

