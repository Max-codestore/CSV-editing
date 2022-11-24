import matplotlib.pyplot as plt,csv,collections
def read_csv_file(csv_file):
    l = []
    csv_file.encode('utf-8')
    file = open(csv_file)
    r = csv.reader(file)
    num = 0
    for i in r:
        l.append(i)
        num = num + 1
    file.close()
    del l[0]
    return l
def fuel(data):
    g = []
    dup=[]
    fueluse=[]
    for i in range(len(data)):
        g.append(data[i][5])
    for i in range(len(g)):
        indi=find_indices(g,g[i])
        dup.append(indi)
    for i in range(len(dup)):
        for i in range(len(dup[i])):
            print(dup[i])
            fueluse.append(data[i][22])
    print(fueluse)

def find_indices(list_to_check, item_to_find):
    indices = []
    for idx, value in enumerate(list_to_check):
        if value == item_to_find:
            indices.append(idx)
    return indices

def graphs(data):
    business = ['Logistics', 'Retail', 'Trading', 'Procurement','UK Centre','Busins Servic','DN IS','DN IS UK','Energy Wholale','Centre','DN Gas Storage','DN Energy Trading','DN Climate & Renewabl']
    labels = 'Logistics', 'Retail', 'Trading', 'Procurement','UK Centre','Business Service','DN IS','DN IS UK','Energy Wholesale','Centre','DN Gas storage','DN Energy Trading','DN Climate & Renewable'
    labelz= 'valid','valid but outdated','not valid'
    valid=['yes','yes(old)','no']
    valids =[]
    for i in range(len(valid)):
        valids.append(data[1].count(valid[i]))
    sizes =[]
    for i in range(len(business)):
        sizes.append(data[0].count(business[i]))
    fig1, ax1 = plt.subplots(2)
    ax1[0].set_title('what companies brought vehicles', fontsize=14)
    ax1[0].pie(sizes, labels=labels, autopct='%1.1f%%')
    ax1[0].axis('equal')
    ax1[1].set_title('number of valid, invalid and old registration plates', fontsize=14)
    ax1[1].bar(labelz,valids)
    plt.show()
l=read_csv_file('DN-Vehicle-Table-SE2.csv')
b = read_csv_file('DN-Fuel-TransactionSE4C6.csv')
x = []
y = []

for i in range(len(l)):
    x.append(l[i][5])
    y.append(l[i][1])

data = [x,y]
fuel(b)
graphs(data)


