
seller = input().upper()
salary = float(input())
sales_made = float(input())

porcentage = sales_made * 15/100
adding = porcentage + salary


print(f'TOTAL = R$ {adding:.2f}')
