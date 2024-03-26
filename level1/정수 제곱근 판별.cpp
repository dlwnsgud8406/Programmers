#include <string>
#include <vector>

using namespace std;

long long solution(long long n) {
    long long answer = 0;
    long number=0;
    while(number*number!=n)
    {
        if(number>n)
            return -1;
        else
            number++;
    }
    number+=1;
    answer=number*number;
    return answer;
}
