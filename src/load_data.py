import pathlib
main_path = str(pathlib.Path(__file__).parent.resolve())[:-4]
with open(main_path + "/DSGen-software-code-3.2.0rc1/tools/tpcds.sql") as ddl:
    for line in ddl:
        if line.startswith('create table'):
            table = line.replace("\n", '').split()[2]
            # replace the path with your own path
            print("bulk insert {} from '{}/data/{}.dat' with (fieldterminator='|',rowterminator='0x0a',batchsize=1000);".format(table, main_path, table))