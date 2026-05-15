-- Fact table: directed navigation edges between Wikipedia pages

with stg as (

    select *
    from {{ ref('stg_clickstream') }}

),

aggregated as (

    select
        from_page,
        to_page,
        sum(click_count) as total_clicks,
        sum(view_count) as total_views
    from stg
    group by 1, 2

)

select
    from_page,
    to_page,
    total_clicks,
    total_views,
    case
        when total_views = 0 then 0
        else total_clicks * 1.0 / total_views
    end as click_through_rate

from aggregated