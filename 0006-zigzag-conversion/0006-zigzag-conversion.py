class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n = len(s)
        numOfCols = 1000
        zigzag = [[""]*numOfCols for _ in range(numRows)]

        i, j = 0, 0
        k = 0
        while k < n:
            i = 0
            while i < numRows and k < n:
                zigzag[i][j] = s[k]
                i += 1
                k += 1
            j += 1
            if i == numRows:
                i -= 2
                while i > 0 and k < n:
                    zigzag[i][j] = s[k]
                    i -= 1
                    k += 1
                    j += 1
        ans = ""
        for row in zigzag:
            ans += "".join(row)
        return ans
             
