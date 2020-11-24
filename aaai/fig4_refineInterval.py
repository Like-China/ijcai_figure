import matplotlib.pyplot as plt

###  TG路网逼近算法有无 prune 比较
#
legendFont = {'family' : 'Times New Roman',
'weight' : '1',
'size'   : 30,
}
yFont = {'family' : 'Times New Roman',
'weight' : '1',
'size'   : 30,
}
xFont = {'family' : 'Times New Roman',
'weight' : '1',
'size'   : 30,
}
# 连线标星大小
startSize = 20
tickSize = 30
markes = ['-x', '-s', '-^', '-p']
intevals = [1, 2, 3, 4, 5]



fig1 = plt.gcf()
TGTime=[204, 475, 814, 1144, 1268]
NYTime = [327, 676, 990, 1396, 1814]
plt.plot(intevals, NYTime, markes[1], label='NY', ms=startSize)
plt.plot(intevals, TGTime, markes[2], label='TG', ms=startSize)
plt.xlabel("Refine Interval (T)", xFont)
plt.ylabel("CPU Time(s)",  yFont)
plt.xticks([1, 2, 3, 4, 5], [1, 2, 3, 4, 5])
plt.yticks([500,1000,1500,2000], [0.5,1.0,1.5,2.0])
plt.tick_params(labelsize=tickSize)
plt.legend(prop=legendFont, frameon=False)
plt.show()
fig1.savefig(r'D:\grade42\AAAI\imgs\fig4_time.png', dpi=200)


fig1 = plt.gcf()
TGCost=[407670/10e4, 406579/10e4, 405886/10e4, 404806/10e4, 404740/10e4]
NYCost = [272465/10e4, 268420/10e4, 267761/10e4, 267383/10e4, 266930/10e4]
plt.plot(intevals, NYCost, markes[1], label='NY', ms=startSize)
plt.plot(intevals, TGCost, markes[2], label='TG', ms=startSize)
plt.xlabel("Refine Interval (T)", xFont)
plt.ylabel("TT(Π) (10e4)",  yFont)
plt.legend(prop=legendFont, frameon=False)
plt.xticks([1, 2, 3, 4, 5], [1, 2, 3, 4, 5])
plt.yticks([2.0, 2.5, 3.2, 3.9, 4.6], ['', 2.5, 3.2, 3.9, 4.6])
plt.tick_params(labelsize=tickSize)
plt.show()
fig1.savefig(r'D:\grade42\AAAI\imgs\fig4_cost.png', dpi=200)







