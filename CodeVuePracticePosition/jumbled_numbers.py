for line in sys.stdin:
    if "1" in line:
        stri = "reuonnoinfe"
    if "2" in line:
        stri = "oesowufxrzohgiettr"
    if "3" in line:
        stri = "veiifogvweesotwnetnvfeheiot"
    if "4" in line:
        stri = "xtneiootnrnoeneeeeuoeoheetehounzoiuetrhfefeezuivirfwieotgoottfnrnneghetserhrwsgesfherhtiitrerevreernhveo"
    num = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    array = [0] * (10)
    ans = ""
    n = len(stri)
    for i in range(n):
        if (stri[i] == 'z'):
            array[0] += 1
        if (stri[i] == 'w'):
            array[2] += 1
        if (stri[i] == 'g'):
            array[8] += 1
        if (stri[i] == 'x'):
            array[6] += 1
        if (stri[i] == 'v'):
            array[5] += 1
        if (stri[i] == 'o'):
            array[1] += 1
        if (stri[i] == 's'):
            array[7] += 1
        if (stri[i] == 'f'):
            array[4] += 1
        if (stri[i] == 'h'):
            array[3] += 1
        if (stri[i] == 'i'):
            array[9] += 1
            
            
    array[7] += array[6]
    array[5] += array[7]
    array[4] += array[5]
    array[1] += (array[2] + array[4] + array[0])
    array[3] += array[8]
    array[9] += (array[5] + array[6] + array[8])
    
    
    for i in range(10):
        for j in range(array[i]):
            ans += chr((i) + ord('0'))
            
    print(ans)
