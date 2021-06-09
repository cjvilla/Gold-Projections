create table gold_prices (
	date_recorded date,
	USA float8,
	Euro float8,
	Japan float8,
	UK float8,
	Canada float8,
	Swizerland float8,
	India float8,
	China float8,
	Turkey float8,
	SB float8,
	Indonesia float8,
	UAE float8,
	Thailand float8,
	Vietnam float8,
	Egypt float8,
	SK float8,
	Russia float8,
	SA float8,
	Australia float8
);

create table country_gold_production(
	Name text,
	code text,
	date_recorded date,
	gold_production float8
);