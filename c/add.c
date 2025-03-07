#include <stdio.h>

int x = 5;

// 함수 선언부
int add(int);

int main() {
	int y = 3;
	// hamsu hochulbu
	printf("%d + %d  = %d\n",x,y,add(y));
	return 0;
}


// hamsu
int add(int y) {
	return x + y;
}
