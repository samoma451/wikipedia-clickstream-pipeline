with pages as (

    select from_page as page from {{ ref('stg_clickstream') }}
    union
    select to_page as page from {{ ref('stg_clickstream') }}

)

select distinct
    page
from pages