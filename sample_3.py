import math


'''Check if points are within the triangle of the given coordinates
The function accepts following parameters:
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
 '''


def side_length(x1, y1, x2, y2):
    a = (x2-x1)**2
    b = (y2-y1)**2
    return math.sqrt(a+b)
    
def in_triangle(x1, y1, x2, y2, x3, y3, xp, yp):
    totalArea = area(x1, y1, x2, y2, x3, y3)
    area1 = area(x1, y1, x2, y2, xp, yp)
    area2 = area(x1, y1, x3, y3, xp, yp)
    area3 = area(x2, y2, x3, y3, xp, yp)
    return area1+ area2 + area3 == totalArea

def area(x1, y1, x2, y2, x3, y3):
    return abs(0.5*((x1*(y2-y3))+ (x2*(y3-y1)) + (x3*(y1-y2))))
    
def pointsBelong(x1, y1, x2, y2, x3, y3, xp, yp, xq, yq):
    # Write your code here
    ab = side_length(x1, y1, x2, y2)
    bc = side_length(x2, y2, x3, y3)
    ca = side_length(x3, y3, x1, y1)
    
    is_nondegenerate = ab + bc > ca and bc + ca > ab and ab + ca > bc
    
    if not is_nondegenerate:
        return 0
    
    p_in_triangle = in_triangle(x1, y1, x2, y2, x3, y3, xp, yp)
    q_in_triangle = in_triangle(x1, y1, x2, y2, x3, y3, xq, yq)

    if p_in_triangle and not q_in_triangle:
        return 1
    elif q_in_triangle and not p_in_triangle:
        return 2
    elif p_in_triangle and q_in_triangle:
        return 3
    else:
        return 4
    
