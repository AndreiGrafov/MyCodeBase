# often load an always stress testing needs a load of data
# and solution I came up with was to generate accounts on my own

import json

import requests
count = 1

res = requests.post('https://develop-api.com/users/authenticate?lang=en',
                        headers={
                            "X-Org-Id": "1"
                        },
                        json={
                            "identifier": "1900",
                            "password": "12345678",
                            # "_csrf": crfs
                        })
res = json.loads(res.content)
res = res.get("token")
admin_token = "Bearer " + res

# res_vpg = requests.post('https://develop-api.com/users/authenticate?lang=en',
#                         headers={
#                             "X-Org-Id": "3"
#                         },
#                         json={
#                             "identifier": "1200",
#                             "password": "Work@Admin10",
#                             # "_csrf": crfs
#                         })
# res_vpg = json.loads(res_vpg.content)
# res_vpg = res_vpg.get("token")
# vpg_token = "Bearer " + res_vpg

print(admin_token)

for i in range(1021, 1201):
    email = "grafov137+" + str(i) + "@gmail.com"
    # https://develop-api.com/users/create?lang=en
    # https://develop-api.com/users/create?lang=en
    res = requests.post('https://develop-api.com/users/create?lang=en',
                        headers={
                            "Authorization": admin_token,
                            "X-Org-Id": "1"
                        },
                        json={
                            "firstName": "load salary",
                             "lastName": "load salary",
                             "email": email,
                             "phone": "",
                             "userStatusId": {"value": 3,
                                              "label": "Active"},
                             "password": "1Su$Q97dv9@8",
                             "cardId": None,
                             "employeeId": None,
                             "roleId": [4],
                             "kitchensIds": [2],
                             "contractorsIds": None,
                             "connectTeam": 0,
                             "magneticStripe": "",
                             "hireFrom": None,
                             "hireTill": None,
                             "mealTypeId": [],
                             "isPasswordTemporary": "false",
                             "companyId": 1,
                             # "_csrf":"FJaA0o58-q_nirmlfW_SsyitpdIbS4532flM"
                        })
    print(res.content)
    print('("' + email + '", ' + '"1Su$Q97dv9@8"' + '),')


