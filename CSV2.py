import csv,re,pandas



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
    stat =[]
    for i in range(len(v)):
        split = [int(x) for x in str(v[i])]
        while split[-1] == 0:
            split.pop()
        check = split.pop()
        total=[]
        for i in range(len(split)):
            if (i % 2) == 0:
                total.append(split[i] * 2)

            else:
                total.append(split[i])
        for i in range(len(total)):
            if total[i] >= 10 and total[i] <= 99:
                splitup = [int(x) for x in str(total[i])]
                part1=sum(splitup)
            else:
                part1 = 0
        part2=sum(total)+part1
        checkdigt = 10-(part2%10)
        if checkdigt == check:
            status='valid'
        else:
            status = 'invalid'
        stat.append(status)
    return stat
def write_csv(data):
    f=open("1.csv",'w',newline='')
    print(data)
    writer = csv.writer(f)
    for i in range(len(data)):
        writer.writerow([data[i]])
    #df = pandas.read_csv("1.csv")
    #df['valid license plates'] = df['valid license plates'].replace({df['valid license plates']: data})
    #df.to_csv("1.csv", index=False)
x=[]
y=[]
c = read_csv_file("DN-Fuel-TransactionSE3.csv")
for i in range(len(c)-1):
    x.append(c[i+1][2])
#    y.append(c[i][3])
#b=[x],[y]

t=validate(x)
write_csv(t)


#=MOD(SUM(INT(MID(REPT("0",20-LEN(B2))&B2,ROW($1:$20),1)*(MOD(ROW($1:$20),2)+1)/10)+MOD(MID(REPT("0",20-LEN(B2))&B2,ROW($1:$20),1)*(MOD(ROW($1:$20),2)+1),10)),10)=0