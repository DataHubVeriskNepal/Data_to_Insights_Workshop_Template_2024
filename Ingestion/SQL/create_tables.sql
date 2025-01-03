
-- Create tables in snowflake
CREATE TABLE IF NOT EXISTS Date_Lookup
(
    bs_date STRING,
    ad_date STRING
);

CREATE TABLE IF NOT EXISTS "gold_silver"
(
    "date" STRING,
    "fine_gold" STRING,
    "standard_gold" STRING,
    "silver" STRING
);

CREATE TABLE IF NOT EXISTS "forex"
(
    "date" STRING,
    "currency" STRING,
    "buy" STRING,
    "sell" STRING,
    "unit" STRING,
    "iso3" STRING    
);