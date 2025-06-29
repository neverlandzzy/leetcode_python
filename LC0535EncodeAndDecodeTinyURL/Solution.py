"""
TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl and it returns a short URL such as http://tinyurl.com/4e9iAk. Design a class to encode a URL and decode a tiny URL.

There is no restriction on how your encode/decode algorithm should work. You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.

Implement the Solution class:

Solution() Initializes the object of the system.
String encode(String longUrl) Returns a tiny URL for the given longUrl.
String decode(String shortUrl) Returns the original long URL for the given shortUrl. It is guaranteed that the given shortUrl was encoded by the same object.
 

Example 1:

Input: url = "https://leetcode.com/problems/design-tinyurl"
Output: "https://leetcode.com/problems/design-tinyurl"

Explanation:
Solution obj = new Solution();
string tiny = obj.encode(url); // returns the encoded tiny url.
string ans = obj.decode(tiny); // returns the original url after decoding it.
 

Constraints:

1 <= url.length <= 10^4
url is guranteed to be a valid URL.
"""

import random

CODE_LENGTH = 6
PREFIX = "http://tinyurl.com/"
ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

class Codec:
    def __init__(self):
        self.code_to_url = {}


    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        code = "".join(random.choices(ALPHABET, k=CODE_LENGTH))
        while code in self.code_to_url:
            code = "".join(random.choices(ALPHABET, k=CODE_LENGTH))
        
        self.code_to_url[code] = longUrl
        return PREFIX + code

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.code_to_url[shortUrl.split("/")[-1]]

if __name__ == "__main__":
    codec = Codec()
    code = codec.encode("https://leetcode.com/problems/design-tinyurl")
    print(code)
    print(codec.decode(code))
