arr=[1,2,3,4,5,6,7] #array which we are going to rotate using reversal algorithm
d=2 #number of rotations or value upto which we have to rotate
n=len(arr) #length of the array

def reversal_algo(arr,start,end): #function for reversal algorithm
    while(start<end):
        temp=arr[start]  #first value of the array is stored in a temporary variable
        arr[start]=arr[end] #last value of the array is stored at the first position
        arr[end]=temp #temp value is stored at the last position of the array
        start+=1 #start value is incremented by one
        end-=1 #end value id decremented by one

def leftrotate(arr,d): #function to do left rotation
    if(d==0): #if d value is 0 then there is no need for this algorithm
        return 0
    else:
        d=d%n
        reversal_algo(arr,0,d-1) #reversal done from 0 to d-1
        reversal_algo(arr,d,n-1) #reversal done from d to n-1
        reversal_algo(arr,0,n-1) #reversal done from 0 to n-1
    return arr #rotated arr value is returned

print(leftrotate(arr,d))

