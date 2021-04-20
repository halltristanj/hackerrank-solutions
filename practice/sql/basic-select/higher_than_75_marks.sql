select name
from students
where marks > 75
order by
    SUBSTRING(name, LENGTH(NAME) - 2, LENGTH(NAME)) asc,
    id asc
