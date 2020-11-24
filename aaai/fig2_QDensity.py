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
queryDensity = [20, 40, 60, 80, 100]



fig1 = plt.gcf()
TGTime=[256, 322, 474, 595, 899]
NYTime = [469, 614, 962, 1213, 1458]
plt.plot(queryDensity, NYTime, markes[1], label='NY', ms=startSize)
plt.plot(queryDensity, TGTime, markes[2], label='TG', ms=startSize)
plt.xlabel("Query arrival rate", xFont)
plt.ylabel("CPU Time(s)",  yFont)
plt.xticks([20,60,100], [20,60,100])
plt.yticks([500, 900, 1300],[0.5, 0.9, 1.3])
plt.tick_params(labelsize=tickSize)
plt.legend(prop=legendFont, frameon=False)
plt.show()
fig1.savefig(r'D:\grade42\AAAI\imgs\fig2_time.png', dpi=200)


fig1 = plt.gcf()
TGCost=[288330/10e4, 299407/10e4, 306064/10e4, 310012/10e4, 312765/10e4]
NYCost = [148133/10e4, 155227/10e4, 158530/10e4, 160933/10e4, 162493/10e4]
plt.plot(queryDensity, NYCost, markes[1], label='NY', ms=startSize)
plt.plot(queryDensity, TGCost, markes[2], label='TG', ms=startSize)
plt.xlabel("Query arrival rate", xFont)
plt.ylabel("TT(Π) (10e4)",  yFont)
plt.legend(prop=legendFont, frameon=False)
plt.xticks([20,60,100], [20,60,100])
plt.tick_params(labelsize=tickSize)
plt.show()
fig1.savefig(r'D:\grade42\AAAI\imgs\fig2_cost.png', dpi=200)







