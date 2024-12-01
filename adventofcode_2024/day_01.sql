create table lists as (
    select split_part(pair, '   ', 1)::integer as v1,
        split_part(pair, '   ', 2)::integer as v2
    from read_csv(
            'inputs/day_01.txt',
            header = false,
            columns = { 'pair': 'VARCHAR' }
        )
);
with sorted1 as (
    select v1,
        row_number() over (
            order by v1
        ) as rn
    from lists
),
sorted2 as (
    select v2,
        row_number() over (
            order by v2
        ) as rn
    from lists
)
select sum(abs(sorted1.v1 - sorted2.v2)) as sum_of_diffs
from sorted1
    inner join sorted2 on sorted1.rn = sorted2.rn;
with occurrences as (
    select v2,
        count(*) as n_occurs
    from lists
    group by v2
)
select sum(v1 * coalesce(o.n_occurs, 0)) as similarity_score
from lists l
    left join occurrences o on l.v1 = o.v2;