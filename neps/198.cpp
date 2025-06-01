#include <iostream>
using namespace std;

int media(int num[]){
    int sum = 0;
    for(int i = 0; i < 3; i++){
        sum+=num[i];
    }
    int media = sum / 3;
    return media;
}

int sum(int num[]){
    int s = 0;
    for(int i = 0; i < 3; i++){
        s+=num[i];
    }
    return s;
}

int main(){
    int matrix[3][3];

    for(int i = 0; i < 3; i++){
        for(int j = 0; j<3; j++){
            cin >> matrix[i][j];
        }
    }

    int sumL[3] = {0,0,0};
    int sumC[3] = {0,0,0};
    int sumDP[3] = {0,0,0};
    int sumDS[3] = {0,0,0};

    for(int i = 0; i < 3; i++){
        for(int j = 0; j < 3; j++){
            sumL[i] +=matrix[i][j];
        }
        for(int j = 0; j < 3; j++){
            sumC[i] +=matrix[j][i];
        }
        for(int j = 0; j < 3; j++){
            if( j == i){
                sumDP[i]+=matrix[i][j];
            }
        }
        for(int j = 0; j < 3; j++){
            if( j+i == 2){
                sumDS[i]+=matrix[i][j];
            }
        }
    }

    if( media(sumL) == media(sumC) && media(sumC) == sum(sumDP) &&  sum(sumDP) == sum(sumDS)){

        cout << "SIM" << endl;
    }else{
        cout << "NAO" << endl;
    }
    return 0;
}
