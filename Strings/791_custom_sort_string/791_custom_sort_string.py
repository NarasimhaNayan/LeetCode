class Solution:
    def customSortString(self, order: str, s: str) -> str:
        hashmap = {}
        res = ""
        for i in range(len(s)) :
            if s[i] not in hashmap :
                hashmap[s[i]] = 1
            else :
                hashmap[s[i]] += 1
        
        for i in range(len(order)) :
            if order[i] in hashmap:
                # while hashmap[order[i]] > 0 :
                #     res+= order[i]
                #     hashmap[order[i]]-=1
                # if hashmap[order[i]] == 0:
                #     del hashmap[order[i]]

                res+= order[i] * hashmap[order[i]]
                del hashmap[order[i]]
        
        for key,count in hashmap.items() :
            # while count > 0:
            #     res += key
            #     count-=1
            res += key *count
        return res       