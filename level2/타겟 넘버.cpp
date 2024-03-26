#include <string>
#include <vector>

using namespace std;

int tango_num;
int answer=0;

void dfs(vector <int>&numbers, int count, int cur)
{
    if(count==numbers.size())
    {
        if(cur==tango_num)
            answer++;
        return;
    }
    int next_tango1= cur+numbers[count];
    int next_tango2= cur-numbers[count];
    dfs(numbers, count+1, next_tango1);
    dfs(numbers, count+1, next_tango2);
}

int solution(vector<int> numbers, int target) {
    tango_num=target;
    dfs(numbers, 0, 0);

    return answer;
}
