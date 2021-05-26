select strftime('%H:%M',stamp), avg(temp), avg(hum), avg(plug), avg(heater)
from (select * from timelog where date(stamp) = date('now'))
group by strftime('%H:%M',stamp) 
having hum < 100 ;

select * from timelog  where temp > 20 order by stamp desc  limit 1200;