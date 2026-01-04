str1  = input('Enter a String to reverse:')

for char in str1:
    if(str1.count(char)) ==1:
        print('Non-repeated char is = ', char)
    break;

