### 5
- replace 'stddev_samp' with 'stdev' in line 6 and 31

### 6
- replace '(cast('2002-08-04' as date) +  30 days)' with '(dateadd(day, 30, cast('2002-08-04' as date)))' in line 15, 31, 57
- replace '||' with '+' in line 71, 78, 85

### 7
- replace '(cast('1999-02-22' as date) + 90 days)' with '(dateadd(day, 90, cast('1999-02-22' as date)))' in line 11, 23

### 8
- replace 'substr' with 'substring' in line 12