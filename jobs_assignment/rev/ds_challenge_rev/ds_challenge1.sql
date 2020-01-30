/*
**************************************************************************
This file contains helper functions to get the significance of the data results for Question 1.
The answers to Question one are below in this file:
The dashboard is saved in Metabase in Personal Collections

*****************************************************************************
*/



select count(*) from users;
/* 
Result:
Total users: 19,430 
*/

/* **************************************************************************/
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
			group by 1,2,3, n.created_date, t.created_date
		) a
	group by 1,2,3
	) b;
/* 
Result:
average difference (ad): -349.19
sum of difference (d): -4,850,885.48
sum of difference squared (sd) 6,600,931,726,421.75
*/

select ((d/u)/sqrt((sd-(d^2/u))/((u-1)*u))) as t_score from
(select 19430 u, -4850885.48 d, 6600931726421.75 sd) a;

/*
Result:
-1.89 < 1.96 which means that the difference is significant at a significance level of 5%..

Overall difference in average transactions 7 days before the notification arrived vs. 7 days after the notification arrived = 349 USD
*/


select avg(diff) ad, sum(sq_diff) SST from
(select b.user_id, b.country, b.gen, (b.diff-c.mean_diff) diff, (b.diff-c.mean_diff)^2 as sq_diff from
	(select user_id, country, gen, sum(post_tr) post_tr, sum(pre_tr) pre_tr, (sum(post_tr)-sum(pre_tr)) diff from
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
			group by 1,2,3, n.created_date, t.created_date
		) a
	group by 1,2,3
	) b
	join
	(select user_id, avg(diff) mean_diff
		(select user_id, country, gen, sum(post_tr) post_tr, sum(pre_tr) pre_tr, (sum(post_tr)-sum(pre_tr)) diff from
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
				group by 1,2,3, n.created_date, t.created_date
			) a
		group by 1,2,3
		) b
	group by 1) c
on c.user_id = b.user_id) d;



/* To Calculate country mean */
select concat(country, '_', gen) c_g, (sum(post_tr)-sum(pre_tr))/count(user_id) country_gen_mean
from
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
		group by 1,2,3, n.created_date, t.created_date
	) a;


/* To calculate SSC taking concatenated country/generations groups */
select avg(diff) mean, sum(diff_sq) SSC from
(select b.user_id, b.c_g, (diff-country_gen_mean) diff, (diff-country_gen_mean)^2 diff_sq from
	(select user_id, concat(country, '_', gen) c_g, (sum(post_tr)-sum(pre_tr)) diff
	from
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
			group by 1,2,3, n.created_date, t.created_date
		) a group by 1,2
	) b
	join
	(select concat(country, '_', gen) c_g, (sum(post_tr)-sum(pre_tr))/count(distinct user_id) country_gen_mean
	from
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
			group by 1,2,3, n.created_date, t.created_date
		) a group by 1
	) c
	on b.c_g = c.c_g
group by 1,2,3) d

/*
without distinct
Mean of groups: -335.16
SSC: 6,598,760,834,610
*/

/* Get distinct country gen groups count */
select concat(u.country, 
	(case 
		when u.birth_year<1965 then 'baby_boomers' 
		when u.birth_year<1980 then 'gen_X' 
		when u.birth_year<1990 then 'gen_Y1' 
		when u.birth_year<1995 then 'gen_Y2'
		else 'gen_Z'
	end)) con
from users u 
left join notifications n on u.user_id = n.user_id
left join transactions t on u.user_id = t.user_id
where t.transactions_state='COMPLETED'
and n.status='SENT'
and abs(Extract(Day from n.created_date-t.created_date)) <= 7
group by 1;

/*
Result:
Gives 155 rows count
*/	

/* Gives mean of observations */
select avg(diff) mean_diff from
	(select user_id, country, gen, sum(post_tr) post_tr, sum(pre_tr) pre_tr, (sum(post_tr)-sum(pre_tr)) diff from
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
			group by 1,2,3, n.created_date, t.created_date
		) a
	group by 1,2,3
	) b;
/*
Result:
Mean of total observations: -349.19
*/


/* To get SST */
select avg(diff) ad, sum(sq_diff) SST from
(select b.user_id, b.country, b.gen, (b.diff-(-349.19)) diff, (b.diff-(-349.19))^2 as sq_diff from
	(select user_id, country, gen, sum(post_tr) post_tr, sum(pre_tr) pre_tr, (sum(post_tr)-sum(pre_tr)) diff from
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
			group by 1,2,3, n.created_date, t.created_date
		) a
	group by 1,2,3
	) b
group by 1,2,3,4,5) c;
/*
Result:
0.0045
SST 6,599,237,867,370.81
*/


/* To calculate F-statistics 
numerator = SSC/(num_groups-1)
denomerator = (SST-SSC)/(num_observations-num_groups)
*/
select SSC*(num_observations-num_groups)/((SST-SSC)*(num_groups-1)) from
(select 155 num_groups, 19430 num_observations, 6598760834610 SSC, 6599237867370.81 SST) a;

/*
Result:
Gives very high value of f-stats, thus Null Hypothesis can be ignored
Overall difference in average transactions 7 days before the notification arrived vs. 7 days after the notification arrived 
at country and generations level = 335.16 USD
*/


/* Query to plot the average differences */
select country, sum(baby_boomers_avg) baby_boomers_avg, sum(gen_X_avg) gen_X_avg, sum(gen_Y1_avg) gen_Y1_avg, sum(gen_Y2_avg) gen_Y2_avg, sum(gen_Z_avg) gen_Z_avg
from 
(
	select country, 
	case when gen='baby_boomers' then avg_diff else 0 end baby_boomers_avg,
	(case when gen='gen_X' then avg_diff else 0 end ) as gen_X_avg,
	(case when gen='gen_Y1' then avg_diff else 0 end ) as gen_Y1_avg,
	(case when gen='gen_Y2' then avg_diff else 0 end ) as gen_Y2_avg,
	(case when gen='gen_Z' then avg_diff else 0 end ) as gen_Z_avg
	from
	(select country, gen, count(user_id) num, avg(diff-country_gen_mean) avg_diff from
		(select user_id, country, gen, concat(country, '_', gen) c_g, (sum(post_tr)-sum(pre_tr)) diff
		from
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
				group by 1,2,3, n.created_date, t.created_date
			) a group by 1,2,3,4
		) b
		join
		(select concat(country, '_', gen) c_g, (sum(post_tr)-sum(pre_tr))/count(user_id) country_gen_mean
		from
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
				group by 1,2,3, n.created_date, t.created_date
			) a group by 1
		) c
		on b.c_g = c.c_g
	group by 1,2) d
	group by 1, d.gen, d.avg_diff) e
group by 1;
