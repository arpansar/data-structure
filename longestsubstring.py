def LongestSubString(string):
	lastseen = {}
	longest = [0,1]
	startidx = 0
	for i, char in enumerate(string):
		if char in lastseen:
			startidx = max(startidx,lastseen[char]+1)
		if longest[1] - longest[0] < i+1 - startidx:
			longest = [startidx,i+1]
		lastseen[char] = i
	return longest[1] - longest[0]

string = "pwwkew"

print LongestSubString(string)	