list=[{"name":"shoe","types":[
                                {"t_name":"adidas","t_price":1500,"t_qty":4},
                                {"t_name":"puma","t_price":2000,"t_qty":5},
                                {"t_name":"nike","t_price":2500,"t_qty":8}]},
      {"name":"shirt","types":[
                                {"t_name":"Snitch","t_price":800,"t_qty":4},
                                {"t_name":"TommyHilfiger","t_price":3500,"t_qty":8},
                                {"t_name":"Arrow","t_price":1300,"t_qty":6}]},
      {"name":"sock"}]

def search(input):
    found =False
    for item in list:
        if item["name"].lower() == input.lower() :
            found = True
            break
    
    return found


def price_comparison(input):
    result=[]
    for item in list:
        if item["name"].lower() == input.lower() :
            result = item["types"]
            break
    
    return result   