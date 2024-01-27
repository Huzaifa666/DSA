class Stacks:

    def __init__(self):
        self.stack = []

    def push(self, n: int) -> None:
        self.stack.append(n)

    def pop(self):
        self.stack.pop(len(self.stack) - 1)

    def peek(self) -> int:
        return self.stack[-1]

    def get_stack(self) -> None:
        print(self.stack)

    # Leetcode Problem No. 1
    @staticmethod
    def cal_points(operations) -> int:
        stack = []
        sum = 0
        for op in operations:
            match op:
                case '+':
                    stack.append(stack[len(stack) - 1] + stack[len(stack) - 2])

                case 'D':
                    stack.append(2 * stack[len(stack) - 1])

                case 'C':
                    sum -= stack[-1]
                    stack = stack[:-1]
                    continue

                case _:
                    stack.append(int(op))
            sum += stack[-1]
        return sum

    # Leetcode Problem No. 2
    @staticmethod
    def is_valid(string) -> bool:



# LeetCode Problem 3
class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val < self.min_number:
            self.min_number = val

    def pop(self) -> None:
        self.stack.pop(len(self.stack) - 1)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_number

    def getArray(self):
        print(self.stack)

if __name__ == '__main__':
    stack = MinStack()

    # ["MinStack", "push", "push", "push", "getMin", "pop", "top", "getMin"]
    # [[], [-2], [0], [-3], [], [], [], []]

    stack.push(-2)
    stack.push(0)
    stack.push(-3)
    print(stack.getMin())
    stack.pop()
    stack.getArray()
    stack.top()
    print(stack.getMin())
    stack.getArray()
    # stacks = Stacks()
    # print(stacks.is_valid("())"))



