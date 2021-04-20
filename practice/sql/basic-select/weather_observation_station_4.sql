/*
Enter your query here.
*/
with
    all_count as (select count(*) as all_count from station),
    dis_count as (select count(distinct city) as dis_count from station)
select all_count - dis_count
from all_count
         join dis_count
              on 1 = 1
