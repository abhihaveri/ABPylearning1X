def even_number(n):
    if n %2==0:
        return True
    else:
        return False

n =[1,2,3,4,5,6,7,8]

even_order = list(filter(even_number,n))
print(f'even_order',even_order)

even_order_alter = list(filter(lambda n: n%2==0,n))
even_order_map = list(map(lambda n: n%2==0,n))
print('numbers list',n)
print(f'even_order_alter',even_order_alter)
print(f'even_order_map',even_order_map)