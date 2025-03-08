
# Bonus Challenge: The Towers of Hanoi (Optimization & Complexity)
# The classic Towers of Hanoi involves moving N disks from A → C, using B as an auxiliary. The goal is to minimize the number of moves.

# Tasks:
#   Write a recursive solution for hanoi(N, A, B, C).
#   Prove that the minimum number of moves is O(2^N - 1).
#   Implement a memoized version and analyze its impact.

# expected output:
#   hanoi(3, 'A', 'B', 'C')
#   Move disk 1 from A to C
#   Move disk 2 from A to B
#   Move disk 1 from C to B
#   Move disk 3 from A to C
#   Move disk 1 from B to A
#   Move disk 2 from B to C
#   Move disk 1 from A to C


def hanoi(N, A, B, C):
  if N == 0:    # stop condition
    return
  hanoi(N-1, A, C, B)  # move the top N-1 disks from A to B, using C as auxiliary
  print(f"Move disk {N} from {A} to {C}")  # move the Nth disk from A to C
  hanoi(N-1, B, A, C)  # move the N-1 disks from B to C, using A as auxiliary
#   Time Complexity: O(2^N - 1)
#   Space Complexity: O(N)  



# test the function
hanoi(3, 'A', 'B', 'C')