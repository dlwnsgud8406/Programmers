#include <string>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;


int solution(vector<int> scoville, int K) {
    int answer = 0;
    priority_queue<int, vector<int>, greater<int>> sco;
    for(int i=0;i<scoville.size();i++)
        sco.push(scoville[i]);

    while(sco.top()<K && sco.size()>1)
    {
        answer++;
        int min, second_min;
        min=sco.top(); sco.pop();
        second_min=sco.top(); sco.pop();
        sco.push(min+second_min*2);
    }
    if(sco.top()<K)
        return -1;
    return answer;
}
