def encode_vector(position):
    ret = ""
    for i in range(0, len(position)):
        ret += str(position[i]) + "x"
    return ret[:-1]

def decode_vector(position):
    position = position.split("x")
    for i in range(0, len(position)):
        position[i] = int(position[i])
    return position

def decode_vector_float(position):
    position = position.split("x")
    for i in range(0, len(position)):
        position[i] = float(position[i])
    return position

def jsonify_vbo_data(vertices, texCoords):
    json = "{\"vertices\":["
    for i in range(0, len(vertices)):
        json += f"{i}"
        if i != len(vertices) - 1:
            json += ","
    json += "], \"texCoords\":["
    for i in range(0, len(texCoords)):
        json += f"{i}"
        if i != len(texCoords) - 1:
            json += ","
    json += "]}"
    return json

def remove_subset(_set, subset):
    for i in range(len(_set)): 
        if _set[i:i+len(subset)] == subset: 
            del _set[i:i+len(subset)] 
            return _set

def get_subset(_set, subset):
    for i in range(len(_set)): 
        if _set[i:i+len(subset)] == subset: 
            return _set[i:i+len(subset)]

def matches(_set, subset):
    for i in range(len(_set)):
        if _set[i] != subset[i]:
            return False
    return True

def get_indexrange(_set, subset):
    for i in range(len(_set)): 
        if matches(_set[i:i+len(subset)], subset): 
            return i, i+len(subset)
    return [0, 0]