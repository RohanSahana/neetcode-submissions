from typing import List, Tuple


# def sum_3_integers(triplet: List[int]) -> int:
#     i1, i2, i3 = triplet
#     return i1+i2+i3

def sum_3_integers(triplet: List[int]) -> int:
    sum = 0
    for i in triplet:
        sum += i    
    return sum

# def compute_volume(box_dimensions: Tuple[int, int, int]) -> int:
#     width, height, depth = box_dimensions
#     return width * height * depth

def compute_volume(box_dimensions: Tuple[int, int, int]) -> int:
    product = 1
    for i in box_dimensions:
        product *= i
    return product
  

# do not modify below this line
print(sum_3_integers([1, 2, 3]))
print(sum_3_integers([4, 6, 2]))

print(compute_volume((1, 2, 3)))
print(compute_volume((3, 2, 1)))
print(compute_volume((3, 9, 7)))
