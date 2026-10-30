def meters_to_millimeters(meters):
    return meters * 1000

if __name__ == "__main__":
    distance = float(input("Enter distance in meters: "))
    print(f"{distance} m = {meters_to_millimeters(distance)} mm")

