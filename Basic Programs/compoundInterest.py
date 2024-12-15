def compound_interest(p, r,t):
    print("Principal amount:", p)
    print("Time :", t)
    print("Rate :", r)

    #Calculate COmpound Interest
    Amount = p * (pow((1 + r / 100), t))
    CI = Amount - p
    print("Compound interest :", CI)


compound_interest(10000,10.25,5)