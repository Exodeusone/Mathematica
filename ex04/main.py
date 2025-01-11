INITIAL_MAP = [
    ["S", "N", "S"],
    ["B", "R", "B"],
    ["S", "N", "S"],
    ]





def generate_empty_line(size: int) -> list[str]:
    return [" " for _ in range(size)]


def generate_new_line(size: int, previous_line: list[str]) -> list[str]:
    print(previous_line)
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


def fill_map(new_map: list[list[str]]) -> list[list[str]]:
    for i in range(len(new_map)):
        for j in range(len(new_map[i])):
            if new_map[i][j] == '':
                if new_map[i - 1][j] == '':
    return new_map

def stretch_map(previous_map: list[list[str]]) -> list[list[str]]:
    x_size = len(previous_map[0])
    y_size = len(previous_map)
    new_content = (2 * x_size - 1) * (2 * y_size - 1)
    new_size = int(new_content ** 0.5)
    new_map = [generate_new_line(new_size, previous_map[0])]
    for i in range(0, y_size):
        if i % 2 == 0:
            new_map.append(generate_empty_line(new_size))
        else:
            new_map.append(generate_new_line(new_size, previous_map[i]))
    new_map.append(generate_new_line(new_size, previous_map[-1]))
    filled_map = fill_map(new_map)
    return filled_map


if __name__ == "__main__":
    mosaic = INITIAL_MAP
    mosaic = stretch_map(mosaic)
    # mosaic = stretch_map(mosaic)