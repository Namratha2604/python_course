#arranging in ascending order or decsending order
#log n
#####SELECTION SORT######
def selection_sort(a, start,end):
    if (start== end): #base case, zero elements!
        return

    idx_max = find_idx_of_max_elt(a,start,end)
    a[idx_max] , a[start] = a[start], a[idx_max]#swap
    selection_sort(a, start+1,end)

def find_idx_of_max_elt(a,start,end):
    max=start
    for i in range(start+1,end):
        max=start
        for i in range (start+1,end):
            if(a[i]> a[max]):
                max=i
        return max
def sort(a):
        selection_sort(a,0,len(a))

items=[5,3,87,8,9,0]
print(sort(items))

### T(n) = T(n-1) + A*n + B 
## T(n) = n^2
