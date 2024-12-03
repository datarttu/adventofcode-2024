-- Part 1
with extracted_operations as (
    select section,
        unnest(regexp_extract_all(section, 'mul\(\d+,\d+\)')) as operation
    from read_csv(
            'inputs/day_03.txt',
            header = false,
            columns = { 'section': 'VARCHAR' }
        )
)
select sum(
        list_reduce(
            regexp_extract_all(operation, '\d+'),
            (x, y)->x::integer * y::integer
        )::integer
    ) as result
from extracted_operations;
-- Part 2; reading do\(\)|don't\(\)|mul\(\d+,\d+\) from a file due to quotation issues.
with rgx_tbl as (
    select rgx
    from read_csv(
            'day_03_regex.txt',
            header = false,
            columns = { 'rgx': 'VARCHAR' }
        )
),
extracted_operations as (
    select ip.section,
        row_number() over () as row_id,
        unnest(regexp_extract_all(ip.section, rgx_tbl.rgx)) as operation,
        generate_subscripts(regexp_extract_all(ip.section, rgx_tbl.rgx), 1) as op_id
    from read_csv(
            'inputs/test_03_2.txt',
            header = false,
            columns = { 'section': 'VARCHAR' }
        ) ip
        cross join rgx_tbl
),
valid_operations as (
    select operation,
        op_id,
        sum(
            case
                when operation similar to 'do\(\)|don.*' then 1
                else 0
            end
        ) over (
            order by row_id,
                op_id
        ) as validity_switch
    from extracted_operations qualify validity_switch % 2 = 0
        and operation similar to 'mul.*'
)
select sum(
        list_reduce(
            regexp_extract_all(operation, '\d+'),
            (x, y)->x::integer * y::integer
        )::integer
    ) as result
from valid_operations;