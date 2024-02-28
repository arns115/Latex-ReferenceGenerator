//segment_Tree
int n, q, arr[MAX_N], st[4 * MAX_N];
 
void build(int node, int start, int end) {
    if (start == end) {
        st[node] = arr[start];
        return;
    }
    int mid = (start + end) / 2;
    build(2 * node, start, mid);
    build(2 * node + 1, mid + 1, end);
    st[node] = min(st[2 * node], st[2 * node + 1]);
}
 
void update(int node, int start, int end, int idx, int val) {
    if (start == end) {
        arr[idx] = val;
        st[node] = val;
        return;
    }
    int mid = (start + end) / 2;
    if (idx <= mid) update(2 * node, start, mid, idx, val);
    else update(2 * node + 1, mid + 1, end, idx, val);
    st[node] = min(st[2 * node], st[2 * node + 1]);
}

int query(int node, int start, int end, int l, int r) {
    if (start > r || end < l) return INF;
    if (l <= start && end <= r) return st[node];
    int mid = (start + end) / 2;
    return min(query(2 * node, start, mid, l, r), query(2 * node + 1, mid + 1, end, l, r)); 
}