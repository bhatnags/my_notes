#include <iostream>

using namespace std;

#define PI 3.142 // define our own constants using the #define preprocessor directive
//const zipcode = 411014;


void f(static int i;){
	
	++i;
	printf("%d",i);
}

int main(){
	cout << "'test'"; 
	f(10);
	f(10);
	f(12);
	f(20);
	f(34);
}


/*
void main(){
	int n = 10;
	while(n>0){
			cout<<n<<","; // not calculated if the condition is not met
			--n;
	}
	cout<<endl;
	int N = 10;
	do {
		cout<<N<<","; // calculated even if the condition is met, though the condition won't let it print
		--N;
	}while(N>0);
	cout << "\n" << n << "," << N << endl;
}



int globalVar = 2;
int main()
{
 int globalVar = 5;
 cout<<globalVar<<endl; // local variable
 cout<<::globalVar<<endl; // access globa; variable
 
 int x (20); // initializing using a contructor notation
 cout << x << endl;

 // defining constants
 const int pi = 3.142;
 //const char c = 'abc';

 int a, b;
 // a = b = x = 5;
 a = 2 + (b = 3);
 cout << a << " " << b << " " << a/b << " " << a%b << " " << ((a/b)*b) + a%b << endl;

 a >>= 2; b <<=2; // b*(2^2)
 cout << a << " " << b << endl; //1,12

 a >>= 3; b <<=3;  // b*(2^3)
 cout << a << " " << b << endl; //0, 96

 a >>= 4; b <<=4;  // b*(2^4)
 cout << a << " " << b << endl; //0, 1536

 a >>= 5; b <<=5;  // b*(2^5)
 cout << a << " " << b << endl; //0, 49152
 
}

int main()
{
	char name;
	char a,b,name; // Error as previously declared within the same scope
	cout << "Hello";
	cin>>name;
}
*/