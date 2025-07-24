# AND Example
age = 25
has_license = True

if age >= 18 and has_license:
    print("You can drive a car")
else:
    print("You cannot drive")
# Output: "You can drive a car"

# OR Example
is_weekend = False
is_holiday = True

if is_weekend or is_holiday:
    print("You can sleep late today")
else:
    print("You should wake up early")
# Output: "You can sleep late today"

# NOT Example
is_raining = False

if not is_raining:
    print("You don't need an umbrella")
else:
    print("Take an umbrella")
# Output: "You don't need an umbrella"

# Combined logical operators
temperature = 22
is_sunny = True
is_windy = False

if temperature > 20 and is_sunny and not is_windy:
    print("Perfect weather for a picnic!")
elif temperature > 20 or is_sunny:
    print("Still decent weather")
else:
    print("Better stay inside")
# Output: "Perfect weather for a picnic!"