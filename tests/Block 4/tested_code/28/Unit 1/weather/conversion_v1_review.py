





tempature_fahrenheit = int(input("What is the tempature today (in °F)? "))


if tempature_fahrenheit > 90:
    print("Wow that's hot.")


tempature_celsius = (tempature_fahrenheit - 32) * (5/9)
if tempature_celsius.is_integer():
    print(f"That's {tempature_celsius:.0f} °C.")
else:
    print(f"That's {tempature_celsius:.2f} °C.")
