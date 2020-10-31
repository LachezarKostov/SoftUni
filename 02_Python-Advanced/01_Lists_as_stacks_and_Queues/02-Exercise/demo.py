def create_stack():
    stack = []
    return stack


def push(stack, elem):
    stack.append(elem)


def pop(stack):
    if len(stack) > 0:  # if stack:
        return stack.pop()

    return None


#############################
from collections import deque


def create_queue():
    return deque()


def enqueue(queue, elem):
    queue.append(elem)


def dequeue(queue):
    if queue:
        return queue.popleft()
    return None

import torch
x = torch.rand(5, 3)
print(x)



