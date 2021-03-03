def calculate(min,max):
    # 請用你的程式補完這個函式的區塊
    sum=0
    for n in range(min,max+1):
        sum+=n
    else:
        print(sum)

calculate(1,3)# 你的程式要能夠計算 1+2+3，最後印出 6
calculate(4,8)# 你的程式要能夠計算 4+5+6+7+8，最後印出 30

def avg(data):
    # 請用你的程式補完這個函式的區塊
    employees=data["employees"]
    sum=0
    for Data in employees:
         money=(Data["salary"])
         sum=sum+money
    people=len(data["employees"])
    print(sum/people)

avg({
    "count":3,
    "employees":[
        {
            "name":"John",
            "salary":30000
        },
        {
            "name":"Bob",
            "salary":60000
        },
        {
            "name":"Jenny",
            "salary":50000
        }
    ]
})# 呼叫 avg 函式


def maxProduct(nums):
    # 請用你的程式補完這個函式的區塊
    list=[]
    for x in nums:
        for y in nums:
            if y==x:
                continue
            else:
                list.append(y*x)
    print(max(list))


maxProduct([5,20,2,6]) # 得到 120 因為 20 和 6 相乘得到最大值
maxProduct([10,-20,0,3])# 得到 30 因為 10 和 3 相乘得到最大值

def twoSum(nums,target):
    # your code here
    for x in nums:
        for y in nums:
            if x+y==target:
                X=nums.index(x)
                Y=nums.index(y)
                return [X,Y]
            elif x==y:
                continue
            
result=twoSum([2,11,7,15],9)
print(result) # show [0, 2] because nums[0]+nums[2] is 9

def maxZeros(nums):
    nlist=[]
    n=0
    for x in nums:
        if x==1:
            nlist.append(n)
            n=0
            continue
        else:
            n=n+1
    nlist.append(n)
    print(max(nlist))



maxZeros([0,1,0,0])# 得到 2
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0])# 得到 4
maxZeros([1, 1, 1, 1, 1]) # 得到 0



