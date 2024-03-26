#include <string>
#include <vector>

using namespace std;

bool solution(int x) {
    int num=x;
    int sum=0;
    while(num>10)
    {
        sum+=(num%10);
        num/=10;
    }
    sum+=num;
    bool answer = true;
        if(x%sum!=0)
        answer=false;
    return answer;
}
