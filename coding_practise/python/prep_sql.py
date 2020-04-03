SELECT CustomerName, Locate('a', CustomerName)-INSTR(CustomerName, "a"), position('a' in CustomerName)
FROM Customers;

select avg(diff) ad, sum(diff) d, sum(sq_diff) sd from
(select user_id, country, gen, sum(post_tr) post_tr, sum(pre_tr) pre_tr, (sum(post_tr)-sum(pre_tr)) diff, ((sum(post_tr)-sum(pre_tr)))^2 sq_diff from
(select u.user_id, u.country, 
(case 
    when u.birth_year<1965 then 'baby_boomers' 
    when u.birth_year<1980 then 'gen_X' 
    when u.birth_year<1990 then 'gen_Y1' 
    when u.birth_year<1995 then 'gen_Y2'
    else 'gen_Z'
end) gen,
(case 
    when Extract(Day from n.created_date-t.created_date)>0 then sum(t.amount_usd) 
    else 0 
end) post_tr,
(case 
    when Extract(Day from n.created_date-t.created_date)<0 then sum(t.amount_usd) 
    else 0 
end) pre_tr
from users u 
left join notifications n on u.user_id = n.user_id
left join transactions t on u.user_id = t.user_id
where t.transactions_state='COMPLETED'
and n.status='SENT'
and abs(Extract(Day from n.created_date-t.created_date)) <= 7
group by 1,2,3, n.created_date, t.created_date) a
group by 1,2,3) b;