## Figure 7
import matplotlib.pyplot as plt

###  TG路网不同算法随用户数目变化下的最差运行时间
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
time1 = [76, 80, 105, 198, 244]
time2 = [67, 110, 125, 234, 275]
time3 = [131, 211, 438, 789, 1138]

markes = ['-p', '-s', '-^']
plt.plot(userCount, time1, markes[0], label='Ind-Alg', ms=20)
plt.plot(userCount, time2, markes[1], label='Gre-Alg', ms=20)
plt.plot(userCount, time3, markes[2], label='Ref-Alg', ms=20)
plt.xlabel("|Q|", font2)
plt.ylabel("CPU Time(ms)",  font1)
plt.xticks([2000, 6000, 10000], [2000, 6000, 10000])
plt.yticks([200, 600,  1000, 1400, 1800,2100], [200, 600,  1000, 1400, 1800,''])
plt.tick_params(labelsize=30)
plt.legend(prop=font, frameon=False, loc=2)
plt.show()
fig1.savefig(r'C:\Users\likem\Desktop\design\paper\editorial feedback\V0\pic\TGWorstTime.png', dpi=200)

###  NY路网不同算法随用户数目变化下的最差运行时间
fig1 = plt.gcf()
userCount = [4000,8000,12000,16000,20000]
time1 = [337, 400, 490, 718, 917]
time2 = [345, 445, 582, 848, 1118]
time3 = [399, 935, 1235, 1796, 2217]
plt.plot(userCount, time1, markes[0], label='Ind-Alg', ms=20)
plt.plot(userCount, time2, markes[1], label='Gre-Alg', ms=20)
plt.plot(userCount, time3, markes[2], label='Ref-Alg', ms=20)
plt.xlabel("|Q|", font2)
plt.ylabel("CPU Time(ms)",  font1)
plt.xticks([4000, 12000, 20000], [4000, 12000, 20000])
plt.yticks([400,  1200,  2000, 2800, 3600,4400], [400,  1200,  2000, 2800, 3600,''])
plt.tick_params(labelsize=30)
plt.legend(prop=font, frameon=False, loc=2)
plt.show()
fig1.savefig(r'C:\Users\likem\Desktop\design\paper\editorial feedback\V0\pic\NYWorstTime.png', dpi=200)

##  TG路网不同算法随用户数目变化下的 最差提升损失
fig1 = plt.gcf()
userCount = [2000,4000,6000,8000,10000]
cost1 = [5487/10e4, 20109/10e4, 53344/10e4, 79129/10e4, 133555/10e4]
cost2 = [5434/10e4, 18908/10e4, 43322/10e4, 70070/10e4, 115237/10e4]
cost3 = [5434/10e4, 18084/10e4, 39773/10e4, 60551/10e4, 76839/10e4]
plt.plot(userCount, cost1, markes[0], label='Ind-Alg', ms=20)
plt.plot(userCount, cost2, markes[1], label='Gre-Alg', ms=20)
plt.plot(userCount, cost3, markes[2], label='Ref-Alg', ms=20)
plt.xlabel("|Q|", font2)
plt.ylabel("GT (10^4 h)",  font1)
plt.legend(prop=font, frameon=False)
plt.xticks([2000, 6000, 10000], [2000, 6000, 10000])
plt.yticks([0.1, 0.6, 1.1, 1.6,1.8],[0.1, 0.6, 1.1, 1.6,''])
plt.tick_params(labelsize=30)
plt.show()
fig1.savefig(r'C:\Users\likem\Desktop\design\paper\editorial feedback\V0\pic\TGWorstBoostingCost.png', dpi=200)

###  NY路网不同算法随用户数目变化下的运行时间
fig1 = plt.gcf()
userCount = [4000,8000,12000,16000,20000]
cost1 = [16279/10e4, 50614/10e4, 100589/10e4, 143922/10e4, 255009/10e4]
cost2 = [15403/10e4, 44028/10e4, 88452/10e4, 120941/10e4, 211328/10e4]
cost3 = [15242/10e4, 40043/10e4, 66051/10e4, 98000/10e4, 139671/10e4]
plt.plot(userCount, cost1, markes[0], label='Ind-Alg', ms=20)
plt.plot(userCount, cost2,markes[1], label='Gre-Alg', ms=20)
plt.plot(userCount, cost3, markes[2], label='Ref-Alg', ms=20)
plt.xlabel("|Q|", font2)
plt.ylabel("GT (10^4 h)",  font1)
plt.legend(prop=font, frameon=False)
plt.xticks([4000, 12000, 20000], [4000, 12000, 20000])
plt.yticks([0.5, 1.0, 1.5, 2.0, 2.5,3.2], [0.5, 1.0, 1.5, 2.0, 2.5,''])
plt.tick_params(labelsize=30)
plt.show()
fig1.savefig(r'C:\Users\likem\Desktop\design\paper\editorial feedback\V0\pic\NYWorstBoostingCost.png', dpi=200)






