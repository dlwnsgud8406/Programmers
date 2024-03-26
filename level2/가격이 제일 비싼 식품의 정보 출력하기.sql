SELECT *
from food_product
where price = (select max(price) price from food_product);
