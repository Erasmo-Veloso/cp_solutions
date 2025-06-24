#include <iostream>
#include <vector>
using namespace std;

int main(){

    int N;
    vector<int> num;
    bool A = false;
    bool B = false;

    cin >> N;

    for(int i = 0; i < N; i++){
        int x;
        cin >> x;
        num.push_back(x);
    }


    for( int i = 0; i< num.size(); i++){
        if(num[i]==1){
            A = !A;
        }else if(num[i]==2){
            A = !A;
            B = !B;
        }
    }

    int rA = A ? 1 : 0;
    int rB = B ? 1 : 0;

    cout << rA << "\n" << rB << endl;

    return 0;
}
