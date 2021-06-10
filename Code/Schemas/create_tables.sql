create final_inflation_production (
	Year integer,
	Month integer,
	Inflation_Value double precision
);

create table final_us_dollar_index (
	Year integer,
	Month integer,
	Date date,
	Value double precision
);

create table monthly_gold_prices_final (
	Date date,
	Year integer,
	month integer,
	us_dollar double precision,
	euro double precision,
	japanese_yen double precision
	pound double precision,
	canadian_dollar double precision,
	swiss_franc double precision,
	indian_rupee double precision,
	saudi_riyal double precision,
	uae_dirham double precision,
	thai_baht double precision,
	korean_won double precision,
	south_african_rand double precision,
	australian_dollar double precision,
);

create table gold_prediction_data
	AS
(select x."Year", x."Month", x."Inflation_Value", x."dollar_index", j."us_dollar", j."pound", j."indian_rupee", j."sauth_african_rand", j."australian_dollar"
from gold_prediction_data x
join monthly_gold_prices_final j
on x."Year" = j."year" and x."Month" = j."month");



