# TPC-DS_DW_F2022
## Group Members
- Arina Gepalova
- Tianheng Zhou
- You Xu

## Instructions
### Make/Build Binaries
- For MacOS users: run the following script in /DSGen-software-code-3.2.0rc1/tools
    ```
    make OS=MACOS
    ```

### Generate Data
Run the following script in /DSGen-software-code-3.2.0rc1/tools
```
mkdir ../../data
./dsdgen -SCALE 1GB -DIR ../../data -TERMINATE n
```
Note: replace "1GB" with the actual data size

### Create table in SQL server
Run the following three sql files located in /DSGen-software-code-3.2.0rc1/tools
- tpcds.sql
- tpcds_ri.sql
- tpcds_source.sql

### Load data
- Run /src/load_data.py
- Copy the printed out result into load_data.sql
- Run load_data.sql

### Generate 99 SQL
Run the following script in /DSGen-software-code-3.2.0rc1/tools
```
./dsqgen -input ../query_templates/templates.lst -directory ../query_templates -dialect sqlserver -scale 1GB -OUTPUT_DIR ../../query_sqlserver
```
- Replace "1GB" with the actual data size
- All queries are in numerical order in file /query_sqlserver/query_0.sql

## Queries to be fixed
Note: log EVERY STEP in /logs/query_log_YOURNAME.md and modify this doc with "done" after the fixed ones to avoid confusion.

You Xu:
- 05 done
- 06 done
- 07 done
- 08 done
- 11
- 14 done
- 17 done
- 18 done
- 21
- 24 done
- 25
- 31
- 32
- 33

Arina:
- 34
- 39
- 41
- 43
- 44
- 47
- 48
- 53
- 57
- 62
- 63
- 64
- 65

Tianheng:
- 67
- 68
- 69
- 75
- 76
- 78
- 80
- 84
- 86
- 87
- 89
- 94
- 98