''' 
Given 2 words (begin_word and end_word), and a dictionarys word list, return the shortest transformation sequence from bein_word to end_word, such that:
1- Only one letter can be changed at a time
2- Each transformed word must exist in the word list. Note that begin_word is not a transformed word.

Return None if there is no such transformation sequence
All words contain only lowercase alphabetic chars
Assume no duplicates in word list
Assume begin_word and end_word are non empty and different

'''
words = set()
with open('./projects/WordLadder/words.txt', 'r') as f:
  for w in f:
    w = w.strip()
    words.add(w)
    
def get_neighbors(word):
  neighbors = []
  for w in words:
    if len(w) == len(word):
      diff_count = 0
      for i in range(len(w)):
        if w[i] != word[i]:
          diff_count += 1
        if diff_count > 1:
          break
      if diff_count == 1:
        neighbors.append(w)
  return neighbors

def bfs(begin_word, end_word):
  visited = set()
  q = []
  q.append([begin_word])
  
  while len(q) > 0:
    path = q.pop(0)
    v = path[-1]
    
    if v not in visited:
      visited.add(v)
      
      if v == end_word:
        return path
      
      for neighbor in get_neighbors(v):
        path_copy = path + [neighbor]
        q.append(path_copy)
        
# print(get_neighbors('hit'))
print(bfs('hit', 'cog'))