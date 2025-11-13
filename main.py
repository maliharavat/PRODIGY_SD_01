# PRODIGY_SD_01 - Temperature Conversion Program

def c_to_f(c): return (c * 9/5) + 32
def c_to_k(c): return c + 273.15
def f_to_c(f): return (f - 32) * 5/9
def k_to_c(k): return k - 273.15

def convert(value, unit):
    unit = unit.upper()
    if unit == "C":
        return {"F": c_to_f(value), "K": c_to_k(value)}
    elif unit == "F":
        c = f_to_c(value)
        return {"C": c, "K": c_to_k(c)}
    elif unit == "K":
        c = k_to_c(value)
        return {"C": c, "F": c_to_f(c)}
    else:
        raise ValueError("Invalid unit! Use C, F, or K.")

if __name__ == "__main__":
    try:
        t = float(input("Enter temperature value: "))
        u = input("Enter unit (C/F/K): ")
        result = convert(t, u)
        print("Converted values:")
        for k, v in result.items():
            print(f"{v:.2f}°{k}")
    except Exception as e:
        print("Error:", e)