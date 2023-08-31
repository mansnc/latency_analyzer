
def get_round_trip_time(ping_str):
    # look for time and extract the number 
    start_sep='time='
    end_sep='ms'
    result=[]
    tmp=ping_str.split(start_sep)
    for par in tmp:
        if end_sep in par:
            result.append(par.split(end_sep)[0])
    #print(result)

    time = []
    for item in result:
        time.append(int(item))
    # print(time)
    
    return time