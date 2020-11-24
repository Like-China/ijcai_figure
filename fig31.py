## figure 3
## GT
import matplotlib.pyplot as plt

###  TG路网不同算法随用户数目变化下的运行时间
fig1 = plt.gcf()
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
userCount = [2000,4000,6000,8000,10000]
cost1 = [7687/10e4, 27109/10e4, 56626/10e4, 99129/10e4, 153555/10e4]
cost2 = [6234/10e4, 20908/10e4, 43343/10e4, 75070/10e4, 115237/10e4]
cost3 = [6061/10e4, 18084/10e4, 29773/10e4, 42551/10e4, 45839/10e4]
markes = ['-p', '-s', '-^']
plt.plot(userCount, cost1, markes[0], label='Ind-Alg', ms=20)
plt.plot(userCount, cost2, markes[1], label='Gre-Alg', ms=20)
plt.plot(userCount, cost3, markes[2], label='Ref-Alg', ms=20)
plt.xlabel("|Q|", font2)
plt.ylabel("GT (10^4 h)",  font1)
plt.legend(prop=font, frameon=False)
plt.xticks([2000, 6000, 10000], [2000, 6000, 10000])
plt.yticks([0.4, 0.8, 1.2, 1.6,2.2], [0.4, 0.8, 1.2, 1.6,''])
plt.tick_params(labelsize=30)
plt.show()
fig1.savefig(r'C:\Users\likem\Desktop\design\paper\editorial feedback\V0\pic\TGCostWithFunction1.png', dpi=200)

# fig1 = plt.gcf()
# cost1 = [2910/10e4, 7672/10e4, 15826/10e4, 29657/10e4, 54175/10e4]
# cost2 = [2855/10e4, 6592/10e4, 12585/10e4, 21718/10e4, 36517/10e4]
# cost3 = [2855/10e4, 6591/10e4, 10585/10e4, 20615/10e4, 30148/10e4]
# plt.plot(userCount, cost1, markes[0], label='Ind-Alg', ms=20)
# plt.plot(userCount, cost2, markes[1], label='Greed-Alg', ms=20)
# plt.plot(userCount, cost3, markes[2], label='Approx-Alg', ms=20)
# plt.xlabel("|Q|", font1)
# plt.ylabel("GT (10^4 h)",  font1)
# plt.legend(prop=font, frameon=False)
# plt.xticks([2000, 6000, 10000], [2000, 6000, 10000])
# plt.yticks([0.1, 0.2, 0.3, 0.4, 0.5], [0.1, 0.2, 0.3, 0.4, 0.5])
# plt.tick_params(labelsize=30)
# plt.show()
# fig1.savefig(r'C:\Users\likem\Desktop\design\paper\editorial feedback\V0\pic\TGCostWithFunction2.png', dpi=200)

###  NY路网不同算法随用户数目变化下的运行时间
fig1 = plt.gcf()
userCount = [4000,8000,12000,16000,20000]
cost1 = [17279/10e4, 54614/10e4, 112589/10e4, 193922/10e4, 298009/10e4]
cost2 = [14423/10e4, 44028/10e4, 88452/10e4, 150971/10e4, 201328/10e4]
cost3 = [14242/10e4, 40043/10e4, 66051/10e4, 99300/10e4, 119671/10e4]
plt.plot(userCount, cost1, markes[0], label='Ind-Alg', ms=20)
plt.plot(userCount, cost2,markes[1], label='Gre-Alg', ms=20)
plt.plot(userCount, cost3, markes[2], label='Ref-Alg', ms=20)
plt.xlabel("|Q|", font2)
plt.ylabel("GT (10^4 h)",  font1)
plt.legend(prop=font, frameon=False)
plt.xticks([4000, 12000, 20000], [4000, 12000, 20000])
plt.yticks([1.1, 2.1, 3.1,4.2], [1.1, 2.1, 3.1,''])
plt.tick_params(labelsize=30)
plt.show()
fig1.savefig(r'C:\Users\likem\Desktop\design\paper\editorial feedback\V0\pic\NYCostWithFunction1.png', dpi=200)

# fig1 = plt.gcf()
# cost1 = [8620/10e4, 24194/10e4, 58578/10e4, 120226/10e4, 238025/10e4]
# cost2 = [8558/10e4 , 23211/10e4, 52006/10e4, 101397/10e4, 192244/10e4]
# cost3 = [8558/10e4, 22846/10e4, 42538/10e4, 59016/10e4, 102121/10e4]
# plt.plot(userCount, cost1, markes[0], label='Ind-Alg', ms=20)
# plt.plot(userCount, cost2, markes[1], label='Greed-Alg', ms=20)
# plt.plot(userCount, cost3, markes[2], label='Approx-Alg', ms=20)
# plt.xlabel("|Q|", font1)
# plt.ylabel("GT (10^4 h)",  font1)
# plt.legend(prop=font, frameon=False)
# plt.xticks([4000, 12000, 20000], [4000, 12000, 20000])
# plt.yticks([0.1, 1.1, 2.1, 3.1], [0.1, 1.1, 2.1, 3.1])
# plt.tick_params(labelsize=30)
# plt.show()
# fig1.savefig(r'C:\Users\likem\Desktop\design\paper\editorial feedback\V0\pic\NYCostWithFunction2.png', dpi=200)





