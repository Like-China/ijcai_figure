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

fig1 = plt.gcf()
alpha = [1, 2, 3, 4, 5]
NYime=[732,927,1065,1165,1280]
TGime=[661,826, 888,972,1048]
plt.plot(alpha, NYime, markes[1], label='NY', ms=startSize)
plt.plot(alpha, TGime, markes[2], label='TG', ms=startSize)
plt.xlabel("\u03B1", xFont)
plt.ylabel("CPU Time(s)",  yFont)
plt.xticks([1,2,3,4,5],[1,2,3,4,5])
plt.yticks([800,1000,1200,1400],[0.8,1.0,1.2,1.4])
plt.tick_params(labelsize=tickSize)
plt.legend(prop=legendFont, ncol=2, handlelength=0, frameon=False, loc=2)
plt.show()
fig1.savefig(r'D:\grade42\AAAI\imgs\fig3_alpha_time.png', dpi=200)


fig1 = plt.gcf()
NYCost = [166684/10e4, 227882/10e4, 279821/10e4, 324734/10e4, 359320/10e4]
TGCost=[263431/10e4, 342696/10e4, 412414/10e4, 477500/10e4, 536622/10e4]
plt.plot(alpha, NYCost, markes[1], label='NY', ms=startSize)
plt.plot(alpha, TGCost, markes[2], label='TG', ms=startSize)
plt.xlabel("\u03B1", xFont)
plt.ylabel("TT(Π) (10e4)",  yFont)
plt.xticks([1,2,3,4,5],[1,2,3,4,5])
plt.yticks([2,3,4,5],[2.0,3.0,4.0,5.0])
plt.legend(prop=legendFont, ncol=2, handlelength=0, frameon=False, loc=2)
plt.tick_params(labelsize=tickSize)
plt.show()
fig1.savefig(r'D:\grade42\AAAI\imgs\fig3_alpha_cost.png', dpi=200)


###  beta
beta = [1, 1.5, 2, 2.5, 3]

fig1 = plt.gcf()
NYime=[1172, 1193, 1086, 1106, 1100]
TGime=[774, 852, 812, 838, 817]
plt.plot(beta, NYime, markes[1], label='NY', ms=startSize)
plt.plot(beta, TGime, markes[2], label='TG', ms=startSize)
plt.xlabel("\u03B2", xFont)
plt.ylabel("CPU Time(s)",  yFont)
plt.xticks([1.0,1.5,2.0,2.5,3.0], [1.0,1.5,2.0,2.5,3.0])
plt.yticks([800,1000,1200,1400],[0.8,1.0,1.2,1.4])
plt.tick_params(labelsize=tickSize)
plt.legend(prop=legendFont, ncol=2, handlelength=0, frameon=False, loc=2)
plt.show()
fig1.savefig(r'D:\grade42\AAAI\imgs\fig3_beta_time.png', dpi=200)



fig1 = plt.gcf()
NYCost=[251616/10e4, 240394/10e4,227882/10e4, 217060/10e4, 210885/10e4]
TGCost=[446002/10e4, 413354/10e4,385762/10e4, 362551/10e4, 342696/10e4]
plt.plot(beta, NYCost, markes[1], label='NY', ms=startSize)
plt.plot(beta, TGCost, markes[2], label='TG', ms=startSize)
plt.xlabel("\u03B2", xFont)
plt.ylabel("TT(Π) (10e4)",  yFont)
plt.legend(prop=legendFont, ncol=2, handlelength=0, frameon=False, loc=2)
plt.xticks([1.0,1.5,2.0,2.5,3.0], [1.0,1.5,2.0,2.5,3.0])
plt.yticks([2.5,3.5,4.5,5.5],[2.5,3.5,4.5,5.5])
plt.tick_params(labelsize=tickSize)
plt.show()
fig1.savefig(r'D:\grade42\AAAI\imgs\fig3_beta_cost.png', dpi=200)






