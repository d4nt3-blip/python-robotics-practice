import math

def deg_to_rad(deg):
    return deg * math.pi / 180

def rad_to_deg(rad):
    return rad * 180 / math.pi

if __name__ == "__main__":
    angle = float(input("Joint angle in degrees: "))
    print(f"{angle} deg = {deg_to_rad(angle):.4f} rad")
