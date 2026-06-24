#include <stdio.h>

int main(){
	char buffer[32];
	puts("WELCOME! Please enter your name!");
	gets(buffer);
	printf("Hello, %s\n", buffer);
}