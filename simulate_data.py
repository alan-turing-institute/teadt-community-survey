import sqlite3
from sqlite3 import Error
import random

def create_connection(db_file):
    """Create a database connection to a SQLite database."""
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

def create_table(conn):
    """Create the table in the SQLite database."""
    try:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS assurance_survey (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                sector TEXT,
                location TEXT,
                role TEXT,
                responsibilities TEXT,
                assurance_meaning TEXT,
                governance_requirements TEXT,
                assurance_methods TEXT,
                assurance_execution TEXT,
                existing_resources TEXT,
                ethics_framework TEXT,
                ethics_definition TEXT,
                framework_development TEXT,
                biggest_challenges TEXT,
                type_of_support TEXT,
                sorted_support_types TEXT,
                ethical_issues TEXT,
                value_ethical_principles INTEGER,
                importance_gemini_principles INTEGER,
                difficulty_operationalizing INTEGER,
                satisfaction_integration INTEGER,
                risk_assessment_accuracy BOOLEAN,
                risk_assessment_fairness BOOLEAN,
                risk_assessment_privacy BOOLEAN,
                risk_assessment_robustness BOOLEAN,
                risk_assessment_transparency BOOLEAN,
                risk_assessment_other BOOLEAN,
                impact_assessment_accuracy BOOLEAN,
                impact_assessment_fairness BOOLEAN,
                impact_assessment_privacy BOOLEAN,
                impact_assessment_robustness BOOLEAN,
                impact_assessment_transparency BOOLEAN,
                impact_assessment_other BOOLEAN,
                bias_audit_accuracy BOOLEAN,
                bias_audit_fairness BOOLEAN,
                bias_audit_privacy BOOLEAN,
                bias_audit_robustness BOOLEAN,
                bias_audit_transparency BOOLEAN,
                bias_audit_other BOOLEAN,
                compliance_audit_accuracy BOOLEAN,
                compliance_audit_fairness BOOLEAN,
                compliance_audit_privacy BOOLEAN,
                compliance_audit_robustness BOOLEAN,
                compliance_audit_transparency BOOLEAN,
                compliance_audit_other BOOLEAN,
                conformity_assessment_accuracy BOOLEAN,
                conformity_assessment_fairness BOOLEAN,
                conformity_assessment_privacy BOOLEAN,
                conformity_assessment_robustness BOOLEAN,
                conformity_assessment_transparency BOOLEAN,
                conformity_assessment_other BOOLEAN,
                formal_verification_accuracy BOOLEAN,
                formal_verification_fairness BOOLEAN,
                formal_verification_privacy BOOLEAN,
                formal_verification_robustness BOOLEAN,
                formal_verification_transparency BOOLEAN,
                formal_verification_other BOOLEAN,
                model_cards_accuracy BOOLEAN,
                model_cards_fairness BOOLEAN,
                model_cards_privacy BOOLEAN,
                model_cards_robustness BOOLEAN,
                model_cards_transparency BOOLEAN,
                model_cards_other BOOLEAN,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            );
        """)
        conn.commit()
    except Error as e:
        print(f"Error creating table: {e}")

def insert_simulated_data(conn, num_entries=100):
    """Insert simulated data into the database."""
    cursor = conn.cursor()
    
    # Define your assurance methods and properties as they appear in your form
    assurance_methods = ["Risk Assessment", "Impact Assessment", "Bias Audit", "Compliance Audit", 
                         "Conformity Assessment", "Formal Verification", "Model Cards", "None"]
    project_stages = ["Accuracy", "Fairness", "Privacy", "Robustness", "Transparency", "Other"]

    for _ in range(num_entries):
        # Start with fixed data for columns not related to method-property combinations
        data = [None, "Technology", "United States", "Developer/Engineer", "Designing and Implementing",
                "Understanding assurance in DT", "ISO standards", "Risk Assessment,Impact Assessment",
                "Internal", "Online resources", "Yes", "Trustworthiness definition", "In-house development",
                "Lack of resources", "Guidance,Case studies", "Case studies,Guidance", "Data privacy issues",
                random.randint(1, 5), random.randint(1, 5), random.randint(1, 5), random.randint(1, 5)]

        # Append random boolean values for each method-property combination
        for method in assurance_methods:
            for property in project_stages:
                data.append(random.choice([True, False]))

        # Construct the SQL insert statement
        placeholders = ', '.join(['?'] * len(data))
        sql = f"INSERT INTO assurance_survey VALUES ({placeholders})"

        # Execute the insert operation
        cursor.execute(sql, data)
    
    conn.commit()
    print(f"Inserted {num_entries} simulated entries into the database.")

if __name__ == "__main__":
    db_file = 'survey_results_sim.db'
    conn = create_connection(db_file)

    if conn is not None:
        create_table(conn)
        insert_simulated_data(conn, num_entries=100)  # Adjust num_entries as needed
        conn.close()
    else:
        print("Error! Cannot create the database connection.")

