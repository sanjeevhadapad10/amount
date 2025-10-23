
temp_c = float(input("Enter temperature in °C: "))


if temp_c < 20:
    status = "Cold"
elif 20 <= temp_c <= 30:
    status = "Normal"
else:
    status = "hot"
temp_f = (temp_c * 9/5) + 32


print("Temperature:", temp_c, "°C")
print("Status:", status)
print("Temperature in Fahrenheit:", temp_f, "°F")
