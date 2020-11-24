import matplotlib.pyplot as plt
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
e = [0.0002, 0.0004, 0.0006, 0.0008, 0.001]



fig1 = plt.gcf()
TGTime=[571, 460, 435, 416, 392]
NYTime = [1284, 816, 790, 568, 561]
plt.plot(e, NYTime, markes[1], label='NY', ms=startSize)
plt.plot(e, TGTime, markes[2], label='TG', ms=startSize)
plt.xlabel("\u0454 (10e-4)", xFont)
plt.ylabel("CPU Time(s)",  yFont)
plt.xticks([0.0002, 0.0004, 0.0006, 0.0008, 0.001], [2, 4, 6, 8, 10])
plt.yticks([100, 600, 1100, 1600], [0.1, 0.6, 1.1, 1.6])
plt.tick_params(labelsize=tickSize)
plt.legend(prop=legendFont, frameon=False)
plt.show()
fig1.savefig(r'D:\grade42\AAAI\imgs\fig5_time.png', dpi=200)


fig1 = plt.gcf()
TGCost=[317797/10e4, 317879/10e4, 318004/10e4, 318127/10e4, 318306/10e4]
NYCost = [156526/10e4, 156953/10e4, 157206/10e4, 159279/10e4, 160979/10e4]
plt.plot(e, NYCost, markes[1], label='NY', ms=startSize)
plt.plot(e, TGCost, markes[2], label='TG', ms=startSize)
plt.xlabel("\u0454 (10e-4)", xFont)
plt.ylabel("TT(Π) (10e4)",  yFont)
plt.legend(prop=legendFont, frameon=False)
plt.xticks(e, [2, 4, 6, 8, 10])
plt.yticks([1.2, 1.7, 2.5, 3.3, 4.0], ['', 1.7, 2.2, 2.7, 3.2, ''])
plt.tick_params(labelsize=tickSize)
plt.show()
fig1.savefig(r'D:\grade42\AAAI\imgs\fig5_cost.png', dpi=200)







