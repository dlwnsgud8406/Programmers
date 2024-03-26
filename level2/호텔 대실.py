from collections import defaultdict


def solution(book_time):
    answer, current_book, books = 0, 0, defaultdict(int)

    for book in book_time:
        begin_hour, begin_minute = map(int, book[0].split(':'))
        end_hour, end_minute = map(int, book[1].split(':'))
        begin = begin_hour * 60 + begin_minute
        end = end_hour * 60 + end_minute
        books[begin] += 1
        books[end + 10] -= 1
    books = sorted(list(map(list, books.items())))

    for book in books:
        current_book += book[1]
        answer = max(answer, current_book)

    return answer
