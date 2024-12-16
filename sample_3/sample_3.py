import math

'''Check if points are within the triangle of the given coordinates only if it is nondegenerate;
 a triangle where the length of any side is strictly less than the sum of the lengths of the other two sides.

The function points_belong() accepts following parameters:
 1. INTEGER x1
 2. INTEGER y1
 3. INTEGER x2
 4. INTEGER y2
 5. INTEGER x3
 6. INTEGER y3
 7. INTEGER xp
 8. INTEGER yp
 9. INTEGER xq
 10. INTEGER yq

 Return 0 if the triangle is not nondegenerate
 Return 1 if point p is in the triangle but not point q
 Return 2 if point p is not in the triangle but point q is 
 Return 3 if point p and point q is in the triangle
 Return 4 if neither point is in the triangle 
 '''

# Obtain the side length of the triangle
def side_length_helper(x1, y1, x2, y2):
    a = (x2-x1)**2
    b = (y2-y1)**2
    return math.sqrt(a+b)
    
# Check if a given coordinate is within the area of the triangle via overlap
def in_triangle_helper(x1, y1, x2, y2, x3, y3, xp, yp):
    totalArea = triangleArea(x1, y1, x2, y2, x3, y3)
    area1 = triangleArea(x1, y1, x2, y2, xp, yp)
    area2 = triangleArea(x1, y1, x3, y3, xp, yp)
    area3 = triangleArea(x2, y2, x3, y3, xp, yp)
    return area1+ area2 + area3 == totalArea

# Gets the area of the triangle
def triangleArea(x1, y1, x2, y2, x3, y3):
    return abs(0.5*((x1*(y2-y3))+ (x2*(y3-y1)) + (x3*(y1-y2))))
    

def points_Belong(x1, y1, x2, y2, x3, y3, xp, yp, xq, yq):
    ab = side_length_helper(x1, y1, x2, y2)
    bc = side_length_helper(x2, y2, x3, y3)
    ca = side_length_helper(x3, y3, x1, y1)
    
    is_nondegenerate = ab + bc > ca and bc + ca > ab and ab + ca > bc
    
    if not is_nondegenerate:
        return 0
    
    p_in_triangle = in_triangle_helper(x1, y1, x2, y2, x3, y3, xp, yp)
    q_in_triangle = in_triangle_helper(x1, y1, x2, y2, x3, y3, xq, yq)

    if p_in_triangle and not q_in_triangle:
        return 1
    elif q_in_triangle and not p_in_triangle:
        return 2
    elif p_in_triangle and q_in_triangle:
        return 3
    else:
        return 4
    
