class DynamicArray:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.length = 0
        self.array = [None] * capacity

    def get(self, i: int) -> int:
        if i < self.length:
            return self.array[i]

    def set(self, i: int, n: int) -> None:
        if i < self.length:
            self.array[i] = n

    def pushback(self, n: int) -> None:
        if self.length == len(self.array):
            self.resize()
        self.array[self.length] = n
        self.length += 1

    def popback(self) -> int:
        if self.length > 0:
            self.length -= 1
        return self.array[self.length]

    def resize(self) -> None:
        # Initialize the new array
        new_array = [None] * self.capacity * 2

        for ind in range(self.length):
            new_array[ind] = self.array[ind]
        self.capacity = len(new_array)
        self.array = new_array

    def getSize(self) -> int:
        return self.length

    def getCapacity(self) -> int:
        return self.capacity

    def get_array(self):
        return self.array

    # Leet Code
    @staticmethod
    def get_concatenation(nums):
        nums = nums + [None] * len(nums)
        length = 0
        for ind in range(len(nums)):
            if nums[ind] is None:
                nums[ind] = nums[length]
                length += 1
        return nums

if __name__=="__main__":
    d = DynamicArray(2)
    d.pushback(1)
    d.pushback(2)
    d.pushback(3)
    d.pushback(4)
    d.pushback(5)
    print(d.get_concatenation([1,3,2,1]))