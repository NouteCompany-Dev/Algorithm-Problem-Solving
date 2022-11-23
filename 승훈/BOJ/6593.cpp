#include<bits/stdc++.h>
using namespace std;

int l, r, c;
char arr[31][31][31];
int cnt[31][31][31];
bool chk[31][31][31];
bool visited[31][31][31];
int dx[] = {-1, 1, 0, 0, 0, 0};
int dy[] = {0, 0, -1, 1, 0, 0};
int dz[] = {0, 0, 0, 0, -1, 1};
queue< pair< int, pair< int, int > > > que;

int main() {
    while(true) {
        cin >> l >> r >> c;
        
        if(l == 0 && r == 0 && c == 0) {
            break;
        }
        
        for(int i = 0; i < l; i++) {
            for(int j = 0; j < r; j++) {
                for(int k = 0; k < c; k++) {
                    cnt[i][j][k] = 0;
                    chk[i][j][k] = true;
                    visited[i][j][k] = false;
                }
            }
        }
        
        for(int i = 0; i < l; i++) {
            for(int j = 0; j < r; j++) {
                for(int k = 0; k < c; k++) {
                    char ch;
                    cin >> ch;
                    arr[i][j][k] = ch;
                    
                    if(ch == 'S') {
                        visited[i][j][k] = true;
                        que.push({ i, { j, k }});
                    }
                    
                    else if(ch == '#') {
                        chk[i][j][k] = false;
                    }
                }
            }
        }
        
        bool res = false;
        
        while(!que.empty()) {
            if(res) {
                break;
            }
            
            int q1 = que.front().first;
            int q2 = que.front().second.first;
            int q3 = que.front().second.second;
            que.pop();
            
            for(int i = 0; i < 6; i++) {
                int nq1 = q1 + dx[i];
                int nq2 = q2 + dy[i];
                int nq3 = q3 + dz[i];
                
                if(nq1 >= 0 && nq2 >= 0 && nq3 >= 0 && nq1 < l && nq2 < r && nq3 < c) {
                        cnt[nq1][nq2][nq3] = cnt[q1][q2][q3] + 1;
                        visited[nq1][nq2][nq3] = true;
                        
                        if(arr[nq1][nq2][nq3] == 'E') {
                            res = true;
                            cout << "Escaped in " << cnt[nq1][nq2][nq3] << " minute(s)." << endl;
                            
                            break;
                        }
                        
                        else {
                            que.push({ nq1, { nq2, nq3 }});
                        }
                    }
                }
            }
        }
            
        while(!que.empty()) {
            que.pop();
        }

        if(!res) {
            cout << "Trapped!" << endl;
        }
    }
    
    return 0;
}