// inverse 
#define ll long long
ll MOD=1e9+7;
ll inverse(long long a,long long b,long long n,long long m){
    if(a==1){
        return n;
    }
    if(a<b){
        long long x=b/a;
        m+=(x*n);
        m=m%MOD;
        b=b%a;
        return inverse(a,b,n,m);
    }
    else if(b==1){
        return(MOD-m);
    }
    else{
        long long x=a/b;
        n+=(x*m);
        n=n%MOD;
        a=a%b;
        return inverse(a,b,n,m);
    }
}