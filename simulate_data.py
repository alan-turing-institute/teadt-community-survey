import random
from faker import Faker

# Initialize Faker
fake = Faker()


def create_connection(db_file):
    # TODO: Mock implementation. Fix later
    pass


def create_table(conn):
    # TODO: Mock implementation. Fix later
    pass


def insert_survey_result(conn, database, mock_data):
    # TODO: Mock implementation. Fix later
    pass


# Function to generate a random list of items from a given list
def random_list(choices):
    return random.sample(choices, random.randint(1, len(choices)))


# Function to generate mock data for one survey entry
def generate_mock_data():
    # Define possible choices for each field based on your survey questions
    sectors = [
        "Aerospace",
        "Architecture",
        "Artificial Intelligence",
        "Automotive",
        "Aviation",
    ]
    roles = [
        "Developer/Engineer",
        "Project/Program Manager",
        "Executive/Decision-Maker",
    ]
    responsibilities = [
        "Designing and Implementing",
        "Strategizing and Directing",
        "Ensuring Compliance",
    ]
    assurance_methods = [
        "Risk Assessment",
        "Impact Assessment",
        "Bias Audit",
        "Compliance Audit",
    ]
    properties_assured = [
        "Accuracy",
        "Fairness",
        "Privacy",
        "Robustness",
        "Transparency",
    ]
    ethics_framework_options = ["Yes", "No", "Don't know"]
    support_types = [
        "Examples of effective practices",
        "Toolkit of methods and tools",
        "Guidance on selecting practices",
    ]

    # Generate random data for each field
    data = {
        "sector": random.choice(sectors),
        "location": fake.country(),
        "role": random.choice(roles),
        "responsibilities": ", ".join(random_list(responsibilities)),
        "assurance_meaning": fake.sentence(),
        "governance_requirements": fake.sentence(),
        "assurance_methods": ", ".join(random_list(assurance_methods)),
        "properties_assured": ", ".join(random_list(properties_assured)),
        "assurance_execution": random.choice(["Internal", "Third-party"]),
        "existing_resources": fake.sentence(),
        "ethics_framework": random.choice(ethics_framework_options),
        "ethics_definition": (
            fake.sentence() if random.choice([True, False]) else None
        ),
        "framework_development": (
            fake.sentence() if random.choice([True, False]) else None
        ),
        "biggest_challenges": fake.sentence(),
        "type_of_support": ", ".join(random_list(support_types)),
        "sorted_support_types": ", ".join(random_list(support_types)),
        "ethical_issues": fake.sentence(),
        "value_ethical_principles": random.randint(1, 5),
        "importance_gemini_principles": random.randint(1, 5),
        "difficulty_operationalizing": random.randint(1, 5),
        "satisfaction_integration": random.randint(1, 5),
        "additional_insights": fake.sentence(),
        "workshop_interest": random.choice([True, False]),
        "email": fake.email() if random.choice([True, False]) else None,
    }

    return data


# Main function to create the mock database and populate it with random data
def create_mock_database(db_file, entries=100):
    conn = create_connection(db_file)
    if conn:
        create_table(conn)

        for _ in range(entries):
            mock_data = generate_mock_data()
            insert_survey_result(conn, "assurance_survey", mock_data)

        print(f"Inserted {entries} mock entries into {db_file}")
        conn.close()
    else:
        print("Failed to create database connection.")


# Specify the name of your mock database file and the number of mock entries
# you want
mock_db_file = "mock_survey_results.db"
mock_entries = 100  # Change this number based on how many mock entries you want

# Create the mock database
create_mock_database(mock_db_file, mock_entries)
