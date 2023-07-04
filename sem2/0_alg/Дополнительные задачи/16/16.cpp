#include <bits/stdc++.h>

using namespace std;

#define ll long long

void process_mem_usage(double& vm_usage, double& resident_set)
{
    vm_usage     = 0.0;
    resident_set = 0.0;

    // the two fields we want
    unsigned long vsize;
    long rss;
    {
        std::string ignore;
        std::ifstream ifs("/proc/self/stat", std::ios_base::in);
        ifs >> ignore >> ignore >> ignore >> ignore >> ignore >> ignore >> ignore >> ignore >> ignore >> ignore
                >> ignore >> ignore >> ignore >> ignore >> ignore >> ignore >> ignore >> ignore >> ignore >> ignore
                >> ignore >> ignore >> vsize >> rss;
    }

    long page_size_kb = sysconf(_SC_PAGE_SIZE) / 1024; // in case x86-64 is configured to use 2MB pages
    vm_usage = vsize / 1024.0;
    resident_set = rss * page_size_kb;
}

ll n;
ll dist[1048576][20];

ll visited_all;

typedef struct {
    vector<ll> visited;
    ll ant = LLONG_MAX;
} ans;

vector<ll> visited;

ans tsp(ll mask, ll pos) {
    if (mask == visited_all) {
        return {visited, dist[pos][0]};
    }
    ans mem;
    ll ant = LLONG_MAX;
    for (int stadt = 0; stadt < n; stadt++) {
        if ((mask&(1 << stadt)) == 0) {
            visited.push_back(stadt);
            ans res = tsp(mask | (1 << stadt), stadt);
            res.ant += dist[pos][stadt];
            if (res.ant < ant) {
                mem = res;
                ant = mem.ant;
            }
            visited.pop_back();
        }
    }
    return mem;
}

int main() {
    ifstream input; input.open("input.txt");
    ofstream output; output.open("output.txt");
    auto start = chrono::high_resolution_clock::now();
    double vm, rss;
    process_mem_usage(vm, rss);
    input >> n;
    for (ll i = 0; i < n; i++) {
        for (ll j = 0; j < n; j++) 
            input >> dist[i][j];
    }
    visited_all = (1 << n) - 1;
    ll ant = LLONG_MAX;
    ll mask = 1;
    ans mem;
    int mem_stadt;
    for (int stadt = 0; stadt < n; stadt++) {
        if ((mask&(1 << stadt)) == 0) {
            ans res = tsp(mask | (1 << stadt), stadt);
            if (res.ant < ant) { 
                mem = res;
                ant = mem.ant;
                mem_stadt = stadt;
            }
        }
    }
    
    output << mem.ant << "\n" << mem_stadt+1 << " ";
    for (ll i = 0; i < mem.visited.size(); i++)
        output << mem.visited[i] + 1 << " ";                                                                                                                                                                                 





    output << "1";
    auto end = chrono::high_resolution_clock::now();

    double diff = chrono::duration<double, std::milli>(end-start).count();
    cout << "Время выполнения: " << diff << endl; 
    cout << "Использовано памяти: " << vm;
    return 0;
}

