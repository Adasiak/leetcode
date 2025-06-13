from collections import defaultdict
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not wordList or endWord not in wordList or endWord == beginWord:
            return 0
        
        if endWord not in wordList:
            return 0
        L = len(beginWord)

        # 1) budujemy maski
        masks = defaultdict(list)
        for w in wordList:
            for i in range(L):
                masks[w[:i] + '*' + w[i+1:]].append(w)

        # 2) bi-BFS
        frontA, frontB = {beginWord}, {endWord}
        visited = set(frontA) | set(frontB)
        depth = 1

        while frontA and frontB:
            if len(frontA) > len(frontB):      # zawsze mniejszy front
                frontA, frontB = frontB, frontA

            next_front = set()
            for word in frontA:
                for i in range(L):
                    mask = word[:i] + '*' + word[i+1:]
                    for nei in masks[mask]:
                        if nei in frontB:
                            return depth + 1   # spotkanie!
                        if nei not in visited:
                            visited.add(nei)
                            next_front.add(nei)

            frontA = next_front
            depth += 1

        return 0
