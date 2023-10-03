import requests
from project_modules.base_data.base_data import baseUrl


# for orderObj in range(len(orders)):
#     print(orders[orderObj])
#     coal_order_id = orders[orderObj]["coal_order_id"]

def get_orders():
    response = requests.get(baseUrl + '/autoDispatch/getCoalOrdersNeedDispatch')
    orders = response.json()

    return orders