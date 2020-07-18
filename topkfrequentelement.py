#given an array what is the top k most freq elements for example if k is 3 and then we need to list top 3 most common elements

#sorting array with how many there is as a tuple will make sense for this but its not as fast it is nlogn
#can use a heap
import heapq
import collections

class solver(object):
  def topFreq(self, nums, k):
    c = collections.defaultdict(int)
    for n in nums:
      c[n] += 1

    heap = []
    for num, c in c.items():
      heap.append((-c, num))
    heapq.heapify(heap)

    result = []
    for i in range(k):
      result.append(heapq.heappop(heap)[1])
    return result


arr = [3, 3, 3, 4, 5, 5, 6, 6, 5, 8, 8, 8, 9, 7, 8]
run = solver()
k = 3
print(solver.topFreq(run, arr, k))