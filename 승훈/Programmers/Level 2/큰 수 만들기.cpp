#include<bits/stdc++.h>
using namespace std;

string solution(string number, int k) {
    string answer = "";
    int size = number.size() - k;
    int start = 0;
    
    for(int i = 0; i < size; i++) {
        char maxN = number[start];
        int idx = start;
        
        for(int j = start; j <= i + k; j++) {
            if(maxN < number[j]) {
                maxN = number[j];
                idx = j;
            }
        }
        
        start = idx + 1;
        answer += maxN;
    }
    
    return answer;
}