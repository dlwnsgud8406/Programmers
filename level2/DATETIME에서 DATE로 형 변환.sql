SELECT ANIMAL_ID, name, date_format(datetime, '%Y-%m-%d') as 날짜
-- 소문자 y를 사용하면 연도 끝 두자릿수 출력 ex) 2016 -> 16
from animal_ins
