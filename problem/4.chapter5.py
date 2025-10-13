class Calculator:
    def __init__(self):
        self.value = 0
    def add(self, val):
        self.value += val
    def minus(self,val):
        self.value -= val

def swip_negatives():
    nums = [1,-2,3,-5,8,-3]
    print( list(filter(lambda x : x>0, nums)) )

def mul3():
     nums = [1,2,3,4]
     print(list( map(lambda x: x*3 , nums) ))

def min_max_sum():
    nums =  [-8, 2, 7, 5,-3, 5, 0, 1]
    mi = min(nums)
    ma = max(nums)
    print(mi)
    print(ma)
    print(mi+ma)



if __name__ == "__main__":
    min_max_sum()