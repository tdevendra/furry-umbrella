import matplotlib.pyplot as plt

sales = [(1, 92), (2, 1), (4, 23), (7, 21), (9, 39), (10, 61), (11, 168)]
totalsales = 450
labels = []
product = ['Frogs', 'Hogs', 'Dogs', 'Logs', 'Sheep', 'PC', 'Mobile', 'Pen', 'Book', 'Shirt', 'Spects', 'Shoes']
sizes = []
sum = 0
for s in sales:
    id, sales = s
    labels.append(product[id])
    pct = ((sales*100)/totalsales)
    sum = sum + sales
    sizes.append(pct)
rem = totalsales - sum
labels.append('Others')
sizes.append(rem)
plt.pie(sizes, labels=labels,
        autopct='%1.1f%%', startangle=90)
# Set aspect ratio to be equal so that pie is drawn as a circle.
plt.axis('equal')

plt.show()
