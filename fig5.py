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
userCount = [2000,4000,6000,8000,10000]
time2 = [537/1000, 1309/1000, 4012/1000, 6123/1000, 9640/1000]
time3 = [109/1000, 198/1000, 357/1000, 587/1000, 952/1000]

markes = ['-x', '-s', '-^']
plt.plot(userCount, time2, markes[1], label='Ref-Alg*', ms=20)
plt.plot(userCount, time3, markes[2], label='Ref-Alg', ms=20)
plt.xlabel("|Q|", font2)
plt.ylabel("CPU Time(s)",  font1)
# plt.yticks([200, 400, 600, 800, 1000], [200, 400, 600, 800, 1000])
plt.xticks([2000, 6000, 10000], [2000, 6000, 10000])
plt.tick_params(labelsize=30)
plt.legend(prop=font, frameon=False,loc=2)
plt.show()
fig1.savefig(r'C:\Users\likem\Desktop\design\paper\editorial feedback\V0\pic\TGApproxTime.png', dpi=200)


fig1 = plt.gcf()
cost2 = [6033/10e4, 17784/10e4, 28700/10e4, 41350/10e4, 44830/10e4]
cost3 = [6061/10e4, 18084/10e4, 29773/10e4, 42551/10e4, 45839/10e4]
markes = ['-p', '-s', '-^']
plt.plot(userCount, cost2, markes[1], label='Ref-Alg*', ms=20)
plt.plot(userCount, cost3, markes[2], label='Ref-Alg', ms=20)
plt.xlabel("|Q|", font2)
plt.ylabel("GT (10^4 h)",  font1)
plt.legend(prop=font, frameon=False, loc=2)
plt.xticks([2000, 6000, 10000], [2000, 6000, 10000])
plt.yticks([0.2, 0.4, 0.6,0.7],[0.2, 0.4, 0.6,''])
plt.tick_params(labelsize=30)
plt.show()
fig1.savefig(r'C:\Users\likem\Desktop\design\paper\editorial feedback\V0\pic\TGApproxCost.png', dpi=200)


###  NY路网逼近算法有无 prune 比较
fig1 = plt.gcf()
userCount = [4000,8000,12000,16000,20000]
time2 = [1579/1000, 4416/1000, 7319/1000, 12263/1000, 20890/1000]
time3 = [234/1000, 525/1000, 792/1000, 1173/1000, 1684/1000]
plt.plot(userCount, time2, markes[1], label='Ref-Alg*', ms=20)
plt.plot(userCount, time3, markes[2], label='Ref-Alg', ms=20)
plt.xlabel("|Q|", font2)
plt.ylabel("CPU Time(s)",  font1)
plt.xticks([4000, 12000, 20000], [4000, 12000, 20000])
# plt.yticks([400, 800, 1200, 1600, 2000], [400, 800, 1200, 1600, 2000])
plt.tick_params(labelsize=30)
plt.legend(prop=font, frameon=False,loc=2)
plt.show()
fig1.savefig(r'C:\Users\likem\Desktop\design\paper\editorial feedback\V0\pic\NYApproxTime.png', dpi=200)

fig1 = plt.gcf()
cost2 = [14010/10e4, 39880/10e4, 65542/10e4, 99120/10e4, 119070/10e4]
cost3 = [14242/10e4, 40043/10e4, 66051/10e4, 99300/10e4, 119671/10e4]
markes = ['-p', '-s', '-^']
plt.plot(userCount, cost2,markes[1], label='Ref-Alg*', ms=20)
plt.plot(userCount, cost3, markes[2], label='Ref-Alg', ms=20)
plt.xlabel("|Q|", font2)
plt.ylabel("GT (10^4 h)",  font1)
plt.legend(prop=font, frameon=False,loc=2)
plt.xticks([4000, 12000, 20000], [4000, 12000, 20000])
plt.yticks([0.5,1.0,1.5],[0.5,1.0,1.5])
plt.tick_params(labelsize=30)
plt.show()
fig1.savefig(r'C:\Users\likem\Desktop\design\paper\editorial feedback\V0\pic\NYApproxCost.png', dpi=200)






