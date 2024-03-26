SELECT BOOK_ID, DATE_FORMAT(PUBLISHED_DATE, '%Y-%m-%d') AS PUBLISHED_DATE
FROM BOOK
WHERE (BOOK_ID = 3 OR BOOK_ID = 4) AND CATEGORY = '인문'
ORDER BY BOOK_ID DESC