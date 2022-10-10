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