# -----------------------------------------------------------
# Write a function that returns the total surface area and volume of a box as an array: [area, volume]
# -----------------------------------------------------------

def get_size(w, h, d):
    area = (w * h + w * d + h * d) * 2
    volume = w * h * d
    return [area, volume]