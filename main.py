'''
Your goal is to write a function that finds gaps between given intervals.
The intervals will be an UNSORTED tuple containing tuples. Each inner tuple will represent an integer interval. It will have two elements: the first element is the beginning of the interval, the second element is the end of the interval. The first element is guaranteed to be strictly less than the second element.
Here is an example of an input tuple:
intervals_1 = (
    (5, 10),
    (12, 15),
    (16, 20),
    (20, 25),
    (27, 30),
)
For clarity of the example, this tuple is sorted. However, note that some of the other test cases are NOT SORTED.
In this example, we can see that the earliest interval ends at 10, and the next interval starts at 12. Thus, there is a gap from 10 to 12. Similarly, we can see there are two other gaps. Below is a tuple (in sorted order) showing all of the gaps for this example:
expected_output = (
    (10, 12), 
    (15, 16), 
    (25, 27)
)
Note that there is NOT a gap at 20. One interval ends at 20, and another starts at 20. Though one interval may start at the same time another ends, you are guaranteed there will be no overlap between the input intervals.
Write a function that accepts the UNSORTED input intervals and returns a SORTED tuple of tuples containing all the gaps.
'''

def find_gaps(intervals):
    #
    start = []
    end = []
    intervals = sorted(intervals)
    print(intervals)
    for interval in intervals:
      start.append(interval[1])
      end.append(interval[0])
    end.pop(0)
    start.pop()
    output = []
    for i,j in zip(start,end):
      if j-i != 0:
        output.append((i,j))
    print (output)

    # convert to tuple to match expected output types
    return tuple(output)

intervals_1 = (
    (5, 10),
    (12, 15),
    (16, 20),
    (20, 25),
    (27, 30),
)
assert find_gaps(intervals_1) == ((10, 12), (15, 16), (25, 27))

intervals_2 = (
    (27, 30),
    (16, 20),
    (12, 15),
    (20, 25),
    (5, 10),
)
assert find_gaps(intervals_2) == ((10, 12), (15, 16), (25, 27))

intervals_3 = (
    (17, 35),
)
assert find_gaps(intervals_3) == tuple()

intervals_4 = (
    (1, 2),
    (2, 3),
    (3, 4),
    (4, 5),
)
assert find_gaps(intervals_4) == tuple()


print("All tests passed!")
print("Discuss time and space complexity if there's time remaining")

"""
***NOTES TO INTERVIEWER***
"""
