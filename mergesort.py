def merge_sort(arr):
    if len(arr)>1:
        left_arr=arr[:len(arr)//2]
        right_arr=arr[len(arr)//2:]
        
        #recursion
        merge_sort(left_arr)
        merge_sort(right_arr)
        
        #merge_sort
        i,j,k=(0,0,0)
        while i<len(left_arr) and j <len(right_arr):
            if left_arr[i]< right_arr[j]:
                arr[k]=left_arr[i]
                i+=1
            else:
                arr[k]=right_arr[j]
                j+=1
            k+=1
        while i <len(left_arr):
            arr[k]=left_arr[i]
            i+=1
            k+=1    
        while j <len(right_arr):
            arr[k]=right_arr[j]
            j+=1
            k+=1
        
        
        

    
    
    

arr_test=[5643,645,56,765,567,657,56768,856,567,56756,7,56353,53,34534,5]

merge_sort(arr_test)
print(arr_test)

