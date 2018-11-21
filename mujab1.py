def konversisuhu(c=0,f=32):
    if c == 0:
        f=float((c*9/5)+32)
        print('suhu',c,'celcius setara dengan',f,'fahrenheit')
    elif f== 32:
        c=float((c-32)*5/9)
        print ('suhu',f,'fahrenheit setara dengan',c,'celcius')
