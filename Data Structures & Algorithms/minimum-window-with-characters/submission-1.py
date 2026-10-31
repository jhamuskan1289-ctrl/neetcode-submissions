class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n1 , n2 = len(s) , len(t)

        if n2 > n1 :

            return ""

        countT , window = {} , {}

        for c in t:
            countT[c] = 1 + countT.get(c , 0)


        have = 0

        need = len(countT)

        res = [-1,-1]
        reslen = float("inf")

        l = 0

        for r in range(len(s)):

            c = s[r]

            window[c] = 1 + window.get(c,0)

            if c in countT and window[c] == countT[c]:
                have +=1

            while have == need:

                if (r-l+1) < reslen:
                    res = [l,r]
                    reslen = r-l+1

                leftchar = s[l]

                window[leftchar] -= 1

                if leftchar in countT and window[leftchar] < countT[leftchar]:
                    have -= 1

                l += 1

        if reslen == float("inf"):

            return ""

        return s[res[0]:res[1] + 1]

        

            









       

                

























        


        









        









        






            
            





















             







            



        





