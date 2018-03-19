# Input 

# Output 
 
# 2
# 3 8 6
# 3 5 2
# 4 4 3
# 1 2 5
# 3 11 14
# 1 3 4
# 5 5 3
# 2 6 5

# Case #1: 7
# Case #2: IMPOSSIBLE


#T
#N(ropes) M(DOLLAR) L(length)
#(N LINES) A B W
import math

INF = 0x3fffffff  
#class Node(object):
#    def __init__(self, a, b, w):
#        self.a = a
#        self.b = b
#        self.w = w
#st = np.zeros((10005, 20)) 
#dp = np.zeros((2, 10005))
# st = [[0]*20]*10005
# dp = [[0]*10005]*2
st = [[0 for x in xrange(20)] for y in xrange(10005)]
dp = [[0 for x in xrange(10005)] for y in xrange(2)]

def makest(x):
    k = int(math.log((l+1),2))
    for i in range(1, l+1):
        st[i][0] = x[i]
    for j in range(1, k+1):
        i = 1
        while(i + (1<<j) - 1 <=l):
            st[i][j] = min(st[i][j-1], st[i+(1<<(j-1))][j-1])
            i +=1

def query(a, b):
    k = int(math.log((b-a+1),2))
    return min(st[a][k], st[b-(1<<k)+1][k])

t = int(raw_input())
for c in xrange(0, t):
    n, m, l = [int(i) for i in raw_input().split(" ")]
    s = []
    for i in range(n):
        a, b, w = [int(z) for z in raw_input().split(" ")]
        s.append([a, b, w])
#         print(s[i].a, s[i].b, s[i].w)
    for i in range(1, l+1):
        dp[0][i] = INF
        dp[1][i] = INF
    dp[0][0] = 0
    dp[1][0] = 0
    a, b =0, 1
    for i in range(n):
        makest(dp[a])
        for j in range(l, 0, -1):
            dp[b][j] = min(dp[b][j], dp[a][j])
            if j >=s[i][0] and j <=s[i][1] :
                dp[b][j] = min(dp[b][j], s[i][2])
            begin = max(1, j-s[i][1])
            end = j - s[i][0]
            if begin <= end :
                tmp = query(begin, end) + s[i][2]
                if tmp <= m :
                    dp[b][j] = min(dp[b][j], tmp)
    
        b = 1 - b
        a = 1 - a
    
    if dp[a][l] == INF:
        print "Case #{}: {}".format(c+1,'IMPOSSIBLE')
    else:
        print "Case #{}: {}".format(c+1,dp[a][l])
