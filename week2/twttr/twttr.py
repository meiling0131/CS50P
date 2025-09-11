text =input("Input: ").strip()
result = "".join(ch for ch in text if ch not in "aeiouAEIOU")
print(f"output: {result}")
