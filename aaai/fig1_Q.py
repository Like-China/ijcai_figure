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
userCount = [2000, 4000, 6000, 8000, 10000]
indTime=[118, 259, 481, 769, 1129]
sbpTime=[699, 1125, 1657, 2136, 2719]
sbpsaTime = [1042, 1909, 2777, 3731, 4710]
sbpdaTime = [1090, 2004, 3152, 4305, 5557]
plt.plot(userCount, indTime, markes[0], label='Ind', ms=startSize)
plt.plot(userCount, sbpTime, markes[1], label='SBP', ms=startSize)
plt.plot(userCount, sbpsaTime, markes[2], label='SBP*SA', ms=startSize)
plt.plot(userCount, sbpdaTime, markes[3], label='SBP*DA', ms=startSize)
plt.xlabel("|Q|", xFont)
plt.ylabel("CPU Time(s)",  yFont)
# plt.yticks([200, 400, 600, 800, 1000], [200, 400, 600, 800, 1000])
plt.xticks([2000, 6000, 10000], [2000, 6000, 10000])
plt.yticks([2000, 5000, 8000, 11000], [2, 5, 8, 11])
plt.tick_params(labelsize=tickSize)
plt.legend(prop=legendFont, ncol=2, handlelength=0, frameon=False, loc=2)
plt.show()
fig1.savefig(r'D:\grade42\AAAI\imgs\fig1_NYC_time.png', dpi=200)


fig1 = plt.gcf()
indCost = [276854/10e4, 625880/10e4, 993751/10e4, 1365409/10e4, 1738609/10e4]
sbpCost=[157206/10e4, 305838/10e4, 447235/10e4, 589316/10e4, 740579/10e4]
subsaCost = [161200/10e4, 315884/10e4, 465396/10e4, 615217/10e4, 772968/10e4]
sbpdaCost = [161429/10e4, 317772/10e4, 469967/10e4, 622328/10e4, 783199/10e4]
plt.plot(userCount, indCost, markes[0], label='Ind', ms=startSize)
plt.plot(userCount, sbpCost, markes[1], label='SBP', ms=startSize)
plt.plot(userCount, subsaCost, markes[2], label='SBP*SA', ms=startSize)
plt.plot(userCount, sbpdaCost, markes[3], label='SBP*DA', ms=startSize)
plt.xlabel("|Q|", xFont)
plt.ylabel("TT(Π) (10e4)",  yFont)
plt.legend(prop=legendFont, ncol=2, handlelength=0, frameon=False, loc=2)
plt.xticks([2000, 6000, 10000], [2000, 6000, 10000])
plt.yticks([4, 12, 20, 28, 30], [4, 12, 20, 28, ''])
plt.tick_params(labelsize=tickSize)
plt.show()
fig1.savefig(r'D:\grade42\AAAI\imgs\fig1_NYC_cost.png', dpi=200)


###  TGC路网
userCount = [4000, 8000, 12000, 16000, 20000]

fig1 = plt.gcf()
indTime=[148, 361, 691, 1116, 1618]
sbpTime=[623, 1101, 1622, 2076, 2565]
sbpsaTime = [688, 1185, 2163, 3108, 4214]
sbpdaTime = [937, 1873, 2573, 3553, 4446]
plt.plot(userCount, indTime, markes[0], label='Ind', ms=startSize)
plt.plot(userCount, sbpTime, markes[1], label='SBP', ms=startSize)
plt.plot(userCount, sbpsaTime, markes[2], label='SBP*SA', ms=startSize)
plt.plot(userCount, sbpdaTime, markes[3], label='SBP*DA', ms=startSize)
plt.xlabel("|Q|", xFont)
plt.ylabel("CPU Time(s)",  yFont)
plt.xticks([4000, 12000, 20000], [4000, 12000, 20000])
plt.yticks([2000,4000,6000,8000],[2.0,4.0,6.0,8.0])

plt.tick_params(labelsize=tickSize)
plt.legend(prop=legendFont, ncol=2, handlelength=0, frameon=False, loc=2)
plt.show()
fig1.savefig(r'D:\grade42\AAAI\imgs\fig1_TGC_time.png', dpi=200)



fig1 = plt.gcf()
indCost=[407670/10e4, 877533/10e4,1365787/10e4, 1871527/10e4, 2369447/10e4]
sbpCost=[313403/10e4, 614923/10e4,902918/10e4, 1187744/10e4, 1475000/10e4]
subsaCost = [322566/10e4, 638721/10e4, 946535/10e4, 1252110/10e4, 1559487/10e4]
sbpdaCost = [313407/10e4, 615025/10e4, 903113/10e4, 1188126/10e4, 1475519/10e4]
plt.plot(userCount, indCost, markes[0], label='Ind', ms=startSize)
plt.plot(userCount, sbpCost, markes[1], label='SBP', ms=startSize)
plt.plot(userCount, subsaCost, markes[2], label='SBP*SA', ms=startSize)
plt.plot(userCount, sbpdaCost, markes[3], label='SBP*DA', ms=startSize)
plt.xlabel("|Q|", xFont)
plt.ylabel("TT(Π) (10e4)",  yFont)
plt.legend(prop=legendFont, ncol=2, handlelength=0, frameon=False, loc=2)
plt.xticks([4000, 12000, 20000], [4000, 12000, 20000])
plt.yticks([10, 20, 30, 40],[10, 20, 30, 40])
plt.tick_params(labelsize=tickSize)
plt.show()
fig1.savefig(r'D:\grade42\AAAI\imgs\fig1_TGC_cost.png', dpi=200)






