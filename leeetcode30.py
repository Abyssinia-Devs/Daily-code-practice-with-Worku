nums =[19,25,39,31,20,10,40,38,28,35,11,11,18,26,26,24,29,14,10,37]
p=23

if sum(nums) < p:
    print(-1)
    
rem = sum(nums) % p
if rem==0:
    print(0)
first = []
if rem in nums:
    first.append(1)
else:
    r=0
    for i in range(len(nums)):
        sumed = sum(nums)
        if (sum(nums)-nums[i])%p==0:
            first.append(1)
        c = len(nums) #len =0,1,2,3,4,5
        while i+1 != c: #3:4  2:3   1:2  1:   1:   1:  1:
            r = nums[i] + sum(nums[i+1: c])
            
            if (sum(nums)-r)%p==0:
                first.append(1+len(nums[i+1:c]))
            c -=1
            r = 0
    result = sorted(first)
if len(sorted(first)) !=0 and (sorted(first)[0] != len(nums)):
    print(sorted(first)[0])
else:
    print(-1)
    
    
    
    
    """total_sum = sum(nums)
rem = total_sum % p
if rem == 0:
    print( 0)

n = len(nums)
mod_to_index = {0: -1}
current_prefix = 0
min_len = n + 1

for i in range(n):
    current_prefix += nums[i]
    current_mod = current_prefix % p
    needed_mod = (current_mod - rem) % p
    if needed_mod in mod_to_index:
        length = i - mod_to_index[needed_mod]
        min_len = min(min_len, length)
    mod_to_index[current_mod] = i

return min_len if min_len < n else -1"""