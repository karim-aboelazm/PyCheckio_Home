from typing import Union


def sun_angle(time: str) -> Union[int, str]:
    hour = int(time[:2])
    if 6 <= hour <= 18:  # Hour is between dawn and dusk
        minutes = ((hour - 6) * 60) + int(time[3:])

        if minutes > 720:
            return "I don't see the sun!"
        angle = round((0.25 * minutes), 2)
        return angle
    else:
        return "I don't see the sun!"


if __name__ == '__main__':
    print("Example:")
    print(sun_angle("07:00"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")
