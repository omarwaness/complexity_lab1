

# Exercise: File System Depth (Tree Recursion)
# A computer file system can be represented as a tree. 
# Each folder contains files or subfolders. Given a nested directory structure, 
# compute the maximum depth of the file system.

# Tasks:
#   Write a tree-recursive function maxDepth(fs) to compute the depth.
#   Analyze the complexity and compare with an iterative BFS approach.

# expected output:
#   maxDepth(file_system)
#   3   


from collections import deque


def maxDepth(fs):
    if not isinstance(fs, dict) or not fs:  # Base case: if it's not a dictionary or it's empty
        return 0
    return 1 + max((maxDepth(subdir) for subdir in fs.values()), default=0)
#   Time Complexity: O(N)
#   Space Complexity: O(D)  


def maxDepth(fs):
    if not fs:  # Edge case: Empty dictionary
        return 0
    queue = deque([(fs, 1)])  # (current_directory, current_depth)
    max_depth = 0
    while queue:
        current, depth = queue.popleft()
        max_depth = max(max_depth, depth)
        for key, value in current.items():
            if isinstance(value, dict):  # Only enqueue subdirectories
                queue.append((value, depth + 1))
    return max_depth
#   Time Complexity: O(N)
#   Space Complexity: O(N)  


# Example file system
file_system = {
    "home": {
        "user": {
            "documents": {
                "project": {
                    "file1.txt": None,
                    "file2.txt": None
                }
            }
        },
        "downloads": {
            "movie.mp4": None
        }
    }
}

# Compute max depth
print(maxDepth(file_system))
print(maxDepth(file_system))