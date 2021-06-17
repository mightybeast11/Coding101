class Solution:
    def findDiagonalOrder(self, nums):
        diagonal = []
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                if i + j < len(diagonal):
                    diagonal[i+j].append(nums[i][j])
                else:
                    diagonal.append([])
                    diagonal[i+j].append(nums[i][j])
        
        result = []                            
        for diag in diagonal:
            result += diag[::-1]
        return result

if __name__ == '__main__':
    sol = Solution()

    # test 1
    t1 = [[1,2,3,4,5,6]]
    print(sol.findDiagonalOrder(t1))
    
    # test 2
    t2 = [[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]
    print(sol.findDiagonalOrder(t2))
