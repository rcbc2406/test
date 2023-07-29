# Dot product of two vectors
def dot_product(vector1, vector2):
    result = 0
    for i in range(len(vector1)):
        result += vector1[i] * vector2[i]
    return result


# Cross product of two vectors
def cross_product(vector1, vector2):
    result = [0, 0, 0]
    result[0] = vector1[1] * vector2[2] - vector1[2] * vector2[1]
    result[1] = vector1[2] * vector2[0] - vector1[0] * vector2[2]
    result[2] = vector1[0] * vector2[1] - vector1[1] * vector2[0]
    return result


# Examples
vector1 = [1, 2, 3]
vector2 = [4, 5, 6]

dot_prod = dot_product(vector1, vector2)
cross_prod = cross_product(vector1, vector2)

print("Dot product:", dot_prod)
print("Cross product:", cross_prod)