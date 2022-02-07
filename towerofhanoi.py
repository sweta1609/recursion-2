def TowerOfHanoi(n , source, destination, auxiliary):
    if n==1:
        print (source, destination)
        return
    elif n<1:
        return
    TowerOfHanoi(n-1, source, auxiliary, destination)
    print (source, destination)
    TowerOfHanoi(n-1, auxiliary, destination, source)    
n = int(input())
TowerOfHanoi(n , 'a', 'c', 'b')
          
