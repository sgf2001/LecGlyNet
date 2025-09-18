import pandas as pd

def get_type(sents: str):
    """获取字符串中糖的种类"""
    sac_list = []
    sub_sents = sents.split(",")
    for i in sub_sents:
        sac_list.append(i.split(":")[0])
    return sac_list

# 读取文件
f = open("test.txt").readlines()

# 统计单、双、三糖的种类列表
single = []
double = []
trip = []
for i in f:
    i = i.strip().split(";")
    if i[0] == "single":
        single += get_type(i[-1])
    elif i[0] == "double":
        double += get_type(i[-1])
    elif i[0] == "trip":
        trip += get_type(i[-1])
single = list(set(single))
double = list(set(double))
trip = list(set(trip))
single.sort()
double.sort()
trip.sort()
all_type = single+double+trip

# 统计个数
sac_dict = {}
sac_dict.setdefault("id",[])
sac_dict.setdefault("name",[])
for i in all_type:
    sac_dict.setdefault(i,[0 for j in range(int(len(f)/3))])
row = 0
j = 3
for i in f:
    i = i.strip().split(";")
    if j >= 3:
        row += 1
        sac_dict['id'].append(row)
        sac_dict['name'].append(i[1])
        j = 0
    if len(i) == 3 and i[-1] != '':
        for n in i[-1].split(","):
            sac_dict[n.split(":")[0]][row-1] = int(n.split(":")[-1])
    j += 1
df = pd.DataFrame(sac_dict)

# 导出
df.to_excel('总糖.xlsx',
            sheet_name='count',
            na_rep='NULL')
