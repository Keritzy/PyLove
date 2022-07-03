def v_moonweight(weightinc, earthweight, yearnum):
    x = .165
    currentweight = earthweight
    for y in range(yearnum):
        currentweight = currentweight + weightinc
        moonweight = currentweight * x
        print(moonweight)
 
 
v_moonweight(100, .20, 30)
