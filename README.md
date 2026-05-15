# Wikipedia Clickstream Pipeline

## Overview
Transforms raw Wikipedia clickstream logs into analytical models using dbt.

## Architecture
- Python ingestion scripts
- DuckDB or warehouse layer
- dbt transformation layer
- Analytics marts

## Pipeline
Raw → Processed → dbt staging → marts

## Key Models
- fct_navigation_edges
- stg_clickstream
- dim_pages

## How to run
1. Install dependencies
2. Run ingestion script
3. Run dbt models