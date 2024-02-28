//kruskal
int n, m, par[MAX_N];
vector<array<int,3>> edges;
 
int find(int u) {
    return u == par[u] ? u : par[u] = find(par[u]);
}
 
void unite(int u, int v) {
    par[find(u)] = find(v);
}

void kruskal() {
    sort(edges.begin(), edges.end());
    for (int i = 1; i <= n; i++) par[i] = i;

    ll cnt = 0, cost = 0;
    for (auto [w, u, v] : edges) {
        u = find(u), v = find(v);
        if (u != v) {
            par[u] = v;
            cost += w;
            cnt++;
        }
    }
    if (cnt == n - 1) cout << cost << "\n";
    else cout << "IMPOSSIBLE\n";
}
