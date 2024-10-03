def rotateArray(arr, k)
  n = arr.length
  k %= n
  
  def reverse(start, finish, arr)
    while start < finish
      arr[start], arr[finish] = arr[finish], arr[start]
      start += 1
      finish -= 1
    end
  end
  
  reverse(0, n-1, arr)
  reverse(0,k-1, arr)
  reverse(k,n-1, arr)
end


array = [1,2,3,4,5]
k=2 
rotateArray(array, k)
puts array.inspect