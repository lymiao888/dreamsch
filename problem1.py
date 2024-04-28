def min_subsequences(source, target):
    '''
    Args:
        source: 源字符串
        target: 目标字符串，需要在源字符串中找到的子序列
    Returns:
        count: 在源字符串中找到目标字符串的最小子序列数量，如果无法找到返回-1
    '''
    pass

    count = 0
    source_pointer = 0
    
    while source_pointer < len(target):
        found_subsequence = False
        for char in source:
            if char == target[source_pointer]:
                source_pointer += 1
                found_subsequence = True
            if source_pointer == len(target):
                break
        if not found_subsequence:
            return -1
        count += 1
    
    return count


#test
source = "abc"
target = "abcbc"
print(source)
print(target)
print(min_subsequences(source, target)) 

source = "abc"
target = "acdbc"
print(source)
print(target)
print(min_subsequences(source, target)) 

source = "xyz"
target = "xzyxz"
print(source)
print(target)
print(min_subsequences(source, target)) 