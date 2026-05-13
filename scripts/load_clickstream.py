import duckdb
import os

DB_PATH = "data/processed/wiki.duckdb"
DATA_PATH = "data/raw/clickstream.tsv.gz" #using 2026-04 data currently

os.makedirs("data/processed", exist_ok=True)

con = duckdb.connect(DB_PATH)

con.execute("""
CREATE OR REPLACE TABLE raw_clickstream AS
SELECT *
FROM read_csv_auto(?)
""", [DATA_PATH])

print("Loaded clickstream into DuckDB")