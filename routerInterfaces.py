#-------------------------------------------------------------------------------
# Name:        routerInterfaces
# Purpose:     returns # of interfaces you have for n routers
#
# Author:      anand
#
# Created:     07/10/2016
# Copyright:   (c) anand 2016
# Licence:     none
#-------------------------------------------------------------------------------
def routerInterfaces(i):
    # running sum will be returned
    sum = 0

    if i == 0:
        return sum
    elif i % 5 == 0:
        sum += 5
        return sum + routerInterfaces(i-1)
    else:
        sum += 10
        return sum + routerInterfaces(i-1)

def main():
    n = int(raw_input("Enter # of Routers"))
    ans = routerInterfaces(n)
    print(ans)

if __name__ == '__main__':
    main()