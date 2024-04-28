# problem1
 
## brief
A subsequence of a string is a new string that is formed from the original string by deleting
some (can be none) of the characters without disturbing the relative positions of the remaining
characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
Given two strings source and target, return the minimum number of subsequences of source
such that their concatenation equals target. If the task is impossible, return -1.
* Example 1:
Input: source = "abc", target = "abcbc"
Output: 2
Explanation: The target "abcbc" can be formed by "abc" and "bc", which are subsequences of source "abc".
* Example 2:
Input: source = "abc", target = "acdbc"
Output: -1
Explanation: The target string cannot be constructed from the subsequences of source string due to the character "d" in target string.
* Example 3:
Input: source = "xyz", target = "xzyxz"
Output: 3
Explanation: The target string can be constructed as follows "xz" + "y" + "xz".

# problem2

## brief
每输入一个字符串，检查括号是否匹配。如果只有左括号没有右括号，我们就在它下面标一个x，如果只有右括号，我们就在它下面标一个问号。每行为单独测试用例。

```input
bge)))))))))
((IIII))))))
()()()()(uuu
))))UUUU((()
```
```output
bge)))))))))
   ?????????
((IIII))))))
        ????
()()()()(uuu
        x
))))UUUU((()
????    xx
```

# run

```
sh run.sh
```