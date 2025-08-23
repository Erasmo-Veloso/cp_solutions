#include <iostream>
#include <vector>

using namespace std;

int main() {
 
    int C;
    
    while(cin >> C) {
        if(C == 0) return 0;
        
        int M = 0;
        int J = 0;
        
        for(int i = 0; i < C; i++){
            int X;
            cin >> X;
            if(X == 0) M++;
            if(X == 1) J++;
        }
        cout << "Mary won " << M << " times and John won " << J << " times" << endl;
    }
 
    return 0;
}