products = [

    {"name": "laptop", 'price': 1000},
    {"name": "smartphone", 'price': 500},
    {"name": "Tablet", 'price': 100},
    {"name": "Hairdryer", 'price': 200}
]
print(type(products))
print(type(products[0]))


def is_affordable(item):
    return item["price"] < 500


def is_affordable_name(item):
    return len(item["name"]) > 6


affordable_items = list(filter(is_affordable, products))
affordable_items_name = list(filter(is_affordable_name, products))
print(affordable_items)
print(affordable_items_name)
print(affordable_items[0]["name"],'$$',affordable_items[0]["price"])
print(affordable_items[1]["name"],"$$",affordable_items[1]["price"])

print(affordable_items_name[0]["price"],"@@",affordable_items_name[0]["name"])

print('*****for loop output********')
for i in affordable_items:
        print(i["name"], i["price"])
        print(i["price"], i["name"])
