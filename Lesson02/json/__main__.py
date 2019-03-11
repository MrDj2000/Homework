import json
import os.path

file_path = 'Lesson02/json/orders.json'


def write_order_to_json(pi_item: str,
                        pi_quantity: int,
                        pi_price: float,
                        pi_buyer: str,
                        pi_date: str
                        ):
    orders = []

    if os.path.exists(file_path):
        with open(file_path) as file:
            orders = json.load(file)
    print(orders)

    orders.append(dict(zip(['item', 'quantity', 'price', 'buyer', 'date'],
                           [pi_item, pi_quantity, pi_price, pi_buyer, pi_date]
                           )
                       )
                  )
    print(orders)

    with open(file_path, 'w') as file:
        json.dump(orders, file, sort_keys=True, indent=4)


write_order_to_json(pi_item='Computer',
                    pi_quantity=10,
                    pi_price=1000,
                    pi_buyer='Yandex',
                    pi_date='01.01.2019'
                    )

write_order_to_json(pi_item='DataCenter',
                    pi_quantity=20,
                    pi_price=4000000,
                    pi_buyer='Yahoo',
                    pi_date='01.01.2019'
                    )
write_order_to_json(pi_item='Phone',
                    pi_quantity=30,
                    pi_price=600,
                    pi_buyer='Huawei',
                    pi_date='01.01.2019'
                    )
write_order_to_json(pi_item='Satellite',
                    pi_quantity=40,
                    pi_price=5000000,
                    pi_buyer='Google',
                    pi_date='01.01.2019'
                    )
write_order_to_json(pi_item='Companies',
                    pi_quantity=50,
                    pi_price=9000000,
                    pi_buyer='Apple',
                    pi_date='01.01.2019'
                    )

