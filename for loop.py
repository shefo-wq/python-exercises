studentgrades = {
    "boba": {
        "math": 90,
        "arabic": 70,
        "english": 88
    }
}

for name, grades in studentgrades.items():
    print(f"{name} grades:")

    for subject, grade in grades.items():
        print(f"{subject}: {grade}")

    total = sum(grades.values())
    average = total / len(grades)

    print(f"Total = {total}")
    print(f"Average = {average:.2f}")