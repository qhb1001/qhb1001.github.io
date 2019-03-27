#include <stdio.h>
#include <iostream>
#include <cstring>
using namespace std;

typedef unsigned char* byte_pointer;

void show_bytes(byte_pointer start, size_t len) {
    for (size_t i = 0; i < len; ++i) 
        printf("%.2x", start[i]);

    printf("\n");
}

void show_int(int x) {
    show_bytes((byte_pointer) &x, sizeof(int));
}

void show_float(float x) {
    show_bytes((byte_pointer) &x, sizeof(float));
}

void show_pointer(void *x) {
    show_bytes((byte_pointer) &x, sizeof(void *));
}


int main() {
    cout << sizeof(byte_pointer) << endl;

    int ival = 12345;
    float fval = 12345.0;
    int *pval = &ival;
    show_int(ival);
    show_float(fval);
    show_pointer(pval);

    for (char c = 'a'; c <= 'f'; ++c) 
        printf("%.2x ", (int)c);
    
    printf("\n");
}