import json
import random
from faker import Faker

# Initialize Faker with Indian locale
fake = Faker('en_IN')

counselors = []
qualifications = [
    "M.Sc. in Counseling Psychology", 
    "M.A. in Clinical Psychology", 
    "PhD in Psychology", 
    "Post Graduate Diploma in Guidance and Counselling"
]

print("Generating data for 2 Counselors...")

for i in range(1, 3):
    # Determine Gender and Names
    gender = random.choice(["Male", "Female"])
    if gender == "Male":
        first_name = fake.first_name_male()
    else:
        first_name = fake.first_name_female()
    
    last_name = fake.last_name()
    full_name = f"{first_name} {last_name}"
    
    # Generate Counselor Data
    counselor = {
        "counselor_id": f"COUN_{2024}_{i:03d}",
        "role": "counselor",  # Identifier for Login logic
        "name": full_name,
        "emailid": f"{first_name.lower()}.{last_name.lower()}@college.edu", # distinct domain for staff
        "password": "password123", # Default password for Login simulation
        "mobileno": f"{random.randint(6,9)}{random.randint(100000000, 999999999)}",
        "gender": gender,
        "address": fake.address().replace("\n", ", "),
        "qualification": random.choice(qualifications),
        "years_of_experience": random.randint(5, 20),
        "specialization": random.choice(["Career Counseling", "Mental Health", "Academic Guidance", "Stress Management"])
    }
    counselors.append(counselor)

# Write to JSON file
file_name = "counselors_data.json"
with open(file_name, "w") as f:
    json.dump(counselors, f, indent=4)

print(f"Successfully created {file_name} with 2 counselor records.")
print("Data structure is compatible with Student login (includes emailid, password, and role).")