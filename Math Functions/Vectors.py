import math


def find_vector(magnitude, angle, quadrant):
    """Find the vector in a 2D system by using the given parameters

    Args:
        magnitude (_type_): the given vector's magnitude
        angle (_type_): the given vector's direction angle (the angle between the vector and the positive x axis'
    """

    adjecent = round((math.cos(math.radians(angle)) * magnitude), 2)
    if quadrant != 1 and quadrant != 4:
        adjecent = -abs(adjecent)
    opposite = round((math.sin(math.radians(angle)) * magnitude), 2)
    if quadrant != 1 and quadrant != 2:
        opposite = -abs(opposite)

    return [adjecent, opposite]


def add_two_vectors(m_1, a_1, q_1, m_2, a_2, q_2):
    """Find the new_magnitude and new angle of the new vector added up by the given two vectors

    Args:
        m_1 (_type_): the magnitude of the first given vector
        a_1 (_type_): the angle of the first given vector
        q_1 (_type_): the quadrant of the first given vector
        m_2 (_type_): the magnitude of the second given vector
        a_2 (_type_): the angle of the second given vector
        q_2 (_type_): the quadrant of the second given vector

    Returns:
        _type_: return the result
    """

    v = find_vector(m_1, a_1, q_1)
    w = find_vector(m_2, a_2, q_2)
    print(v, w)
    [a, b] = [(v[0]+w[0]), (v[1]+w[1])]
    new_angle = math.degrees(math.atan(b/a))
    new_magnitude = math.sqrt(a**2 + b**2)
    print([a, b])
    print(new_angle)
    if a > 0 and b > 0:
        # quadrant = 1
        return print(
            f"The new vector's magnitude is {new_magnitude}, and its angle is {new_angle}")

    elif a < 0 and b > 0:
        # quadrant = 2
        return print(
            f"The new vector's magnitude is {new_magnitude}, and its angle is {180 - new_angle}")
    elif a < 0 and b < 0:
        # quadrant = 3
        return print(
            f"The new vector's magnitude is {new_magnitude}, and its angle is {180 +new_angle}")
    else:
        # quadrant = 4
        return print(
            f"The new vector's magnitude is {new_magnitude}, and its angle is {360 - new_angle}")


def law_cosine(m_1, m_2, angle):

    result = math.sqrt(m_1**2 + m_2**2 - 2 * m_1 * m_2 *
                       math.cos(math.radians(angle)))
    return result
