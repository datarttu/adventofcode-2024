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