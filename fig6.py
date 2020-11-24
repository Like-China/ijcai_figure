## 绘制不同算法的运行时间比较
import matplotlib.pyplot as plt

###  用等式1，alpha 变化, TG路网
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
## 用时
alpha = [0.02,0.04,0.06,0.08,0.10]
time1 = [255, 240, 229, 229, 242]
time2 = [286, 302, 284, 265, 259]
time3 = [758, 1015, 1406, 1439, 1406]
markes = ['-p', '-s', '-^']
plt.plot(alpha, time1, markes[0], label='Ind-Alg', ms=20)
plt.plot(alpha, time2, markes[1], label='Gre-Alg', ms=20)
plt.plot(alpha, time3, markes[2], label='Ref-Alg', ms=20)
plt.xlabel(u'\u03B1', font2)
plt.ylabel("CPU Time(ms)",  font1)
plt.legend(prop=font, frameon=False)
# plt.xticks(alpha, alpha)
plt.xticks([0.02,0.06,0.10],[0.02,0.06,0.10])
plt.tick_params(labelsize=30)
plt.show()
fig1.savefig(r'C:\Users\likem\Desktop\design\paper\editorial feedback\V0\pic\TGFunction1CompareTime.png', dpi=200)

fig1 = plt.gcf()
cost1 = [20464/10e4, 52053/10e4, 73234/10e4, 94938/10e4, 117576/10e4]
cost2 = [18565/10e4, 43725/10e4, 59818/10e4, 76136/10e4, 92695/10e4]
cost3 = [17242/10e4, 39196/10e4, 50818/10e4, 66453/10e4, 70023/10e4]
markes = ['-p', '-s', '-^']
plt.plot(alpha, cost1, markes[0], label='Ind-Alg', ms=20)
plt.plot(alpha, cost2,markes[1], label='Gre-Alg', ms=20)
plt.plot(alpha, cost3, markes[2], label='Ref-Alg', ms=20)
plt.xlabel(u'\u03B1', font2)
plt.ylabel("GT (10^4 h)",  font1)
plt.legend(prop=font, frameon=False)
# plt.xticks(alpha, alpha)
plt.xticks([0.02,0.06,0.10],[0.02,0.06,0.10])
plt.yticks([0.6,1.2,1.7,1.9],[0.6,1.2,1.7,''])
plt.tick_params(labelsize=30)
plt.show()
fig1.savefig(r'C:\Users\likem\Desktop\design\paper\editorial feedback\V0\pic\TGFunction1CompareCost.png', dpi=200)


###  ###  用等式2，alpha 变化, TG路网
partial = [20,40,60,80,100]
fig1 = plt.gcf()
time1 = [245, 241, 230, 223, 210]
time2 = [303, 300, 301, 290, 282]
time3 = [1125,1071, 1105,947, 913]
markes = ['-p', '-s', '-^']
plt.plot(partial, time1, markes[0], label='Ind-Alg', ms=20)
plt.plot(partial, time2, markes[1], label='Gre-Alg', ms=20)
plt.plot(partial, time3, markes[2], label='Ref-Alg', ms=20)
# plt.xlabel(u'\u03c3', font2)
plt.xlabel(u'\u03c6', font2)
plt.ylabel("CPU Time(ms)",  font1)
plt.legend(prop=font, frameon=False)
# plt.xticks(partial, partial)
plt.xticks([20,60,100], [20,60,100])
plt.tick_params(labelsize=30)
plt.show()
fig1.savefig(r'C:\Users\likem\Desktop\design\paper\editorial feedback\V0\pic\TGFunction2CompareTime.png', dpi=200)


fig1 = plt.gcf()
cost1 = [29306/10e4, 17210/10e4, 13432/10e4, 12073/10e4, 11442/10e4]
cost2 = [21367/10e4 , 14290/10e4, 12144/10e4, 11357/10e4, 11039/10e4]
cost3 = [20463/10e4, 14292/10e4, 12144/10e4, 11358/10e4, 11039/10e4]
markes = ['-p', '-s', '-^']
plt.plot(partial, cost1, markes[0], label='Ind-Alg', ms=20)
plt.plot(partial, cost2, markes[1], label='Gre-Alg', ms=20)
plt.plot(partial, cost3, markes[2], label='Ref-Alg', ms=20)
# plt.xlabel(u'\u03c3', font2)
plt.xlabel(u'\u03c6', font2)
plt.ylabel("GT (10^4 h)",  font1)
plt.legend(prop=font, frameon=False)
# plt.xticks(partial, partial)
plt.xticks([20,60,100], [20,60,100])
plt.tick_params(labelsize=30)
plt.show()
fig1.savefig(r'C:\Users\likem\Desktop\design\paper\editorial feedback\V0\pic\TGFunction2CompareCost.png', dpi=200)





