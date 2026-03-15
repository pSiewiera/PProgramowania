def Add(numbers):
    if not numbers:
        return 0
    nums= numbers.replace("\n", ",")
    nums = nums.split(",")
    sum=0
    for num in nums:
        sum+=int(num)
    return sum