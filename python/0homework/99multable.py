#encoding:utf-8

# for循环实现99乘法表  case1

# #行
# for i in range(1,10):
#     m = []
#     #列
#     for j in range(1,i+1):
#         str='%s*%s=%s'%(j,i,j*i)
#         m.append(str)
#     print (m)

#case20
#行
# m =''
# for i in range(1,10):
#     #列
#     for j in range(1,i+1):
#         str='%s*%s=%s'%(j,i,j*i)
#         m=m+'\t'+str
#     m=m+'\n'
# print m



#case21
#行
# m =''
# for i in range(1, 10):
#     for j in range(1, i+1):
#         m = m+'%s*%s=%s' % (j, i, j*i)+'\t'
#     m = m+'\n'
# print m

# #case22
# #行
#
# for i in range(1, 10):
#     m = ''
#     for j in range(1, i+1):
#         m = m+'%s*%s=%s' % (j, i, j*i)+'\t'
#     print m

# case23
# 行

# for i in range(1, 10):
#     m = ''
#     for j in range(1, i + 1):
#         m = m + '%s*%s=%s' % (j, i, j * i) + '\t'
#     print m

# # case24
# for i in range(1,10):
#     print #行换行
#     for j in range(1,i+1):
#         print "%d*%d=%-2s"%(j,i,i*j), #python2下，最后加逗号实现不换行



#一行代码实现99乘法表 join
#case30
# print '\n'.join([' '.join(['%s*%s=%-2s' % (y,x,x*y) for y in range(1,x+1)]) for x in range(1,10)])


# case31
# print '\n'.join(' '.join("%d*%d=%-2s" % (y, x, x*y) for y in range(1, x+1)) for x in range(1, 10))


# #case32
# for i in range(1, 10):
#     print " ".join(map(lambda j: "%s*%s=%s" % (i, j, i * j)+'\t', range(1, i + 1)))


#
# 倒叙99乘法表
# case1
# for i in range(1, 10):
#     m = ''
#     for j in range(10-i, 10):
#         m = m+'%s*%s=%s' % (i, j, j*i)+'\t'
#     print m

for i in range(1, 10)[::-1]:
    m = ''
    for j in range(1, i+1):
        m = m+'%s*%s=%s' % (j, i, j*i)+'\t'
    print m
