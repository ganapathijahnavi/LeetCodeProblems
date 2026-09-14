class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        x1, y1 = rec1[0], rec1[1]
        x2, y2 = rec1[2], rec1[3]
        X1, Y1 = rec2[0], rec2[1]
        X2, Y2 = rec2[2], rec2[3]
        return x1 < X2 and X1 < x2 and y1 < Y2 and Y1 < y2
                