def solution(arr, delete_list):
    for i in delete_list:
        try: arr.remove(i)
        except ValueError:
            pass
    return arr
