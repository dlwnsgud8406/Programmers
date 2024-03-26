def solution(gems):
    # Dictionary to store the count of each gem type in the current window
    gem_count = {}
    # Total unique gems in the input
    total_gems = len(set(gems))
    # Start and end pointers of the window
    start, end = 0, 0
    # The answer tuple: (start index, end index, length of the segment)
    answer = (0, len(gems) - 1, len(gems))
    
    while end < len(gems):
        # Include the gem at the current end in the count
        if gems[end] in gem_count:
            gem_count[gems[end]] += 1
        else:
            gem_count[gems[end]] = 1
        
        # When the window contains all types of gems, try to shrink it from the left
        while len(gem_count) == total_gems and start <= end:
            # Update the answer if the current window is smaller
            if end - start < answer[2]:
                answer = (start, end, end - start)
            
            # Remove or decrease the count of the gem at the current start
            gem_count[gems[start]] -= 1
            if gem_count[gems[start]] == 0:
                del gem_count[gems[start]]
            start += 1
        
        # Expand the window
        end += 1
    
    # Adjusting the answer to be 1-indexed as per the problem statement
    return answer[0] + 1, answer[1] + 1
gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
# gems = ["AA", "AB", "AC", "AA", "AC"]
# gems = ["XYZ", "XYZ", "XYZ"]
# gems = ["ZZZ", "YYY", "NNNN", "YYY", "BBB"]
화
solution(gems)

