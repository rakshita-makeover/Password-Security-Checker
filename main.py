
print(r"""
██████╗  █████╗ ███████╗███████╗
██╔══██╗██╔══██╗██╔════╝██╔════╝
██████╔╝███████║███████╗███████╗
██╔═══╝ ██╔══██║╚════██║╚════██║
██║     ██║  ██║███████║███████║
╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝

  PASSWORD SECURITY CHECKER
          VERSION 1.0
""")

print("=" * 40)

password = input("Enter a TEST password: ")

score = 0

if len(password) >= 8:
    score += 1

if any(c.isupper() for c in password):
    score += 1

if any(c.islower() for c in password):
    score += 1

if any(c.isdigit() for c in password):
    score += 1

if any(not c.isalnum() for c in password):
    score += 1

print("\n--- SECURITY REPORT ---")
print("Length:", len(password), "characters")
print("Score:", score, "/ 5")

if score <= 2:
    print("Rating: WEAK")
elif score <= 4:
    print("Rating: MODERATE")
else:
    print("Rating: STRONG")

print("=" * 40)
print("PSC v1.0 | Stay secure!")
