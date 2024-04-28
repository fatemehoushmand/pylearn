def diamond(n):
    for i in range(n+1):
        print((n-i)*' '+(2*i-1)* '*')
    for i in range(n+1):
        print(i*' '+(-2*i+(2*n-1))*'*')    
        
        
diamond(6)