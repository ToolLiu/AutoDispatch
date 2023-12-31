import requests
from project_modules.base_data.base_data import baseUrl


# for orderObj in range(len(orders)):
#     print(orders[orderObj])
#     coal_order_id = orders[orderObj]["coal_order_id"]

def get_orders():
    response = requests.get(baseUrl + '/autoDispatch/getCoalOrdersNeedDispatch')
    orders = response.json()

    return orders


def updateCoalBillNum(coal_order_id, coal_bill_number):
    params = {
        "coal_order_id": coal_order_id,
        "coal_bill_number": coal_bill_number,
    }
    response = requests.post(baseUrl + '/coal/addCoalBillNum', data=params)
    print(response)
    return response
