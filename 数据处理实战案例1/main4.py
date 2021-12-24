from tqdm import tqdm

with open('rating.txt','r',encoding='utf-8')as f:
    content = f.readlines()
list_target = []
list_80 = []
list_20 = []
for c in tqdm(content):
    c = str(c)
    c = c.strip('\n')
    c = c.split(' ')
    target = str(c[0])
    list_target.append(target)
    neirong = c[1:]
    bai_80 = int(len(neirong) * 0.8)
    nei_80 = neirong[:bai_80]
    list_80.append(nei_80)
    nei_20 = neirong[bai_80:]
    list_20.append(nei_20)


for i,o,p in zip(list_target,list_80,list_20):
    a = o.insert(0,i)
    b = p.insert(0,i)
    with open('train.txt','a',encoding='utf-8')as f:
        c = ' '.join(o)
        f.write(c+'\n')
    with open('test.txt','a',encoding='utf-8')as f:
        d = ' '.join(p)
        f.write(d+'\n')