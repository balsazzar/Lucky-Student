import random
name=['ang.cunrong.kleon@dhs.sg', 'ang.junming@dhs.sg', 'ang.sweechow@dhs.sg',
      'au.jiaying@dhs.sg', 'chin.yongchen@dhs.sg', 'chong.jiale.nicholas@dhs.sg',
      'chong.jiamin.desirae@dhs.sg', 'chua.yiqi@dhs.sg', 'foo.lexian.felicia@dhs.sg',
      'gn.jingwen.bellerie@dhs.sg', 'goh.jiaying1@dhs.sg', 'kou.yongkang@dhs.sg',
      'lee.wenhao.damien@dhs.sg', 'li.jinjie@dhs.sg', 'lim.kaixin.sheena@dhs.sg',
      'lim.mingmin.michelle@dhs.sg', 'lim.tjionghann@dhs.sg', 'loi.xinyi.audrey@dhs.sg',
      'ng.cheryl@dhs.sg', 'ng.xingyu@dhs.sg', 'quek.jiaqi@dhs.sg',
      'shi.changxiao@dhs.sg', 'tan.chuan@dhs.sg', 'tan.meizi.sherene@dhs.sg',
      'wong.jieyu.jade@dhs.sg', 'yan.hongyao.alvin@dhs.sg', 'zeng.jin@dhs.sg',
      'zhu.siyi@dhs.sg']

gender=['M', 'M', 'M', 'F', 'M', 'M', 'F', 'F', 'F', 'F', 'F', 'M', 'M', 'F',
        'F', 'F', 'F', 'F', 'F', 'M', 'F', 'F', 'M', 'F', 'F', 'M', 'F', 'F']

member=[0,0,0,0,0,0,0,0,1,0,1,1,2,0,0,0,0,0,1,0,0,0,1,0,0,1,0,0]

# main

#distributing chance
chance=[1 for i in range(len(gender))]
for a in range(len(name)):
    if name[a] == 'lee.wenhao.damien@dhs.sg':
        chance[a] *= 2
    if gender[a] == 'F':
        chance[a] *= 2
    if member[a] == 0:
        chance[a] *= 2
        
#choose lucky!
b = -100
counter = 0
for a in range(len(name)):
    if chance[a] > 0:
        counter += 1
while counter > 3:
    if b == -9:
        b -= 1
    for a in range(len(name)):
        if chance[a] < random.randint(b,5):
            chance[a] -= 1
    b += 1
    if chance.count(4) + chance.count(3) + chance.count(2) + chance.count(1) < 3:
        for a in range(len(name)):
            chance[a] += 1
    counter = 0
    for a in range(len(name)):
        if chance[a] > 0:
            counter += 1

#Get name!
for a in range(len(name)):
    if chance[a] > 0:
        print(name[a])
