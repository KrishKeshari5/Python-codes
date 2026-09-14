def changepi(n):
    if len(n) < 1:
        return n 
    elif n[:2] == 'pi':
        return '3.14' + changepi(n[2:])

    else:
        return n[0] + changepi(n[1:])

print(changepi('hellopipihello'))
    
        
    