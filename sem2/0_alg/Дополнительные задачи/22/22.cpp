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

const int maxi = 1 << 6;

int n,m;

int dp[maxi][maxi];
int a[31][maxi];

bool calc(int i, int j) {
    bool b[4];
    for (int i_ = 0; i_ < n - 1; i_++) {
        b[0] = (i & (1 << i_)) != 0;
        b[1] = (i & (1 << (i_ + 1))) != 0;
        b[2] = (j & (1 << i_)) != 0;
        b[3] = (j & (1 << (i_ + 1))) != 0;
        if ((b[0] == b[1]) && (b[1] == b[2]) && (b[2] == b[3]))
            return false;
    }
    return true;
}


int main() {
    ifstream input; input.open("input.txt");
    ofstream output; output.open("output.txt");
    auto start = chrono::high_resolution_clock::now();
    double vm, rss;
    process_mem_usage(vm, rss);

    input >> n >> m;

    if (n > m) {
        int c = n;
        n = m;
        m = c;
    }

    int res = 0;
    int len = 1 << n;
    for (int i = 0; i < len; i++) {
        for (int j = 0; j < len; j++)
            dp[i][j] = calc(i,j);
    }

    for (int i = 0; i < len; i++) 
        a[0][i] = 1;
    for (int i = 1; i < m; i++) {
        for (int j = 0; j < len; j++) {
            for (int k = 0; k < len; k++) 
                a[i][j] += a[i-1][k] * dp[k][j];
        }
    }
    for (int i = 0; i < len; i++)
        res += a[m-1][i];
    output << res;

    auto end = chrono::high_resolution_clock::now();

    double diff = chrono::duration<double, std::milli>(end-start).count();
    cout << "Время выполнения: " << diff << endl; 
    cout << "Использовано памяти: " << vm;

    return 0;
}
