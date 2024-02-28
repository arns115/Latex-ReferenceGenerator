#include <iostream>
#include <vector>
#include <stack>
using namespace std;
//dfs
void dfs(){
    bool deb=true;
    int n, m; cin>>n>>m;
    vector<vector<int>> adj(n+1);
    for(int i=0; i<m; i++){
        int a,b; cin>>a>>b;
        adj[a].push_back(b);
        adj[b].push_back(a);
    }
    vector<bool> visited(n+1, 0);
    
    stack<int> s;
    for(int i=1; i<=n; i++){
        if(visited[i]){ continue; }
        s.push(i);
        
        while(!s.empty()){
            int u=s.top(); s.pop();
            if(visited[u]){ continue; }
            if(deb) cout<<u<<" ";
            visited[u] = true;
            for(int v:adj[u]){
                if(visited[v]){ continue; }
                s.push(v);
            }
            
        }
        if(deb) cout<<endl;
    }
}

int main(){
    dfs();
}
