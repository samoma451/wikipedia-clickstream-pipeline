import duckdb

RAW_PATH = "data/raw/clickstream.tsv.gz"
DB_PATH = "clickstream.duckdb"

def load_to_duckdb():
    con = duckdb.connect(DB_PATH)

    con.execute("""
        CREATE OR REPLACE TABLE clickstream AS
        SELECT *
        FROM read_csv(
        'data/raw/clickstream.tsv.gz',
        delim='\t',
        header=false
            )
    """)

    con.execute("""
    ALTER TABLE clickstream RENAME COLUMN column0 TO prev;
    """)

    con.execute("""
    ALTER TABLE clickstream RENAME COLUMN column1 TO curr;
    """)

    con.execute("""
    ALTER TABLE clickstream RENAME COLUMN column2 TO type;
    """)

    con.execute("""
    ALTER TABLE clickstream RENAME COLUMN column3 TO n;
    """)

    print("Loaded TSV.GZ into DuckDB table: clickstream")

if __name__ == "__main__":
    load_to_duckdb()