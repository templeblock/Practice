# Input 	
# 2   t
# 5 1     v
# this
# is
# a
# good
# day
# sithsiaodogyad
# 5 3
# pt
# ybsb
# xnydt
# qtpb
# kw
# xnydttbpqtpqb
# yxdtntpbsby
# ptptxytdnsbybpt

# output:
# Case #1: 2
# Case #2: 1 1 1

# V :the size of the monster's vocabulary 
# S :the number of enciphered strings.
#dp problem 

t = int(raw_input())
def Findvocab(hh, x):
    x = sorted(x)
    x = str(x)
    if hh.get(x):
        return hh[x]
    return 0
for c in xrange(0, t):
    size_v, number_s = [int(s) for s in raw_input().split(" ")]
    #set a dict  {'string': value}
    hh = dict()
    ans = []
    for i in xrange(0, size_v):
        vocab = sorted(str(raw_input()))
        vocab = str(vocab)
        hh.setdefault(vocab,0)
        hh[vocab] +=1     
    for l in xrange(0, number_s):
        code = str(raw_input())
        dp = [0]*4005
        for i in xrange(0, len(code)):
            if i < 20:
                tmp = Findvocab(hh, code[0:i+1])
                if tmp:
                    dp[i] +=tmp
                    dp[i] %= 1000000007
            j = i
            while(j > i-20 and j >0):
                tmp = Findvocab(hh, code[j:i+1])
                if tmp:
                    dp[i] +=tmp * dp[j-1]
                    dp[i] %= 1000000007
                j -=1
        ans.append(str(dp[len(code)-1]))
    print "Case #{}: ".format(c+1) + ' '.join(ans)
