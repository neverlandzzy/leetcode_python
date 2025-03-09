"""
Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left-justified, and no extra space is inserted between words.

Note:

A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.


Example 1:

Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
Example 2:

Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
Explanation: Note that the last line is "shall be    " instead of "shall     be", because the last line must be left-justified instead of fully-justified.
Note that the second line is also left-justified because it contains only one word.
Example 3:

Input: words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20
Output:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]


Constraints:

1 <= words.length <= 300
1 <= words[i].length <= 20
words[i] consists of only English letters and symbols.
1 <= maxWidth <= 100
words[i].length <= maxWidth
"""

from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        lst = []
        width = 0
        i = 0

        while i < len(words):
            if len(words[i]) + width <= maxWidth:
                width += len(words[i]) + 1
                lst.append(words[i])
                i += 1
            else:
                # 本行里所有的剩余空间(space)：maxWidth - 已经加入的每个word和word后面space的长度(length), 最后要加回最后一个word后面的space（+1）
                space = maxWidth - width + 1
                # 本行里有多少个单词间padding的空格（也就是单词数 - 1）
                intervals = len(lst) - 1

                # 本行里将空格均摊到每个interval后，剩下的不能均摊的空格
                extra_space = 0
                if intervals != 0:
                    extra_space = space % intervals
                line = []
                for w in lst:
                    line.append(w)
                    if len(lst) > 1:
                        if w is not lst[-1]:
                            line.append(' ' * (space // intervals + 1))

                            if extra_space > 0:
                                line.append(' ')
                                extra_space -= 1
                    else:
                        line.append(' ' * space)

                result.append(''.join(line))
                lst.clear()
                width = 0

        last_line = []
        width = 0

        for w in lst:
            last_line.append(w)
            width += len(w)

            if w is not lst[-1]:
                last_line.append(' ')
                width += 1

        last_line.append(' ' * (maxWidth - width))
        result.append(''.join(last_line))
        return result

    def run(self):
        words1 = ["This", "is", "an", "example", "of", "text", "justification."]
        words2 = ["What", "must", "be", "acknowledgment", "shall", "be"]
        words3 = ["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain", "to", "a",
                  "computer.", "Art", "is", "everything", "else", "we", "do"]

        print(self.fullJustify(words1, 16))
        print(self.fullJustify(words2, 16))
        print(self.fullJustify(words3, 20))


if __name__ == "__main__":
    Solution().run()
