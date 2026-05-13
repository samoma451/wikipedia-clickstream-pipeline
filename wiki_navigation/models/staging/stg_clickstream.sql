with source as (
    select *
    from raw_clickstream
)

select
    lower(referrer) as source_page,
    lower(resource) as destination_page,
    cast(n as integer) as click_count,
    type as traffic_type

from source