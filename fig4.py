# Figure 4
import matplotlib.pyplot as plt

###  TG路网逼近算法有无 prune 比较
font = {'family' : 'Times New Roman',
'weight' : '1',
'size'   : 30,
}
font1 = {'family' : 'Times New Roman',
'weight' : '1',
'size'   : 40,
}
font2 = {'family' : 'Times New Roman',
'weight' : '1',
'size'   : 50,
}
fig1 = plt.gcf()
eplision  = [0.02, 0.04 ,0.06 ,0.08 ,0.10]
tg = [820, 814, 780, 764, 685]
ny = [748, 717, 640, 612, 605]

markes = ['-x', '-s', '-^']
plt.plot(eplision, tg, markes[1], label='TG', ms=20)
plt.plot(eplision, ny, markes[2], label='NYN', ms=20)
plt.xlabel(u'\u0454', font2)
plt.ylabel("CPU Time(ms)",  font1)
# plt.xticks(eplision, eplision)
plt.xticks([0.02, 0.06 ,0.10], [0.02, 0.06 ,0.10])
plt.yticks([500,600, 700, 800], ['',600, 700, 800])
plt.tick_params(labelsize=30)
plt.legend(prop=font, frameon=False)
plt.show()
fig1.savefig(r'C:\Users\likem\Desktop\design\paper\editorial feedback\V0\pic\ApproxRatioTime.png', dpi=200)


fig1 = plt.gcf()
cost2 = [6737/3616, 6957/3616, 7051/3616, 7250/3616, 7452/3616]
cost3 = [10623/5562, 10883/5562, 11489/5562, 11928/5562, 12018/5562]
markes = ['-p', '-s', '-^']
plt.plot(eplision, cost2, markes[1], label='TG', ms=20)
plt.plot(eplision, cost3, markes[2], label='NYN', ms=20)
# plt.xlabel(u'\u0190', font1)
plt.xlabel(u'\u0454', font2)
plt.ylabel("Approx-Ratio*",  font1)
plt.legend(prop=font, frameon=False)
# plt.xticks(eplision, eplision)
plt.xticks([0.02, 0.06 ,0.10], [0.02, 0.06 ,0.10])
plt.yticks([1.9, 2.0, 2.1, 2.2,2.3], [1.9, 2.0, 2.1, 2.2,''])
plt.tick_params(labelsize=30)
plt.show()
fig1.savefig(r'C:\Users\likem\Desktop\design\paper\editorial feedback\V0\pic\ApproxRatio.png', dpi=200)







