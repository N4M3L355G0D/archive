def confread():
    address=str()
    user=str()
    password=str()
    database=str()

    with open("config","r") as conf:
        for i in conf:
            line=i.split("=")
            if line[0] == "address":
                address=line[1].rstrip("\n")
            elif line[0] == "user":
                user=line[1].rstrip("\n")
            elif line[0] == "password":
                password=line[1].rstrip("\n")
            elif line[0] == "database":
                database=line[1].rstrip("\n")
            elif line[0] == "alternative_address":
                alternative_address=line[1].rstrip("\n")
    return [address,user,password,database,alternative_address]



