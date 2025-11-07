import math

def cos_sim(v1, v2):

    dot_product = sum(x * y for x, y in zip(v1, v2))
    
    magnitude_v1 = math.sqrt(sum(x**2 for x in v1))
    magnitude_v2 = math.sqrt(sum(y**2 for y in v2))
    
    if magnitude_v1 == 0 or magnitude_v2 == 0:
        return 0.0
    
    return dot_product / (magnitude_v1 * magnitude_v2)

if __name__ == '__main__':
    cs = cos_sim([1, 0], [5, 5])
    print(cs)
    cs = cos_sim([14, 0, 5], [5, 8, 4])
    print(cs)