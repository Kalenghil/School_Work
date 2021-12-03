#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
	string alphabet = "CHETAI";
	int counter = 0;
	for (const char a: alphabet){
		for (const char b: alphabet){
			for (const char c: alphabet){
				for (const char d: alphabet){
					string s = a + b + c + d;
					if (count(s.begin(), s.end(), 'A') <= 1)
						counter++;
				}
			}
		}
	}

	return 0;
}