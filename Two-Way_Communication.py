

# Exercise: Two-Way Communication (Indirect Recursion)
# A phone call alternates between caller and receiver until the conversation ends.
#  The caller speaks first, then the receiver replies,
#  then the caller again, and so on. If the caller starts with n sentences,
#  and each reply is n-1 until n=0, simulate the conversation using indirect recursion.

# Tasks:
#   Write two mutually recursive functions callerNo and receiverNo.
#   Print a conversation simulation where each side speaks alternately.

# expected output:
#   caller(3)
#   Caller: i will speak 3 time
#   Receiver: i will speak 2 time
#   Caller: i will speak 1 time




def caller(n):
    if n != 0: # caller will start talking
        print(f"Caller: i will speak {n} time") # display the message
        return receiver(n-1) # decrement the value of n beacuse receiver will speak less by 1
#   Time Complexity: O(N)
#   Space Complexity: O(N)

def receiver(n):
    if n != 0: # reveiver will reply to the caller
        print(f"Receiver: i will speak {n} time") # display the message
        return caller(n) # return the same n beacuse we already decremented it
#   Time Complexity: O(N)
#   Space Complexity: O(N)


# test the function 
caller(3)
