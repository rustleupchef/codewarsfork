import os

def find_trailer(dir_name, search_name):
    for name in os.listdir(dir_name):
        joined = os.path.join(dir_name, name)
        if os.path.isdir(joined):
            if name == search_name:
                trailer_dir = os.path.join(joined, 'trailers')
                if os.path.exists(trailer_dir) and os.path.isdir(trailer_dir):
                    for trailer in os.listdir(trailer_dir):
                        if trailer.endswith(".m2ts"): return trailer_dir + "/" + trailer
                    return ""
                else:
                    return ""
            else:
                res = find_trailer(os.path.join(dir_name, name), search_name)
                if res: return res
    return ""

dir_name = f"files/{input()}/"

while True:
    name = input()
    if name == "END": break
    res = find_trailer(dir_name, name)
    if res:
        print(name, "trailer was found at:", res[len(dir_name):].replace('/', '\\'))
    else:
        print(name, "trailer missing")