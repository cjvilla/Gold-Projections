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

create table country_gold_production (
	Name text,
	Code text,
	date_recorded date,
	gold_production float8
);

create table inflation_rates (
	date_recorded date,
	JAN float8,
	FEB float8,
	MAR float8,
	APR float8,
	MAY float8,
	JUN float8,
	JUL float8,
	AUG float8,
	SEP float8,
	OCT float8,
	NOV float8,
	DEC float8,
	AVE float8
);

create table dollar_index (
	date_recorded date,
	value float8
);