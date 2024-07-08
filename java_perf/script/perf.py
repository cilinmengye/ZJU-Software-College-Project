import sqlite3
import re

conn = sqlite3.connect('perf_data.db')
cursor = conn.cursor()

create_table = """
CREATE TABLE IF NOT EXISTS perfdata (
    command TEXT,
    pid INTEGER,
    timep FLOAT,
    function TEXT,
    lib TEXT
);
"""
cursor.execute(create_table)
conn.commit()

command = ""
pid = ""
timep = 0.0

filepath = "/home/cilinmengye/java_perf/perf/second_sparse/out.perf"

with open(filepath) as file:
    for line in file:
        tokens = line.split()
        tokens = [token.strip('():[]') for token in tokens]
        tklen = len(tokens)
        if tklen >= 5:
            command = ""
            for i in range(tklen - 5 + 1):
                if i != 0:
                    command = command + " "
                command = command + tokens[i]
            pid = tokens[tklen - 5 + 1]
            try:
                timep = float(tokens[tklen - 5 + 2])
            except ValueError:
                print(f"Skipping line due to ValueError: {line} and {tokens[2]}")
                continue
        elif len(tokens) >=3:
            fct = tokens[1].split('+')[0]
            lib = tokens[2]
            insert_table = """
            INSERT INTO perfdata (command, pid, timep, function, lib) VALUES (?, ?, ?, ?, ?);
            """
            record = (command, pid, timep, fct, lib)
            cursor.execute(insert_table, record)
            print(f"{command} {pid} {timep} {fct} {lib}\n")            
# 提交更改并关闭连接
conn.commit()
conn.close()
