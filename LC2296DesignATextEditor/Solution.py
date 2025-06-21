"""
Design a text editor with a cursor that can do the following:

Add text to where the cursor is.
Delete text from where the cursor is (simulating the backspace key).
Move the cursor either left or right.
When deleting text, only characters to the left of the cursor will be deleted. The cursor will also remain within the actual text and cannot be moved beyond it. More formally, we have that 0 <= cursor.position <= currentText.length always holds.

Implement the TextEditor class:

TextEditor() Initializes the object with empty text.
void addText(string text) Appends text to where the cursor is. The cursor ends to the right of text.
int deleteText(int k) Deletes k characters to the left of the cursor. Returns the number of characters actually deleted.
string cursorLeft(int k) Moves the cursor to the left k times. Returns the last min(10, len) characters to the left of the cursor, where len is the number of characters to the left of the cursor.
string cursorRight(int k) Moves the cursor to the right k times. Returns the last min(10, len) characters to the left of the cursor, where len is the number of characters to the left of the cursor.
 

Example 1:

Input
["TextEditor", "addText", "deleteText", "addText", "cursorRight", "cursorLeft", "deleteText", "cursorLeft", "cursorRight"]
[[], ["leetcode"], [4], ["practice"], [3], [8], [10], [2], [6]]
Output
[null, null, 4, null, "etpractice", "leet", 4, "", "practi"]

Explanation
TextEditor textEditor = new TextEditor(); // The current text is "|". (The '|' character represents the cursor)
textEditor.addText("leetcode"); // The current text is "leetcode|".
textEditor.deleteText(4); // return 4
                          // The current text is "leet|". 
                          // 4 characters were deleted.
textEditor.addText("practice"); // The current text is "leetpractice|". 
textEditor.cursorRight(3); // return "etpractice"
                           // The current text is "leetpractice|". 
                           // The cursor cannot be moved beyond the actual text and thus did not move.
                           // "etpractice" is the last 10 characters to the left of the cursor.
textEditor.cursorLeft(8); // return "leet"
                          // The current text is "leet|practice".
                          // "leet" is the last min(10, 4) = 4 characters to the left of the cursor.
textEditor.deleteText(10); // return 4
                           // The current text is "|practice".
                           // Only 4 characters were deleted.
textEditor.cursorLeft(2); // return ""
                          // The current text is "|practice".
                          // The cursor cannot be moved beyond the actual text and thus did not move. 
                          // "" is the last min(10, 0) = 0 characters to the left of the cursor.
textEditor.cursorRight(6); // return "practi"
                           // The current text is "practi|ce".
                           // "practi" is the last min(10, 6) = 6 characters to the left of the cursor.
 

Constraints:

1 <= text.length, k <= 40
text consists of lowercase English letters.
At most 2 * 10^4 calls in total will be made to addText, deleteText, cursorLeft and cursorRight.
"""

class TextEditor:

    def __init__(self):
        self.text = ""
        self.cursor = 0

    def addText(self, text: str) -> None:
        self.text = self.text[:self.cursor] + text + self.text[self.cursor:]
        self.cursor += len(text)

    def deleteText(self, k: int) -> int:
        if self.cursor == 0:
            return 0
        deleted_count = min(k, self.cursor)
        self.text = self.text[:self.cursor - deleted_count] + self.text[self.cursor:]
        self.cursor -= deleted_count
        return deleted_count

    def cursorLeft(self, k: int) -> str:
        if self.cursor <= k:
            self.cursor = 0
            return ""
        self.cursor -= k
        return self.text[max(0, self.cursor - 10):self.cursor]

    def cursorRight(self, k: int) -> str:
        if self.cursor + k >= len(self.text):
            self.cursor = len(self.text)
        else:
            self.cursor += k
        return self.text[max(0, self.cursor - 10):self.cursor]


if __name__ == "__main__":
    textEditor = TextEditor()
    textEditor.addText("leetcode")
    print(textEditor.deleteText(4))
    textEditor.addText("practice")
    print(textEditor.cursorRight(3))
    print(textEditor.cursorLeft(8))
    print(textEditor.deleteText(10))
    print(textEditor.cursorLeft(2))
    print(textEditor.cursorRight(6))