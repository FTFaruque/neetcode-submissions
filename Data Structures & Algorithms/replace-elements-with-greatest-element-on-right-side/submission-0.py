class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        i = 0
        j = i+1

        for i in range(len(arr)):
           x = sorted(arr[j:len(arr)], reverse=True)
           if i == len(arr) - 1:
                arr[len(arr) - 1] = -1
           else:
                arr[i] = x[0]
           j += 1 
        
        return arr
        