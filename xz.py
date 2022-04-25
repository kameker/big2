import requests


def degree(obj):
    corners = obj['boundedBy']['Envelope']
    left_bottom, right_upper = corners['lowerCorner'].split(), corners['upperCorner'].split()
    return str(abs((float(left_bottom[0]) - float(right_upper[0])) / 2)), \
           str(abs((float(left_bottom[1]) - float(right_upper[1])) / 2))


def show_image(x_coor, y_coor, scale, type_s_p):
    spn = scale
    toponym_longitude, toponym_lattitude = x_coor, y_coor
    map_params = {
        "ll": ",".join([toponym_longitude, toponym_lattitude]),
        "spn": ",".join(spn),
        "l": type_s_p}
    with open('out.jpg', 'wb') as out_file:
        out_file.write(requests.get("http://static-maps.yandex.ru/1.x/", params=map_params).content)