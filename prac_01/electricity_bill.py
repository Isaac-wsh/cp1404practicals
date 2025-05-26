# print("Electricity bill estimator")
# cent_per_kwh = int(input("Enter cents per kWh: "))
# daily_use = float(input("Enter daily use in kWh: "))
# day = int(input("Enter daily use in kWh: "))
# total = float(cent_per_kwh) * 0.01 * daily_use * float(day)
# print(f"Estimated bill: ${total:.2f}")

print("Electricity bill estimator 2.0")
tariff = input("Which tariff? TARIFF_11 or TARIFF_31: ")
if tariff == "TARIFF_11":
    cent_per_kwh = 0.244618
else:
    cent_per_kwh = 0.136928
daily_use = float(input("Enter daily use in kWh: "))
day = int(input("Enter daily use in kWh: "))
total = cent_per_kwh * daily_use * float(day)
print(f"Estimated bill: ${total:.2f}")