select concat(name, '(', substring(occupation,1,1), ')') as cname
from occupations
order by cname;

select concat('There are a total of',' ',count(occupation),' ',lower(occupation),'s.') as total
from occupations
group by occupation
order by total;
