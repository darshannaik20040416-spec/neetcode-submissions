class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}
        for word in strs:
            count = [0]*26
            for char in word:
                index = ord(char)-ord('a')
                count[index]+=1
            key = tuple(count) #Python lists are mutable and cannot be used as dictionary keys.Tuples are immutable, so a tuple containing the character counts can be used as a dictionary key.
            if key not in group:
                group[key]=[]
            group[key].append(word)
        return list(group.values()) #group.values() returns all the lists stored in the dictionary.list() converts those values into a list.
                        
# group.values() retrieves all the values:

# dict_values([
#     ["eat", "tea", "ate"],
#     ["tan", "nat"],
#     ["bat"]
# ])

# list(group.values()) converts those values into a list:

# [
#     ["eat", "tea", "ate"],
#     ["tan", "nat"],
#     ["bat"]
# ]
