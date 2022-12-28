import sys
original_data = sys.argv[-1]

sep = "\n\n"
data = original_data.split(sep)

for line, index in zip(data, range(0,len(data))):
    sub_data = list(filter(None, line.split(' ')))
    if len(sub_data)!=0 and sub_data[0]=='on':
        while data[index][-1]=='\n':
            data[index]= data[index][:-1]

        data[index]="```\n"+data[index]+"\n```"

data = sep.join(data)
print(data)