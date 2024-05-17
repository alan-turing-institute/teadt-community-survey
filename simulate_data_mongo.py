import random
import string
import csv
import datetime
import pycountry
from webapp.survey_questions import questions


countries = ["Select"] + sorted(
    [country.name for country in pycountry.countries]
)


# Mock database
database = []


# Helper function to generate random email addresses
def generate_email():
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for i in range(10)) + "@example.com"


# Helper function to generate random date
def generate_date():
    start_date = datetime.date(2020, 1, 1)
    end_date = datetime.date(2023, 12, 31)
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    return start_date + datetime.timedelta(days=random_days)


roles = random.choices(
    questions["role"]["options"][1:],
    weights=[1] * len(questions["role"]["options"][1:]),
    k=100,
)

# Define the sectors and their weights
sectors = [
    "Technology",
    "Education",
    "Renewable Energy",
    "Electricity",
    "Construction",
    "Engineering",
    "Water",
    "Buildings",
]
weights = [
    10,  # Technology Sector
    8,  # Education Sector
    6,  # Renewable Energy Sector
    6,  # Electricity Sector
    6,  # Construction Sector
    5,  # Engineering Sector
    4,  # Water Sector
    4,  # Buildings Sector
]

# Sample sectors based on the defined weights
sampled_sectors = random.choices(sectors, weights=weights, k=100)

# Define countries by continent
european_countries = [
    "United Kingdom",
    "Germany",
    "France",
    "Italy",
    "Spain",
    "Netherlands",
    "Switzerland",
    "Sweden",
    "Belgium",
    "Austria",
]
american_countries = [
    "United States",
    "Canada",
    "Brazil",
    "Argentina",
    "Mexico",
    "Colombia",
    "Chile",
    "Peru",
    "Venezuela",
]
asian_australian_countries = [
    "China",
    "India",
    "Japan",
    "Australia",
    "South Korea",
    "Indonesia",
    "Philippines",
    "Vietnam",
    "Thailand",
    "Pakistan",
]

# Sample countries from each continent with specified weights
european_sample = random.choices(european_countries, k=25)
american_sample = random.choices(american_countries, k=5)
asian_australian_sample = random.choices(asian_australian_countries, k=10)

# Combine samples into a single country vector
country_vector = (
    ["United Kingdom"] * 60
    + european_sample
    + american_sample
    + asian_australian_sample
)

# Randomly shuffle the country vector
random.shuffle(country_vector)

# Ensure the country vector has a length of 100
locations = country_vector[:100]


