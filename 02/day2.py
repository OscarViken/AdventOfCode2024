
def is_safe(nums: list[int]) -> bool:

    diffs = [abs(n1-n2) for n1, n2 in zip(nums, nums[1:])]
    if not all(1 <= d <= 3 for d in diffs):
        return False
    if all(n1 < n2 for n1, n2 in zip(nums, nums[1:])):
        return True
    if all(n1 > n2 for n1, n2 in zip(nums, nums[1:])):
        return True
    return False

def check1(line: str) -> bool:
    nums = list(map(int, line.split()))
    return is_safe(nums)

def check2(line: str) -> bool:
    nums = list(map(int, line.split()))
    for i in range(len(nums)):
        if is_safe(nums[:i] + nums[i+1:]):
            return True
    return False


with open('input.txt', 'r') as f:
    lines = f.readlines()

good_reports1 = [r for r in lines if check1(r)]

good_reports2 = [r for r in lines if check1(r) or check2(r)]



print(len(good_reports1))
print(len(good_reports2))
