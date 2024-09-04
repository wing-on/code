
class Solution:
    def get_num_words(self, char_matrix, words):
        res = 0
        for word in words:
            length = len(word)
            self.P = False
            for i in range(rows):
                for j in range(cols):
                    if self.P:
                        break
                    cnt = 0
                    self.dfs(i, j, cnt, length, word)
            if self.P:
                res += 1
        return res

    def dfs(self, x, y, cnt, length, word):
        if cnt == length:
            self.P = True
            return
        if x < 0 or x >= rows:
            return
        if y < 0 or y >= cols:
            return
        if visited[x][y]:
            return

        if char_matrix[x][y] == word[cnt] or char_matrix[x][y] == '?':
            cnt += 1
            visited[x][y] = True
            self.dfs(x + 1, y, cnt, length, word)
            self.dfs(x - 1, y, cnt, length, word)
            self.dfs(x, y + 1, cnt, length, word)
            self.dfs(x, y - 1, cnt, length, word)
            visited[x][y] = False

        else:
            return


rows, cols = map(int, input().strip().split())
char_matrix = [list(map(str, input().strip())) for _ in range(rows)]
num = int(input().strip())
words = list(map(str, input().strip().split()))
visited = [[False] * cols for i in range(rows)]
f = Solution()
res = f.get_num_words(char_matrix, words)
print(res)
# 3 4
# ACEI
# EX?I
# SSTJ
# 8
# ACX II STJIIE XE NXE ACA ACECTJ ACETJ

# 5 5
# A?JFL
# J?ASD
# DG?OI
# G??GB
# A?OFC
# 7
# A AA AAA AAAAAAAA ADJAS ADJAJDA LDSFL