'''
In this solution we have used backtracking, understanding was little tough, but amazing question
'''
def squareFull(self,nums):
    result = []

    def dfs(nums,path,resutl):
        if not nums:
            result.append(path)
        
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            if path and not square(path[-1]+nums[i]):
                continue
            #BackTracking
            dfs(nums[:i]+nums[i+1:],path+[nums[i]],result)



    def square(num):
        from math import sqrt
        return pow(int(sqrt(num)),2)==num

    dfs(sorted(nums),[],result)
    return len(result)