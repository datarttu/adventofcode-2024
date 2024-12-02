create table reports as (
    select report
    from read_csv(
            'inputs/test_02.txt',
            delim = ',',
            header = false,
            columns = { 'report': 'VARCHAR' }
        )
);
with levels as (
    select row_number() over () as rep_num,
        report,
        unnest(string_split(report, ' '))::integer as lvl,
        from reports
),
numbered as (
    select rep_num,
        report,
        lvl,
        row_number() over (partition by report) as rn
    from levels
),
diffs as (
    select rep_num,
        report,
        lvl - lag(lvl) over (
            partition by report
            order by rn
        ) as diff
    from numbered
)
select rep_num,
    report,
    bool_and(
        diff between 1 and 3
    )
    or bool_and(
        diff between -3 and -1
    ) as is_safe
from diffs
group by rep_num,
    report
order by rep_num;