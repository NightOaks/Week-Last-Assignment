def gCd(x, y):
    if y==0:
        return x
    else:
        return gCd(y, x%y)
    
def main():
    x=eval(input("Pick a number."))
    y=eval(input("Pick another number."))
    print("GCD of",x,",",y,"=",gCd(x,y))

if __name__ == "__main__":
    main()