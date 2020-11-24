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
userSizes = [2000, 4000, 6000, 8000, 10000]


# NY路网
fig1 = plt.gcf()
NYTime=[699, 1125, 1657, 2136, 2719]
NYTimeNoPC = [891, 1585, 2267, 3066, 3693]
plt.plot(userSizes, NYTime, markes[1], label='SBP', ms=startSize)
plt.plot(userSizes, NYTimeNoPC, markes[2], label='SBP*PC', ms=startSize)
plt.xlabel("|Q|", xFont)
plt.ylabel("CPU Time(s)",  yFont)
plt.xticks([2000, 6000, 10000], [2000, 6000, 10000])
plt.yticks([1000, 2000, 3000,4000,4500], [1.0,2.0,3.0,4.0,''])
plt.tick_params(labelsize=tickSize)
plt.legend(prop=legendFont, frameon=False)
plt.show()
fig1.savefig(r'D:\grade42\AAAI\imgs\fig6_NY.png', dpi=200)

# TG路网
userCount = [4000, 8000, 12000, 16000, 20000]
fig1 = plt.gcf()
TGTime= [909, 1813, 2839, 3616, 4648]
TGTimeNoPC =  [965, 1900, 2899, 3620, 4765]
plt.plot(userCount, TGTime, markes[1], label='SBP', ms=startSize)
plt.plot(userCount, TGTimeNoPC, markes[2], label='SBP*PC', ms=startSize)
plt.xlabel("|Q|", xFont)
plt.ylabel("CPU Time(s)",  yFont)
plt.xticks([4000, 12000, 20000], [4000, 12000, 20000])
plt.yticks([1500, 2500, 3500, 4500], [1.5, 2.5, 3.5, 4.5])
plt.tick_params(labelsize=tickSize)
plt.legend(prop=legendFont, frameon=False)
plt.show()
fig1.savefig(r'D:\grade42\AAAI\imgs\fig6_TG.png', dpi=200)







