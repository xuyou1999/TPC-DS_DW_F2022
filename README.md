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