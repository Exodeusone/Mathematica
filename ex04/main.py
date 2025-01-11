import tkinter as tk

INITIAL_MAP = [
    ["S", "S", "S"],
    ["S", "S", "S"],
    ["S", "S", "S"],
    ]

FILLED_MAPPING = {
    "RR": "N",
    "RN": "B",
    "RB": "S",
    "RS": "N",
    "NN": "B",
    "NB": "S",
    "NS": "R",
    "BB": "S",
    "BS": "N",
    "SS": "N"
    }

FILLED_VALUES = {
    "R": 0,
    "N": 1,
    "B": 2,
    "S": 3
    }

VALUES_TO_COLOR = {
    0: "R",
    1: "N",
    2: "B",
    3: "S"
    }

COLOR_TO_RENDER = {
    "R": "#ff0000",  # Rouge en hexadécimal
    "N": "#000000",  # Noir en hexadécimal
    "B": "#0000ff",  # Bleu en hexadécimal
    "S": "#ffffff"   # Blanc en hexadécimal
}


def generate_empty_line(size: int) -> list[str]:
    return ["" for _ in range(size)]


def generate_new_line(size: int, previous_line: list[str]) -> list[str]:
    current_previous_line_offset = 0
    new_line = []
    for i in range(1, size):
        if i % 2 == 0:
            new_line.append('')
        else:
            new_line.append(previous_line[current_previous_line_offset])
            current_previous_line_offset += 1
    new_line.append(previous_line[-1])
    return new_line


def get_cardinal_color(value_a: str, value_b: str):
    if not value_a or not value_b:
        return ''
    else:
        for obj in FILLED_MAPPING.keys():
            if value_a in obj and value_b in obj:
                return FILLED_MAPPING[obj]
    return ''


def fill_map(new_map: list[list[str]]) -> list[list[str]]:
    for i in range(len(new_map)):
        for j in range(len(new_map[i])):
            if new_map[i][j] == '':
                j_left = j - 1
                j_right = j + 1
                color = ''
                color = get_cardinal_color(new_map[i][j_left] if j_left >= 0 else '', new_map[i][j_right] if j_right < len(new_map[i]) else '')
                if color == '':
                    i_up = i - 1
                    i_down = i + 1
                    if i_up >= 0 and i_down < len(new_map):
                        color = get_cardinal_color(new_map[i_up][j], new_map[i_down][j])
                new_map[i][j] = color
    return new_map


def fill_map_with_angle(new_map: list[list[str]]) -> list[list[str]]:
    for i in range(len(new_map)):
        for j in range(len(new_map[i])):
            if new_map[i][j] == '':
                total = FILLED_VALUES[new_map[i - 1][j -1]] + FILLED_VALUES[new_map[i + 1][j + 1]] + FILLED_VALUES[new_map[i + 1][j - 1]] + FILLED_VALUES[new_map[i - 1][j + 1]]
                color = VALUES_TO_COLOR[total % 4]
                new_map[i][j] = color
    return new_map


def stretch_map(previous_map: list[list[str]]) -> list[list[str]]:
    x_size = len(previous_map[0])
    y_size = len(previous_map)
    new_content = (2 * x_size - 1) * (2 * y_size - 1)
    new_size = int(new_content ** 0.5)
    new_map = []

    current_previous_line_offset = 0
    for i in range(0, new_size):
        if i % 2 == 0:
            line = generate_new_line(new_size, previous_map[current_previous_line_offset])
            new_map.append(line)
            current_previous_line_offset += 1
        else:
            line = generate_empty_line(new_size)
            new_map.append(generate_empty_line(new_size))
    filled_map = fill_map(new_map)
    filled_map = fill_map_with_angle(filled_map)
    return filled_map


def create_mosaic(data):
    root = tk.Tk()
    root.title("Mosaïque de Carrés de 3 Pixels")

    pixel_size = 2

    canvas_width = len(data[0]) * pixel_size
    canvas_height = len(data) * pixel_size
    canvas = tk.Canvas(root, width=canvas_width, height=canvas_height)
    canvas.pack()

    for i, row in enumerate(data):
        for j, color in enumerate(row):
            x1 = j * pixel_size
            y1 = i * pixel_size
            x2 = x1 + pixel_size
            y2 = y1 + pixel_size
            color_key = data[i][j]  # Assurez-vous que data[i][j] est "R", "N", "B", ou "S"
            color = COLOR_TO_RENDER[color_key]
            canvas.create_rectangle(x1, y1, x2, y2, outline='', fill=color)

    root.mainloop()


if __name__ == "__main__":
    mosaic = INITIAL_MAP
    i = 0

    while True:
        mosaic = stretch_map(mosaic)
        if len(mosaic) == 257:
            break
    create_mosaic(mosaic)

    # while True:
    #     i += 1
    #     if len(mosaic) == 257:
    #         break
