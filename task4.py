# 1.circle with constructor
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def display_radii(self):
        for radius in self.radius:
            print(f"Radius: {radius}")
radii = [10, 501, 22, 37, 100, 999, 87, 351]
circle = Circle(radii)
circle.display_radii()

#2.class private named pi=3.141
class Circle:
    # Private class variable for pi
    __pi = 3.141

    def __init__(self, radius_list):
        self.radius_list = radius_list  # Member variable to store the list of radii

    def display_radii_and_pi(self):
        print(f"Pi value: {Circle.__pi}")
        for radius in self.radius_list:
            print(f"Radius: {radius}")
radii = [10, 501, 22, 37, 100, 999, 87, 351]
circle = Circle(radii)
circle.display_radii_and_pi()

#3.area and perimeter
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.radius ** 2

    def perimeter(self):
        return 2 * self.radius


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

# Given list
dimensions = [10, 501, 22, 37, 100, 999, 87, 351]

# Calculate Circle
circle = Circle(dimensions[0])
print(f"Circle Area: {circle.area()}")
print(f"Circle Perimeter: {circle.perimeter()}")

# Calculate Rectangles
for i in range(1, len(dimensions), 2):
    if i + 1 < len(dimensions):
        rect = Rectangle(dimensions[i], dimensions[i + 1])
        print(f"\nRectangle Area: {rect.area()}, Perimeter: {rect.perimeter()}")

#4.UML into python class and its methods
class TV:
    def __init__(self, brand):
        self.brand = brand
        self.channel = 1
        self.volume = 50
        self.on = False

    def toggle_power(self):
        """Toggle the power of the TV on/off."""
        self.on = not self.on

    def change_channel(self, channel):
        """Set the channel if the TV is on and within range (1-50)."""
        if self.on and 1 <= channel <= 50:
            self.channel = channel

    def adjust_volume(self, amount):
        """Increase or decrease the volume (0-100) if the TV is on."""
        if self.on:
            self.volume = max(0, min(100, self.volume + amount))

    def status(self):
        """Return the current status of the TV."""
        state = "On" if self.on else "Off"
        return f"{self.brand} TV - Channel: {self.channel}, Volume: {self.volume}, State: {state}"


class LedTV(TV):
    def __init__(self, brand, thickness):
        super().__init__(brand)
        self.thickness = thickness

    def details(self):
        """Return details specific to LED TV."""
        return f"{self.brand} LED TV - Thickness: {self.thickness} mm"


class PlasmaTV(TV):
    def __init__(self, brand, thickness):
        super().__init__(brand)
        self.thickness = thickness

    def details(self):
        """Return details specific to Plasma TV."""
        return f"{self.brand} Plasma TV - Thickness: {self.thickness} mm"

led_tv = LedTV("SONY", 20)
led_tv.toggle_power()
led_tv.change_channel(5)
led_tv.adjust_volume(10)
print(led_tv.status())
print(led_tv.details())

plasma_tv = PlasmaTV("LG", 25)
plasma_tv.toggle_power()
plasma_tv.change_channel(51)  
plasma_tv.adjust_volume(-10)
print(plasma_tv.status())
print(plasma_tv.details())