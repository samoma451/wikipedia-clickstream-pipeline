with source as (

    select *
    from clickstream

),

cleaned as (

    select
        lower(trim(prev)) as from_page,
        lower(trim(curr)) as to_page,
        trim(type) as ref_type,
        cast(n as integer) as n
    from source

)

select *
from cleaned