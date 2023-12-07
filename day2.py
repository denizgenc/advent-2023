import adventinput

def map_record(game: str) -> list:
    game_str, rest = game.split(": ")
    id_num = int(game_str.split()[-1])
    sets = []
    for set_str in rest.split("; "):
        set_dict = {}
        for ball_pair in set_str.split(", "):
            count, colour = ball_pair.split(" ")
            set_dict[colour] = int(count)
        sets.append(set_dict)
    return {"id": id_num, "sets": sets}

def possible_game(record: list, red: int, green: int, blue: int) -> int:
    for game in record:
        for set_ in game.get("sets"):
            if set_.get("red", 0) > red or set_.get("green", 0) > green or set_.get("blue", 0) > blue:
                break
        else:
            yield game.get("id")
    yield 0

def power_game(record: list) -> int:
    for game in record:
        min_red, min_green, min_blue = (1,1,1)
        for set_ in game.get("sets"):
            min_red   = max(set_.get("red",   1),   min_red)
            min_green = max(set_.get("green", 1), min_green)
            min_blue  = max(set_.get("blue",  1),  min_blue)
        yield min_red * min_green * min_blue

if __name__ == "__main__":
    lines = adventinput.get_data(2)
    record = [map_record(l) for l in lines]
    # print(record)
    red, green, blue = (12, 13, 14)
    print(sum(possible_game(record, red, green, blue)))
    print(sum(power_game(record)))
