#include <stdio.h>
#include <stdlib.h>

int getint(){
	int c = getchar();
	if (EOF == c) exit(0);
	return c - '0';
}

int main(){
	for(;;) {
		int h = getint()*10 + getint();
		getint();
		int m = getint()*10 + getint();
		getint();
		int s = getint()*10 + getint();
		getint();
		int ms = getint()*100 + getint()*10 + getint();
		getint();getint();
		printf("%i.%03i\n", h*3600 + m*60 + s, ms);
	}
	
	return 0;
}