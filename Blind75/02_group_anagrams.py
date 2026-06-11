# 49. Group Anagrams (LeetCode #49)

"""
MNEMONIC: "Same letters, same bucket"
- Anagrams are words with identical character frequencies — they just need a common key.
- The trick: find a canonical form that all anagrams share, then group by that key.
- Two natural keys: sorted string OR character frequency tuple.
- Think: "How do I fingerprint a word so all its rearrangements match?"

Pattern: HashMap grouping — whenever you need to cluster items by equivalence, hash them to the same key.
"""

# Problem:
# Given an array of strings, group the anagrams together.
# You can return the answer in any order.
#
# Example:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

from collections import defaultdict


class Solution:
    # Sub-optimal: Sort each string as key — O(n * k log k) time, O(n * k) space
    def groupAnagrams_sort(self, strs):
        groups = defaultdict(list)
        for s in strs:
            key = "".join(sorted(s))
            groups[key].append(s)
        return list(groups.values())

    # Optimal 1: Character count tuple as key — O(n * k) time, O(n * k) space
    # Avoids sorting by using a fixed-size frequency array (26 lowercase letters)
    def groupAnagrams_count(self, strs):
        groups = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            groups[tuple(count)].append(s)
        return list(groups.values())

    # Optimal 2: Prime number product as key — O(n * k) time, O(n * k) space
    # Each letter maps to a unique prime; anagrams produce the same product.
    # Works well for short strings; large strings risk integer overflow in other languages.
    def groupAnagrams_prime(self, strs):
        primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101]
        groups = defaultdict(list)
        for s in strs:
            key = 1
            for c in s:
                key *= primes[ord(c) - ord('a')]
            groups[key].append(s)
        return list(groups.values())


# Demo
sol = Solution()
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print("Sort key:  ", sol.groupAnagrams_sort(strs))
print("Count key: ", sol.groupAnagrams_count(strs))
print("Prime key: ", sol.groupAnagrams_prime(strs))
