# TPC-DS_DW_F2022
## Group Members
- Arina Gepalova
- Tianheng Zhou
- You Xu
- Marie Giot

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
- File /src/split_queries.ipynb may help spliting the queries
- Alternatively, all 99 queries are separately stored in /query_sqlserver_org_order already

### Run Queries
- /src/auto_run_sql.ipynb will help connecting, running 99 queries and documenting the runtime automatically. 
- Add database credentials in file "/src/credential.json" in the following format:
```
{
    "server": "yourServer",
    "database": "yourDatabase",
    "username": "yourUsername",
    "password": "yourPassword"
}
```

## Work Plan
### Queries to be fixed
Note: log EVERY STEP in /logs/query_log_YOURNAME.md and modify this doc with "done" after the fixed ones to avoid confusion.

You Xu:
- 05 done
- 06 done
- 07 done
- 08 done
- 11 done
- 14 done
- 17 done
- 18 done
- 21 done
- 24 done
- 25 done
- 31 done
- 32 done
- 33 done
- 34 done
- 39 done
- 41 done
- 43 done
- 44 done
- 47 done

Arina:
- 48
- 53 done
- 57 done
- 62 done
- 63 done
- 64 done
- 65 done

Tianheng:
- 67 done
- 68 done
- 69 done
- 75 done
- 76 done
- 78 done
- 80 done

Marie:
- 84 done
- 86 done
- 87 done
- 89 done
- 94 done
- 98 done

### Query Optimization
#### 1GB
- 10: 500s
- 35: 1060s
- 23: 85s
- 14: >4hrs - see /logs/query_log_yx.md

## Order issue
- The order number correspondence documents is under /logs
- Correct ordered queries in /query_sqlserver_org_order
- All already renamed and moved except 48

## Runtime limitations
- The test run is on ARM64 MacOS machine. Thus, it is based on Microsoft's Azura SQL Edge docker container developer version, which limit the CPU performance to maximun 4 cores.
- When running query 23, only 1 CPU core is allocated . Reason unknow. This only happens under the environment condition specified above. We believe this issue if irrelevant to our project but due to the lack of ARM64 support from Microsoft.

## Results
In /result folder for scale factors 1, 2, 5, 10