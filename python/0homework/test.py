#encoding:utf-8

#case1

# #行
# for i in range(1,10):
#     m = []
#     #列
#     for j in range(1,i+1):
#         str='%s*%s=%s'%(j,i,j*i)
#         m.append(str)
#     print (m)

#case2
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


#case3
# print '\n'.join([' '.join(['%s*%s=%-2s' % (y,x,x*y) for y in range(1,x+1)]) for x in range(1,10)])

# case4
for i in range(1,10):
    print #行回车
    for j in range(1,i+1):
        print "%d*%d=%-2s"%(j,i,i*j), #python2下，最后加逗号实现不换行
    # print

#case5
# print '\n'.join( ' '.join( "%d*%d=%-2s" %(y,x,x*y) for y in range(1,x+1)) for x in range(1,10))
#
# #case6
# for i in xrange(1, 10):
#     print " ".join(map(lambda x: "%s*%s=%s" % (i, x, i * x), range(1, i + 1)))

#case7
# print'\n'.join([''.join([('AndyLove'[(x-y)%8]if((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3<=0 else' ')for x in range(-30,30)])for y in range(15,-15,-1)])



# print '\n'.join(map(lambda x:' '.join(map(lambda y: "%s x %s = %s" % (x, y, x * y), range(1,10))), range(1,10)))

# l=[1,2,3,4]
# print filter(lambda x: x>3, l)


# print reduce(lambda x, y: x+y,  range(1, 10))

# print  [i*j for i in range(1, 10) for j in range(1, i+1)]

# print map(lambda x, y: x*y, range(1, 10), range(1, 10))

# print '\n'.join([' '.join(['%s*%s=%-2s' % (y,x,x*y) for y in range(1,x+1)]) for x in range(1,10)])

# print reduce(lambda x, y: x-y, (1, 2, 3, 4, 5), 20)

# print  str = ['%s*%s=%s'%(j,i,j*i) for i in range(1,10) for j in range(1,i+1)]

#
# for x in range(1,10):
#     print #行回车
#     for y in range(1,x+1):
#         print("%d*%d=%-2s"%(y,x,x*y)  )  #注意逗号
#
# print 'I','love','you.'