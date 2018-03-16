#include <cstdio>  
#include <cstring>  
#include <string>  
#include <cstdlib>  
#include <vector>  
#include <queue>  
#include <algorithm>  
#include <cmath>  
#include <unordered_map>  
#include <set>  
#include <iostream>  
#include <cstdlib>  
#define N 100005  
#define INF 0x7fffffff  
using namespace std;  
int n,m,T;  
long long dp[4005];  
int find(unordered_map<string,int> &hh,string x){  
    sort(x.begin(), x.end());  
    if(hh.find(x) == hh.end())  
        return 0;  
    return hh[x];  
}  
int main(){  
    scanf("%d",&T);  
    for(int c = 0;c<T;){  
        string str;  
        unordered_map<string, int> hh;  
        cin >> m >> n;  
        for(int i = 0;i<m;i++){  
            cin >> str;  
            sort(str.begin(), str.end());  
            if(hh.find(str) == hh.end())  
                hh[str] = 1;  
            else  
                hh[str]++;  
        }  
        printf("Case #%d:",++c);  
        for(int l = 0;l<n;l++){  
            cin >> str;  
            memset(dp, 0, sizeof(dp));  
            for(int i = 0;i<str.size();i++){  
                if(i<20){  
                    if(int tmp = find(hh,str.substr(0,i+1)))  
                        dp[i] += tmp;  
                    dp[i] %= 1000000007;  
                }  
                for(int j = i;j>0 && j>i-20;j--)  
                    if(int tmp = find(hh,str.substr(j,i-j+1))){  
                        dp[i] += dp[j-1]*tmp;  
                        dp[i] %= 1000000007;  
                    }  
            }  
            printf(" %lld",dp[str.size()-1]);  
        }  
        printf("\n");  
    }  
    return 0;  
}  
