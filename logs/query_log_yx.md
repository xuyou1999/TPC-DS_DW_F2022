## Fix queries
### 5
- replace 'stddev_samp' with 'stdev' in line 6 and 31

### 6
- replace '(cast('2002-08-04' as date) +  30 days)' with '(dateadd(day, 30, cast('2002-08-04' as date)))' in line 15, 31, 57
- replace '||' with '+' in line 71, 78, 85

### 7
- replace '(cast('1999-02-22' as date) + 90 days)' with '(dateadd(day, 90, cast('1999-02-22' as date)))' in line 11, 23

### 8
- replace 'substr' with 'substring' in line 12

### 11
- replace 'lochierarchy' with 'grouping(i_category)+grouping(i_class)' in line 22 because SQL server does not allow alias in case statement

### 14
- replace '(cast ('2000-05-19' as date) - 30 days)' with '(dateadd(day, -30, cast('2000-05-19' as date)))' in line 19
- replace '(cast ('2000-05-19' as date) + 30 days)' with '(dateadd(day, 30, cast('2000-05-19' as date)))' in line 20

### 17
- replace '(cast('1999-4-01' as date) + 60 days)' with '(dateadd(day, 60, cast('1999-4-01' as date)))' in line 13

### 18
- replace 'substr' with 'substring' in line 7

### 21
- replace 'lochierarchy' with 'grouping(i_category)+grouping(i_class)' in line 26 because SQL server does not allow alias in case statement

### 24
- replace 'substr' with 'substring' in line 3, 27, 30

### 25
- replace '(cast('1999-5-01' as date) + 60 days)' with '(dateadd(day, 60, cast('1999-5-01' as date)))' in line 13

### 31
- replace '(cast('2001-06-09' as date) +  60 days)' with '(dateadd(day, 60, cast('2001-06-09' as date)))' in line 9

### 32
- replace '(cast('2000-01-05' as date) + 30 days)' with '(dateadd(day, 30, cast('2000-01-05' as date)))' in line 19

### 33
- replace 'substr' with 'substring' in line 2, 78

### 34
- replace 'lochierarchy' with 'grouping(s_state)+grouping(s_county)' in line 34 because SQL server does not allow alias in case statement

### 39
- replace '||' with '+' in line 55, 135

### 41
- replace 'stddev_samp' with 'stdev' in line 7, 8, 11, 12, 14, 15

### 43
- replace '(cast('2002-5-01' as date) + 60 days)' with '(dateadd(day, 60, cast('2002-5-01' as date)))' in line 18

### 44
- replace '(cast('2001-01-25' as date) + 90 days)' with '(dateadd(day, 90, cast('2001-01-25' as date)))' in line 12
- replace '(cast('2001-01-25' as date) + 90 days)' with '(dateadd(day, 90, cast('2001-01-25' as date)))' in line 24

### 47
- replace 'stddev_samp' with 'stdev' in line 9, 10, 14, 15, 19, 20

## Query optimization
### 14
For subquery 
```
select iss.i_brand_id brand_id
     ,iss.i_class_id class_id
     ,iss.i_category_id category_id
 from store_sales
     ,item iss
     ,date_dim d1
 where ss_item_sk = iss.i_item_sk
   and ss_sold_date_sk = d1.d_date_sk
   and d1.d_year between 1999 AND 1999 + 2
 intersect 
 select ics.i_brand_id
     ,ics.i_class_id
     ,ics.i_category_id
 from catalog_sales
     ,item ics
     ,date_dim d2
 where cs_item_sk = ics.i_item_sk
   and cs_sold_date_sk = d2.d_date_sk
   and d2.d_year between 1999 AND 1999 + 2
 intersect
 select iws.i_brand_id
     ,iws.i_class_id
     ,iws.i_category_id
 from web_sales
     ,item iws
     ,date_dim d3
 where ws_item_sk = iws.i_item_sk
   and ws_sold_date_sk = d3.d_date_sk
   and d3.d_year between 1999 AND 1999 + 2) aa1
 where i_brand_id = brand_id
      and i_class_id = class_id
      and i_category_id = category_id
```
By analyzing the query, it is not difficult to see that the duplicate result from this subquery is not necessary since the result is eventually used in the "where in" clause.

Therefore, I applied "distinct" before "interset."

In addition, I applied selection in the original table first, which reduced redundant data for finding intersect, and rewrote the "interset" between three tables into "where" clauses to force it to change from $n^2$ sequential scan to inner join, which is much more efficient.

The new query is now:
```
with q1 as (
    select distinct ss_item_sk
    from store_sales, date_dim d1
    where ss_sold_date_sk = d1.d_date_sk
        and d1.d_year between 1999 AND 1999 + 2
),
q2 as(
    select distinct cs_item_sk
    from catalog_sales, date_dim d2
    where cs_sold_date_sk = d2.d_date_sk
        and d2.d_year between 1999 AND 1999 + 2
)
,
q3 as(
    select distinct ws_item_sk
    from web_sales, date_dim d3
    where ws_sold_date_sk = d3.d_date_sk
        and d3.d_year between 1999 AND 1999 + 2
)
select distinct iss.i_brand_id brand_id
     ,iss.i_class_id class_id
     ,iss.i_category_id category_id
 from q1
     ,q2
     ,q3
     ,item iss
 where q1.ss_item_sk = iss.i_item_sk
        and q2.cs_item_sk = iss.i_item_sk
        and q3.ws_item_sk = iss.i_item_sk;
```
After optimization, the running time is reduced from over 4 hours to only 6 seconds.