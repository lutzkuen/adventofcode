#include <stdio.h> 
#include<iostream>
using namespace std;

int main() {
    int a[1000000], b[1000000], cut[3], targ, targ_idx;
    a[0] = 3;
    a[1] = 8;
    a[2] = 9;
    a[3] = 1;
    a[4] = 2;
    a[5] = 5;
    a[6] = 4;
    a[7] = 6;
    a[8] = 7;
    for (int i=9; i < 1000000; i++) {
        a[i] = i+1;
    }
    for (int turn=0; turn<10000000; turn++) {
        if ( turn % 1000 == 0 ) {
            cout << turn << endl;
        }
        targ = a[0]-1;
        if ( targ < 1 ) {
            targ = 1000000;
        }
        for (int ic=1; ic<4; ic++) {
            cut[ic-1] = a[ic];
        }
        while ( targ == cut[0] || targ == cut[1] || targ == cut[2] ) {
            targ -= 1;
            if ( targ < 1 ) {
                targ = 1000000;
            }
        }
        targ_idx = -1;
        for (int i=0; i<999999;i++) {
            if (targ_idx < 0) {
                b[i] = a[i+4];
            } else {
                if ( targ_idx >= 0 && i <= (targ_idx + 3)) {
                    b[i] = cut[i-targ_idx-1];
                } else {
                    b[i] = a[i+1];
                }
            }
            if (b[i] == targ) {
                targ_idx = i;
            }
        }
        b[999999] = a[0];
        for (int i=0; i<1000000;i++) {
            a[i] = b[i];
        }
    }
    int result=1;
    for (int k=0;k<1000000;k++) {
        if (a[k] == 1) {
            result = result * a[k+1];
            result = result * a[k+2];
            break;
        }
    }
    cout << result << endl;
}
