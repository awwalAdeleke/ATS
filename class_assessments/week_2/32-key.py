def key(record:dict):
    for key in record:
        print(f"{key} is the key and {record[key]} is the value.")
       
key({"a": "1" , "b" : "2" , "c" : "3"})