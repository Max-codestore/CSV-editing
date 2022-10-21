import csv,re



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
    return l
def validate(v):
    validated = []
    valids=[]
    valids.append('valid license plates')
    validated.append('VEH REG')
    for i in range(len(v)-1):
        valid = re.findall(r"[A-Za-z]{2}[0-9]{2}[A-Za-z]{3}",v[i+1])
        if valid == []:
            valid_old=re.findall(r"[A-Za-z]{1}[0-9]{3}[A-Za_z]{3}",v[i+1])
            if valid_old != []:
                print(valid_old)
                validated.append(v[i+1])
                valids.append('yes(old)')
            else:
                validated.append(v[i+1])
                valids.append('no')
        elif valid != []:
            validated.append(v[i+1])
            valids.append('yes')

    return validated,valids
def write_csv(data):
    f=open("1.csv",'w',newline='')
    writer = csv.writer(f)
    for i in range(len(data[0])):
        writer.writerow([data[0][i], data[1][i]])


x=[]
c = read_csv_file("DN-Vehicle-Table-SE1.csv")
for i in range(len(c)-1):
    x.append(c[i+1][0])
t=validate(x)
write_csv(t)



