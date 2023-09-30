import math
import numpy as np

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def distance(start_vertice, end_vertice): 
    x1, y1 = start_vertice
    x2, y2 = end_vertice
    dis = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    return dis

# Tính diện tích hình thoi
def calculate_diamond_area(vertices):
    # Ensure there are exactly 4 vertices provided
    if len(vertices) != 4:
        raise ValueError("A diamond must have exactly 4 vertices.")
    
    # Extract coordinates of the four vertices
    x1, y1 = vertices[0]
    x2, y2 = vertices[1]
    x3, y3 = vertices[2]
    x4, y4 = vertices[3]

    # Calculate the area of the diamond using the formula: (1/2) * d1 * d2
    diagonal1 = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    diagonal2 = ((x4 - x3) ** 2 + (y4 - y3) ** 2) ** 0.5
    area = 0.5 * diagonal1 * diagonal2

    # print(area)
    return area

# Tính góc của đường thẳng tạo bởi 2 điểm 
def angle_of(start_vertice, end_vertice):
    x1, y1 = start_vertice
    x2, y2 = end_vertice
    slope = (y2 - y1) / (x2 - x1)
    
    angle = math.degrees(math.atan(abs(slope)))
    # print(angle, ";", x1, " ", x2, ";", y1, " ", y2)
    return angle

# Xác định sự chênh lệch về góc giữa 3 điểm (để kiểm tra 3 điểm thẳng hàng)
def angle(line_vertices, threshold_degrees):
    # Extract coordinates of the three vertices
    x1, y1 = line_vertices[0]
    x2, y2 = line_vertices[1]
    x3, y3 = line_vertices[2]

    # Calculate the slopes of two line segments
    slope1 = (y2 - y1) / (x2 - x1)
    slope2 = (y3 - y2) / (x3 - x2)

    # Calculate the angles of the two line segments with respect to the vertical axis
    angle1 = math.degrees(math.atan(abs(slope1)))
    angle2 = math.degrees(math.atan(abs(slope2)))

    # Calculate the absolute difference between the angles
    angle_diff = abs(angle1 - angle2)

    # Check if the angle difference is greater than the threshold
    return angle_diff

# Tính tích chéo giữa 2 điểm
def cross_product(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return x1 * y2 - y1 * x2

# Kiểm tra xem điểm q có nằm trên đoạn thẳng qr hay không
def on_segment(p, q, r):
    xp, yp = p
    xq, yq = q
    xr, yr = r
    return min(xp, xr) <= xq <= max(xp, xr) and min(yp, yr) <= yq <= max(yp, yr)

# Xác định hướng thông qua tích chéo
def orientation(p, q, r):
    xp, yp = p
    xq, yq = q
    xr, yr = r
    val = cross_product((xq - xp, yq - yp), (xr - xq, yr - yq))
    if val == 0:
        return 0  # Collinear
    return 1 if val > 0 else 2  # Clockwise or counterclockwise

# Kiểm tra xem AB và CD có giao nhau hay không?
def do_lines_intersect(A, B, C, D):
    # Check orientations of points
    o1 = orientation(A, B, C)
    o2 = orientation(A, B, D)
    o3 = orientation(C, D, A)
    o4 = orientation(C, D, B)

    if o1 != o2 and o3 != o4:
        return True  # Lines intersect

    if o1 == 0 and on_segment(A, C, B):
        return True  # A, B, and C are collinear and C is on AB
    if o2 == 0 and on_segment(A, D, B):
        return True  # A, B, and D are collinear and D is on AB
    if o3 == 0 and on_segment(C, A, D):
        return True  # C, D, and A are collinear and A is on CD
    if o4 == 0 and on_segment(C, B, D):
        return True  # C, D, and B are collinear and B is on CD

    return False  # Lines do not intersect

def almost_collapsed(p1, p2, threshold_value):
    return distance(p1, p2) <= threshold_value

def distance_point_to_line(point, line_start, line_end):
    # Calculate the length of the line segment
    line_length = math.sqrt((line_end[0] - line_start[0]) ** 2 + (line_end[1] - line_start[1]) ** 2)

    # Handle the special case of a zero-length line
    if line_length == 0:
        return math.sqrt((point[0] - line_start[0]) ** 2 + (point[1] - line_start[1]) ** 2)

    # Calculate the vector from the line's start point to the test point
    vector_from_start = (point[0] - line_start[0], point[1] - line_start[1])

    # Calculate the unit vector along the line segment
    unit_vector = ((line_end[0] - line_start[0]) / line_length, (line_end[1] - line_start[1]) / line_length)

    # Calculate the dot product of the two vectors
    dot_product = vector_from_start[0] * unit_vector[0] + vector_from_start[1] * unit_vector[1]

    # Calculate the closest point on the line segment to the test point
    closest_point = (line_start[0] + dot_product * unit_vector[0], line_start[1] + dot_product * unit_vector[1])

    # Calculate the distance from the test point to the closest point on the line segment
    distance = math.sqrt((point[0] - closest_point[0]) ** 2 + (point[1] - closest_point[1]) ** 2)

    return distance

def distance_between_segments(segment1_start, segment1_end, segment2_start, segment2_end):
    # Calculate the distances from the endpoints of segment1 to segment2
    distances = [
        distance_point_to_line(segment1_start, segment2_start, segment2_end),
        distance_point_to_line(segment1_end, segment2_start, segment2_end),
        distance_point_to_line(segment2_start, segment1_start, segment1_end),
        distance_point_to_line(segment2_end, segment1_start, segment1_end)
    ]

    print(min(distances))
    # Return the minimum distance
    return min(distances)