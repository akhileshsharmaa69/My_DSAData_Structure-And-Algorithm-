arr=[70,90,40,50,20,30,10]
n=len(arr)# how element in list count
for i in range(n-1):# control the total pasees
    for j in range(n-1-i):# compare the current adjacent
        if arr[j]>arr[j+1]:# check  the left element graeter than right
            arr[j],arr[j+1]=arr[j+1],arr[j] # swap the element

print("Sorted array",arr)        

def bubble_sort(arr):
    n=len(arr)
    for i in range(n):
        swap=False
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swap=True
        if not swap:
            break
arr=[50,60,10,80,20]   
bubble_sort(arr)
print("sorted array is",arr)

                
