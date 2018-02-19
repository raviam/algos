def BucketSort(A):
	max = 0
	for i in A:
		if i > max:
			max = i
	bucket = [[False,0] for i in range(max)]
	for i in A:
		bucket[i-1][0] = True
		bucket[i-1][1] += 1
	for index,value in enumerate(bucket):
		if value[0]:
			for count in range(value[1]):
				yield index+1
def BubbleSort(A):
	unsorted = len(A)
	while unsorted > 1:
		for i in range(unsorted-1):
			if A[i] > A[i+1]:
				A[i],A[i+1] = A[i+1],A[i]
		unsorted -= 1
	return

def SelectionSort(A):
	last_idx = len(A)-1
	start = 0
	while start < last_idx:
		min_idx = start
		for i in range(start,last_idx+1):
			if A[i] < A[min_idx]:
				min_idx = i
		A[min_idx],A[start] = A[start],A[min_idx]
		start += 1
	return
def InsertionSort(A):
    n = len(A)
    for i in range(1,n):
        val = A[i]
        inserted = False
        for j in range(i-1,-1,-1):
            if A[j] > val:
                A[j+1] = A[j]
            else:
                A[j+1] = val
                inserted = True
                break
        if not inserted:
            A[0] = val
    return
def MergeSort(A):
	mid_idx = len(A)//2
	if mid_idx == 0:
		return A
	left = A[:mid_idx]
	right = A[mid_idx:]
	left = MergeSort(left)
	right = MergeSort(right)
	return(_merge(left,right))
def _merge(l,r):
	lid = 0
	rid = 0
	merged_list = []
	while lid < len(l) and rid < len(r):
		if r[rid] < l[lid]:
			merged_list.append(r[rid])
			rid +=1
		else:
			merged_list.append(l[lid])
			lid +=1
	merged_list.extend(r[rid:len(r)]+l[lid:len(l)])
	return merged_list