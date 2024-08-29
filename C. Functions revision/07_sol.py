cars = ["URUS","KIGER","SCORPIO","RANGE_ROVER","THAR","XUV7OO"]

def singh(lst,idx=0):
    if(idx == len(lst)):
        return
    print(lst[idx])
    singh(lst,idx+1)
    
singh(cars)    