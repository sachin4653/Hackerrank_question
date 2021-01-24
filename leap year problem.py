def is_leap(year):
    if year in range(1900,100001):
        p=year/4
        if p%2==0:
            t=year/100
            if t%2==0:
                p=year/400
                if p%2==0:
                    return True
        else:
            return False
        
    

year = int(input())
print(is_leap(year))
