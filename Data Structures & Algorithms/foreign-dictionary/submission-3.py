class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj={w: set() for word in words for w in word}
        indegree={ch:0 for ch in adj }

        for i in range (len(words)-1):
            w1=words[i]
            w2=words[i+1]

            minlen=min(len(w1),len(w2))
            if len(w1)>len(w2) and w1[:minlen]==w2[:minlen]:
                return ""
            for j in range (minlen):
                if w1[j]!=w2[j]:
                    if w2[j] not in adj[w1[j]]:
                        adj[w1[j]].add(w2[j])
                        indegree[w2[j]]+=1
                    break
        q=deque([c for c in indegree if indegree[c]==0])
        res=[]
        while q:
            ch=q.popleft()
            res.append(ch)
            for neigh in adj[ch]:
                indegree[neigh] -=1
                if indegree[neigh]==0:
                    q.append(neigh)
        if len(res) != len(indegree):
            return ""
        else:
            return "".join(res)
