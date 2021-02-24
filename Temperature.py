def temperature(temp):
    print('What is the temperature in celsius?')
    temp = input()
    fahrenheit = int(temp) * 9/5 +32
    return fahrenheit


    
final = temperature('temp')
print((f'The temperature is {final} in fahrenheit!'))
