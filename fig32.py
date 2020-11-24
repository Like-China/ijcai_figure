## Figure 3
## 绘制不同算法的运行时间比较
import matplotlib.pyplot as plt

###  TG路网不同算法随用户数目变化下的运行时间
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
time1 = [44, 51, 94, 139, 195]
time2 = [39, 61, 110, 171, 235]
time3 = [109, 198, 357, 587, 952]

markes = ['-p', '-s', '-^']
plt.plot(userCount, time1, markes[0], label='Ind-Alg', ms=20)
plt.plot(userCount, time2, markes[1], label='Gre-Alg', ms=20)
plt.plot(userCount, time3, markes[2], label='Ref-Alg', ms=20)
plt.xlabel("|Q|", font2)
plt.ylabel("CPU Time(ms)",  font1)
plt.xticks([2000, 6000, 10000], [2000, 6000, 10000])
plt.yticks([300,  700,  1100, 1600], [300,  700,  1100, ''])
plt.tick_params(labelsize=30)
plt.legend(prop=font, frameon=False,loc=2)
plt.show()
fig1.savefig(r'C:\Users\likem\Desktop\design\paper\editorial feedback\V0\pic\TGTime.png', dpi=200)

###  NY路网不同算法随用户数目变化下的运行时间
fig1 = plt.gcf()
userCount = [4000,8000,12000,16000,20000]
time1 = [95, 181, 328, 444, 619]
time2 = [122, 214, 408, 572, 746]
time3 = [234, 525, 792, 1173, 1684]
plt.plot(userCount, time1, markes[0], label='Ind-Alg', ms=20)
plt.plot(userCount, time2, markes[1], label='Gre-Alg', ms=20)
plt.plot(userCount, time3, markes[2], label='Ref-Alg', ms=20)
plt.xlabel("|Q|", font2)
plt.ylabel("CPU Time(ms)",  font1)
plt.xticks([4000, 12000, 20000], [4000, 12000, 20000])
# plt.yticks([400, 800, 1200, 1600, 2000], [400, 800, 1200, 1600, 2000])
plt.yticks([400,  1200,  2000,3000],[400,  1200,  2000,''])
plt.tick_params(labelsize=30)
plt.legend(prop=font, frameon=False,loc=2)
plt.show()
fig1.savefig(r'C:\Users\likem\Desktop\design\paper\editorial feedback\V0\pic\NYTime.png', dpi=200)







