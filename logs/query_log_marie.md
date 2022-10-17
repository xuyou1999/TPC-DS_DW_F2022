###84
-add 'as temporary_table' after 'from catalog_sales)' at line 12


### 86
- replace line 21 by '(dateadd (day, -30, cast ('2002-05-18' as date)))and (dateadd (day, 30, cast ('2002-05-18' as date)))'

###87

-replace 'd1.d_date' by (dateadd (day, 5, d1.d_date)) at line 20

###89
-replace 'substr' with 'substring' in line 3, 20
-add a "as" between ')' and 'ms' line 18


### 94
-replace 'substr' with 'substring' in line 3, 27 and 30

### 98
- replace lines 29, 60, 91 by '(dateadd (day, 14, cast('2001-08-04' as date)))'
-replace '||' with '+' in lines 103, 110, 117

