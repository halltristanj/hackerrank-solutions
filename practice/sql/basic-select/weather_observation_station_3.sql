/*
Enter your query here.
*/
select distinct city
from station
where
        MOD(id, 2) = 0
  and id != 0
;
