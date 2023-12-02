class Solution:
    def matSearch(self, mat, N, M, X):
        # Start from the top-right corner
        i, j = 0, M - 1

        # Iterate until you go out of the matrix
        while i < N and j >= 0:
            # If the current element is equal to X, return 1
            if mat[i][j] == X:
                return 1
            # If the current element is greater than X, move left
            elif mat[i][j] > X:
                j -= 1
            # If the current element is less than X, move down
            else:
                i += 1

        # If the element is not found in the entire matrix, return 0
        return 0
