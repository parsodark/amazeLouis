import numpy as np

magicTapsForCorner = np.array([[1, 0, 3, 1],  # Changes [[1, 0, 0, 0],
                               [0, 0, 0, 0],  #          [0, 0, 0, 0],
                               [3, 0, 1, 3],  #          [0, 0, 0, 0],
                               [1, 0, 3, 1]]) #          [0, 0, 0, 0]]
magicTapsForEdge =   np.array([[0, 0, 1, 3],  # Changes [[0, 1, 0, 0],
                               [0, 0, 0, 0],  #          [0, 0, 0, 0],
                               [0, 0, 3, 1],  #          [0, 0, 0, 0],
                               [0, 0, 1, 3]]) #          [0, 0, 0, 0]]
magicTapsForCenter = np.array([[0, 0, 0, 0],  # Changes [[0, 0, 0, 0],
                               [0, 0, 0, 0],  #          [0, 1, 0, 0],
                               [0, 0, 1, 3],  #          [0, 0, 0, 0],
                               [0, 0, 3, 1]]) #          [0, 0, 0, 0]]

magicTaps = {}
magicTaps[0,0] = magicTapsForCorner
magicTaps[0,1] = magicTapsForEdge
magicTaps[0,2] = np.fliplr(magicTapsForEdge)
magicTaps[0,3] = np.fliplr(magicTapsForCorner)
magicTaps[1,0] = magicTapsForEdge.T
magicTaps[1,1] = magicTapsForCenter
magicTaps[1,2] = np.fliplr(magicTapsForCenter)
magicTaps[1,3] = np.fliplr(magicTapsForEdge.T)
magicTaps[2,0] = np.flipud(magicTapsForEdge.T)
magicTaps[2,1] = np.flipud(magicTapsForCenter)
magicTaps[2,2] = np.fliplr(np.flipud(magicTapsForCenter))
magicTaps[2,3] = np.fliplr(np.flipud(magicTapsForEdge.T))
magicTaps[3,0] = np.flipud(magicTapsForCorner)
magicTaps[3,1] = np.flipud(magicTapsForEdge)
magicTaps[3,2] = np.flipud(np.fliplr(magicTapsForEdge))
magicTaps[3,3] = np.flipud(np.fliplr(magicTapsForCorner))

# Input matrix:
# 0 = up
# 1 = right
# 2 = down
# 3 = left
inputMatrix = np.array([[3, 1, 2, 3],
                        [1, 0, 3, 0],
                        [2, 1, 1, 2],
                        [1, 0, 3, 2]])

solution = np.zeros((4,4), int)
for i in range(4):
    for j in range(4):
        value = inputMatrix[i,j]
        requiredRotations = 4 - value
        solution = solution + requiredRotations * magicTaps[i,j]
solution = solution % 4

print("Prepare to be amazed!")
print(solution)

