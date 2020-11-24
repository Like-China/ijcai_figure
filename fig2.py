# Figure 2
import matplotlib.pyplot as plt

x = [0, 0, 5, 5, 0, 5, 10, 10, 5]
y = [0, 3, 3, 0, 0, 3, 0,  3, 3]
n = ["$v_3$", "$v_1$", "$v_2$", "$v_5$", "", "", "$v_6$", "$v_3$", ""]


x1 = [0, 0, 5, 10]
y1 = [0, 3, 3,  0]
n1 = ["v3", "v1",  "v2",   "v6"]

#drop
# x2 = [ 5, 0]
# y2 = [ 3, 0]
# n2 = ["v2",  "v3"]

# # add
# x2 = [5, 10, 10]
# y2= [3,  3 ,0]
# n2 = ["v2", "v3", "v6"]


# swap
x2 = [0, 5, 5]
y2 = [0, 0, 3]
n2 = ["v3", "v5", "v2"]

fig1 = plt.gcf()
fig,ax=plt.subplots()
plt.axis('off')
ax.scatter(x, y, s=300, color="black", alpha=1)
ax.plot(x, y, color="black", linewidth=5)
ax.plot(x1,y1, color="blue", linewidth=10, alpha=0.7)
ax.plot(x2,y2, color="red", linewidth=10,alpha=0.7, ls="--")

plt.xlim(-1, 11)
plt.ylim(-1, 4)


xx = [0, 5, 10, 0, 5, 10]
yy = [3, 3, 3, 0, 0,  0]
nn = ["$v_1$", "$v_2$", "$v_3$","$v_4$", "$v_5$", "$v_6$"]

for i, txt in enumerate(nn):
    if(i < 3):
        plt.text(xx[i]-0.6, yy[i]+0.5, txt, fontsize=50)
    else:
        plt.text(xx[i]-0.6, yy[i]-1, txt, fontsize=50)
plt.show()
fig.savefig(r'C:\Users\likem\Desktop\design\latex\IJCAI20\swap.png', dpi=200)