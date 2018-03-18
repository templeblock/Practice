#include <cstdio>
#include <cstring>
#include <string>
#include <cstdlib>
#include <vector>
#include <queue>
#include <algorithm>
#include <cmath>
#include <map>
#include <set>
#include <iostream>
#define N 100005
#define INF 0x3fffffff
using namespace std;
int n,m,l,T;
struct node{
    int a,b,w;
}s[1005];
int dp[2][10005];
int st[10005][20];
void makest(int *t){
    int k = log2(double(l+1));
    for(int i = 1;i<=l;i++)
        st[i][0] = t[i];
    for(int j = 1;j<=k;j++)
        for(int i = 1;i+(1<<j)-1<=l;i++)
            st[i][j] = min(st[i][j-1], st[i+(1<<(j-1))][j-1]);
}
int query(int a,int b){
    int k = log2(double(b-a+1));
    return min(st[a][k], st[b-(1<<k)+1][k]);
}
int main(){
    scanf("%d",&T);
    for(int c = 0;c<T;){
        scanf("%d %d %d",&n,&m,&l);
        for(int i = 0;i<n;i++)
            scanf("%d %d %d",&s[i].a,&s[i].b,&s[i].w);
        for(int i = 1;i<=l;i++)
            dp[0][i] = dp[1][i] = INF;
        dp[0][0] = dp[1][0] = 0;
        int a = 0,b = 1;
        for(int i = 0;i<n;i++){
            makest(dp[a]);
            for(int j = l;j>=1;j--){
                dp[b][j] = min(dp[b][j], dp[a][j]);
                if(j>=s[i].a && j<=s[i].b)
                    dp[b][j] = min(dp[b][j], s[i].w);
                int begin = max(1, j-s[i].b);
                int end = j-s[i].a;
                if(begin <= end){
                    int tmp =query(begin, end)+s[i].w;
                    if(tmp <= m)
                    dp[b][j] = min(dp[b][j], query(begin, end)+s[i].w);
                }
            }
            b = 1-b;
            a = 1-a;
        }
        if(dp[a][l] == INF)
            printf("Case #%d: IMPOSSIBLE\n",++c);
        else
            printf("Case #%d: %d\n",++c,dp[a][l]);
    }
    return 0;
}
