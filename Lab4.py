
#Program no 1:
stack=[]
stack.append(4)
stack.append(5)
stack.append(6)
print("Length of stack",len(stack))
print ("Numbers in stack are: ",stack)
print ("The top element of the stack",stack[0])
print(stack.pop())
print(stack.pop())
print(stack.pop())
print ("Stack after pop: ",stack)

#Program no 2:
queue=[]
queue.append(4)
queue.append(5)
queue.append(6)
print("Length of stack",len(stack))
print ("Numbers in stack are: ",stack)
print(queue.pop())
print(queue.pop())
print(queue.pop())
print ("Stack after pop: ",queue)

#Program no 3:
def binarySearch(array, x, low, high):
    while low <= high:

        mid = (low+high)//2

        if x == array[mid]:
            return mid

        elif x > array[mid]:
            low = mid + 1

        else:
            high = mid - 1

    return -1


array = [3, 4, 5, 6, 7, 8, 9]
x = 4

result = binarySearch(array, x, 0, len(array)-1)

if result != -1:
    print("Element is present at index " + str(result))
else:
    print("Not found")




