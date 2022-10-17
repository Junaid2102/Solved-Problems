maximum = []

firstline = list(map(int, input().split()))
customers = int(firstline[0])
stock_available = int(firstline[1])
# print(f"Customers: {customers}")
# print(f"Available Stock: {stock_available}")

secondline = list(map(int, input().split()))
stockA = int(secondline[0])
stockB = int(secondline[1])
# print(f"StockA:{stockA}")
# print(f"StockB:{stockB}")

totalstock = stockA * stockB

# print(f"Total Stock: {totalstock}")
for reps in range(0, customers):
    add_customers = list(map(int, input().split()))
    # print(add_customers)
    maximum.append((add_customers[0] * stockA) + add_customers[1] * stockB)

maximum2 = maximum.copy()
maximum.sort()
# print(maximum2)
# print(maximum)
s = maximum2
li = []
for i in range(len(s)):
    li.append([s[i], i])
li.sort()
sort_index = []
for x in li:
    sort_index.append(x[1] + 1)

indexlist = []
i = 0
while(True):
    demand = maximum[i]
    if demand <= stock_available:
        stock_available = stock_available - demand
        indexlist.append(sort_index[i])
        i = i + 1
    else:
        break

print(len(indexlist))
for i in range(0, len(indexlist)):
    print(indexlist[i], end=' ')
