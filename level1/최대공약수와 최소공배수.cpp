#include <string>
#include <vector>

using namespace std;
#include<vector>
#include<iostream>
using namespace std;


int Euclidean(int a, int b)
{
    return b ? Euclidean(b, a%b) : a;
}

vector<int> gcdlcm(int a,int b)
{
    vector<int> answer;
  answer.push_back(Euclidean(a,b));

  answer.push_back(a*b / answer[0]);

    return answer;
}

vector<int> solution(int n, int m) {
    vector<int> answer=gcdlcm(n,m);
    return answer;
}
