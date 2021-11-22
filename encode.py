from sys import argv


def encode(input_string):
    count, prev, result = 1, "", []
    for character in input_string:
        if character != prev:
            if prev:
                result.append((prev, count))
            count = 1
            prev = character
        else:
            count += 1
    result.append((character, count))
    return result


def decode(code):
    result = ""
    for character, count in code:
        result += character * count
    return result


if __name__ == '__main__':
    print(encode(argv[1]))