# Populate mock database with weighted sampling and limited distinct responses
for i in range(100):
    record = {
        "_id": i + 1,
        "email": generate_email(),
        "location": locations[i],
        "sector": sampled_sectors[i],
        "role": roles[i],
        "established_dt": random.choice(
            questions["established_dt"]["options"]
        ),
        "type_dt_other": "".join(
            random.choice(string.ascii_letters) for i in range(10)
        ),
        "assurance_meaning": "".join(
            random.choice(string.ascii_letters) for i in range(50)
        ),
        "assurance_mechanisms[0]": random.choice(
            questions["assurance_mechanisms"]["options"]
        ),
        "assurance_mechanisms[1]": random.choice(
            questions["assurance_mechanisms"]["options"]
        ),
        "assurance_mechanism_other": "".join(
            random.choice(string.ascii_letters) for i in range(10)
        ),
        "assured_properties[0]": random.choice(
            questions["assured_properties"]["options"][:-1]
        ),
        "assured_properties[1]": random.choice(
            questions["assured_properties"]["options"][:-1]
        ),
        "assured_properties_other": "".join(
            random.choice(string.ascii_letters) for i in range(10)
        ),
        "asset_data_sharing": random.choice(
            questions["asset_data_sharing"]["options"]
        ),
        "partner_trust_difficulty": random.choice(
            questions["partner_trust_difficulty"]["options"]
        ),
        "partner_trust_challenges[0]": random.choice(
            questions["partner_trust_challenges"]["options"]
        ),
        "preparedness_for_argument": random.choice(
            questions["preparedness_for_argument"]["options"]
        ),
        "communication_impact": random.choice(
            questions["communication_impact"]["options"]
        ),
        "communication_methods[0]": random.choice(
            questions["communication_methods"]["options"]
        ),
        "communication_methods[1]": random.choice(
            questions["communication_methods"]["options"]
        ),
        "integrate_assurance": random.choice(
            questions["integrate_assurance"]["options"]
        ),
        "link_assurance_activities": random.choice(
            questions["link_assurance_activities"]["options"]
        ),
        "satisfaction_justification": random.choice(
            questions["satisfaction_justification"]["options"]
        ),
        "ethical_framework_existence": random.choice(
            questions["ethical_framework_existence"]["options"]
        ),
        "familiarity_with_gemini_principles": random.choice(
            questions["familiarity_with_gemini_principles"]["options"]
        ),
        "value_of_guiding_principles": random.choice(
            questions["value_of_guiding_principles"]["options"]
        ),
        "framework_description": "".join(
            random.choice(string.ascii_letters) for i in range(50)
        ),
        "framework_development": random.choice(
            questions["framework_development"]["options"]
        ),
        "benefits_of_visual_tool": "".join(
            random.choice(string.ascii_letters) for i in range(50)
        ),
        "need_for_visual_tool": random.choice(
            questions["need_for_visual_tool"]["options"]
        ),
        "reasons_against_visual_tool": "".join(
            random.choice(string.ascii_letters) for i in range(50)
        ),
        "operationalization_challenges": "".join(
            random.choice(string.ascii_letters) for i in range(50)
        ),
        "support_for_assurance[0]": random.choice(
            questions["support_for_assurance"]["options"]
        ),
        "support_for_assurance[1]": random.choice(
            questions["support_for_assurance"]["options"]
        ),
        "support_for_assurance_other": "".join(
            random.choice(string.ascii_letters) for i in range(50)
        ),
        "ranking_support_options": random.sample(
            questions["ranking_support_options"]["options"],
            len(questions["ranking_support_options"]["options"]),
        ),
        "modification_date": generate_date(),
        "consent_0": "Yes",
        "consent_1": "Yes",
        "consent_2": "Yes",
        "consent_3": "Yes",
        "consent_4": "Yes",
        "consent_5": "Yes",
        "consent_6": "Yes",
        "consent_7": "Yes",
        "consent_8": "Yes",
        "consent_9": "Yes",
        "project_interest": random.choice(["Yes", "No"]),
        "workshop_interest": random.choice(["Yes", "No"]),
        "challenge_curation": random.sample(
            questions["challenge_in_application"]["options"], 1
        )[0],
        "challenge_evolution": random.sample(
            questions["challenge_in_application"]["options"], 1
        )[0],
        "challenge_federation": random.sample(
            questions["challenge_in_application"]["options"], 1
        )[0],
        "challenge_good": random.sample(
            questions["challenge_in_application"]["options"], 1
        )[0],
        "challenge_insight": random.sample(
            questions["challenge_in_application"]["options"], 1
        )[0],
        "challenge_openness": random.sample(
            questions["challenge_in_application"]["options"], 1
        )[0],
        "challenge_quality": random.sample(
            questions["challenge_in_application"]["options"], 1
        )[0],
        "challenge_security": random.sample(
            questions["challenge_in_application"]["options"], 1
        )[0],
        "challenge_value": random.sample(
            questions["challenge_in_application"]["options"], 1
        )[0],
        "relevance_curation": random.sample(
            questions["relevance_of_principles"]["options"], 1
        )[0],
        "relevance_evolution": random.sample(
            questions["relevance_of_principles"]["options"], 1
        )[0],
        "relevance_federation": random.sample(
            questions["relevance_of_principles"]["options"], 1
        )[0],
        "relevance_good": random.sample(
            questions["relevance_of_principles"]["options"], 1
        )[0],
        "relevance_insight": random.sample(
            questions["relevance_of_principles"]["options"], 1
        )[0],
        "relevance_openness": random.sample(
            questions["relevance_of_principles"]["options"], 1
        )[0],
        "relevance_quality": random.sample(
            questions["relevance_of_principles"]["options"], 1
        )[0],
        "relevance_security": random.sample(
            questions["relevance_of_principles"]["options"], 1
        )[0],
        "relevance_value": random.sample(
            questions["relevance_of_principles"]["options"], 1
        )[0],
    }
    database.append(record)

# Print the first record for verification
print(database[0])

# Adjusted code to save the database to a CSV file
csv_file = "mock_database.csv"

# Define fieldnames based on the keys of the first record
fieldnames = list(database[0].keys())

# Write database to CSV file
with open(csv_file, mode="w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    for record in database:
        writer.writerow(record)

print(f"Database saved to {csv_file}")
