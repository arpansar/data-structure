arr = [2, 7, 11, 15]
target = 9

def TwoSum(arr,target):
	nums = {}
	for num in arr:
		match = target - num
		if match in nums:
			return[nums[match],arr.index(num)] 

		else:
			nums[num] = arr.index(num)


print TwoSum(arr,target)
