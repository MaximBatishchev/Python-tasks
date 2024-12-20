def number_to_ordinal(num):
    if num < 1 or num > 12:
        return ""

    ordinals = [
        "first", "second", "third", "fourth", "fifth",
        "sixth", "seventh", "eighth", "ninth", "tenth",
        "eleventh", "twelfth"
    ]

    return ordinals[num - 1]


def verse(day):
    gifts = [
        "Twelve drummers drumming",
        "Eleven pipers piping",
        "Ten lords a-leaping",
        "Nine ladies dancing",
        "Eight maids a-milking",
        "Seven swans a-swimming",
        "Six geese a-laying",
        "Five gold rings",
        "Four calling birds",
        "Three French hens",
        "Two turtle doves",
        "A partridge in a pear tree"
    ]

    ordinal = number_to_ordinal(day)
    result = [f"On the {ordinal} day of Christmas\nmy true love sent to me:"]

    for i in range(day, 0, -1):
        if i == 1 and day != 1:
            result.append("And " + gifts[-i])
        else:
            result.append(gifts[-i])

    return "\n".join(result)


def main():
    for day in range(1, 13):
        print(verse(day))
        print()


if __name__ == "__main__":
    main()
