def synthetic_div(polynomial, factor_list):

    count = 0
    tempval = 0
    result = []
    for j in range(count, len(factor_list)):
        for i in range(0, len(polynomial)):
            print(tempval)
            tempval = tempval + polynomial[i] 
            print(tempval)
            tempval = tempval * factor_list[count]
            print(tempval)

        if tempval == 0:
             result.append(factor_list[count])
        tempval = 0    
        count += 1
    return result

if __name__ == '__main__':
        print ("POLYNOMIAL SYNTHETIC DIVISION")
        N = [4, -19, 12]
        D = [0.75, 1.5, 1.0, 3, -0.75, 0.5, -0.5, 0.25, -0.25, 6, 2, 4, 12, -12, -2, -6, -4, -3, -1, -1.5]
        print (synthetic_div(N, D))
