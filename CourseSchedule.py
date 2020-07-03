#eachcourse has pre reqs and need to figure out how to take them
#we can store all the data as a graph and the edges go to the next class
#if there is a cycle you cant make the schedule because if a pre req for class 1 is class 2 and other way around that will have a cycle
#first option is to use dfs for checking a cycle we can do a depth limited seach deleting a node once we know it doesnt have a cycle and making time complexity O(n)

class Solution:
    def Cycle(self, graph, course, visited, visitedlist):
        if course in visitedlist:
            return visitedlist[course]

        if course in visited:
            return True

        if course not in graph:
            return False

        visited.add(course)
        ret = False

        for neighbor in graph[course]:
            if self.Cycle(graph, neighbor, visited, visitedlist):
                ret = True
                break

        visited.remove(course)
        visitedlist[course] = ret
        return ret



    def classes(self, amountCourses, preReqs):
        graph = {}

        for preReq in preReqs:
            if preReq[0] in graph:
                graph[preReq[0]].append(preReq[1])
            else:
                graph[preReq[0]] = [preReq[1]]

        for course in range(amountCourses):
            if self.Cycle(graph, course, set(), {}):
                return False

        return True

print(Solution().classes(2, [[1, 0]]))

print(Solution().classes(2, [[1, 0], [0, 1]]))