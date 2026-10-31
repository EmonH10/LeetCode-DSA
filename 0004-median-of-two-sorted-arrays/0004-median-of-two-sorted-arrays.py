class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        
        n1 = len(nums1)
        n2 = len(nums2)

        result = [0]*(n1+n2)
        i = 0
        j = 0
        k = 0
        while(i<n1 and j<n2):
            if nums1[i]<nums2[j]:
                result[k] = nums1[i]
                i+=1
                k+=1
            else:
                result[k] = nums2[j]
                j+=1
                k+=1

        while(i<n1):
            result[k] = nums1[i]
            k+=1
            i+=1
        
        while(j<n2):
            result[k] = nums2[j]
            k+=1
            j+=1

        
        i = 0
        j = len(result)-1

        while(i<j):
            i+=1
            j-=1

        if i == j:
            return result[i]

        return (result[i]+result[j])/2
