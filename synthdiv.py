def synthetic_div(polynomial, factor_list):

    count = 0
    tempval = 0
    result = []
    if count < len(factor_list):
        for i in range(0, len(polynomial)):
            tempval += polynomial[i] 
            tempval = tempval * factor_list[count]
        
        if tempval == 0:
             result.append(factor_list[count])
        count += 1
    return result

if __name__ == '__main__':
        print ("POLYNOMIAL SYNTHETIC DIVISION")
        N = [1, 3, 5]
        D = [1, -3, -2, 2, 3]
        print (synthetic_div(N, D))