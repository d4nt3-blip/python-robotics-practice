def meters_to_millimeters(meters):
    return meters * 1000


def millimeters_to_meters(millimeters):
    return millimeters / 1000


if __name__ == "__main__":
    distance = float(input("Enter distance in meters: "))
    print(f"{distance} m = {meters_to_millimeters(distance)} mm")

    distance_mm = float(input("Enter distance in millimeters: "))
    print(f"{distance_mm} mm = {millimeters_to_meters(distance_mm)} m")