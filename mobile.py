mobile_data = {
    'status': True,
    'data': [
        {'name': 'Xiaomi Note 5', 'price': '300 USD', 'made': 'China'},
        {'name': 'Samsung Note 6', 'price': '200 USD', 'made': 'USA'},
        {'name': 'Iphone 5', 'price': '180.5 USD', 'made': 'Japan'},
        {'name': 'Pixel 5', 'price': '89.60 USD', 'made': 'Rusia'},
        {'name': 'Techno 5', 'price': '110 USD', 'made': 'Uk'},
        {'name': 'Huawei 5', 'price': '350 USD', 'made': 'Malaysia'},
    ],
    'exchange_rate': 103.25
}

#  Your Code Starts from here
# example: Xiaomi Note 5 is made in China. The price is 300 USD which is almost equal to 30975 BDT

for data in mobile_data.get('data'):
    name = data.get('name')
    price = data.get('price')
    country = data.get('made')
    bdt = int(float(price.replace(' USD', '')) * mobile_data.get('exchange_rate'))
    sentence1 = f"{name} is made in {country}. "
    sentence2 = f"The price is {price} which is almost equal to {bdt} BDT"
    template = sentence1 + sentence2
    print(template)
