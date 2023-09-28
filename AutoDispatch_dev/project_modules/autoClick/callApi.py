import requests
from project_modules.baseData.baseData import baseUrl


response = requests.get(baseUrl+'/autoDispatch/getCoalOrdersNeedDispatch')

orders = response.json()

for orderObj in range(len(orders)):
    print(orders[orderObj])
    coal_order_id = orders[orderObj]["coal_order_id"]