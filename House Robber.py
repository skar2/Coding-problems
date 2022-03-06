n=int(input())
nums=[]

res1=[]

for i in range(n):
    nums.append(int(input()))

for i in range(n):
    ind = nums.index(max(nums))
    res1.append([nums[ind],ind])
    nums[ind]=0

rob=0
ind1=[]

for j in range(len(res1)):
    if res1[j][1]-1 not in ind1 and res1[j][1]+1 not in ind1:
        rob+=res1[j][0]
        ind1.append(res1[j][1])



print(rob)
