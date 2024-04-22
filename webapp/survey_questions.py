# survey_questions.py
import pycountry
questions = {
    "sector": {
        "tag": "sector",
        "question": "What sector best represents your field of work?",
        "type": "multiple_choice",
        "options": [
            "Select","Aerospace", "Architecture", "Artificial Intelligence", "Automotive",
            "Aviation", "Construction", "Consumer Goods", "Defence", "Education",
            "Electronics", "Engineering", "Environment and Conservation", "Finance",
            "Food and Agriculture", "Freight", "Healthcare", "International Government",
            "Local Government", "Manufacturing", "Maritime", "Media", "Mining",
            "National Government", "Nuclear Energy", "Oil and Gas", "Place Leadership",
            "Rail", "Renewable Energy", "Smart Cities", "Supply Chain and Logistics",
            "Technology", "Telecommunications", "Transport", "Utilities",
            "Waste and Recycling", "Water"
        ],
        "section": "community_composition"  # Example section
    },
    "location": {
        "tag": "location",
        "question": "Where is your organisation located?",
        "type": "multiple_choice",
        "options": [country.name for country in pycountry.countries],
        "section": "community_composition"  # Example section
    },
    "role": {
        "tag": "role",
        "question": "What is your role within your organisation?",
        "type": "multiple_choice",
        "options": [
            "Select","Developer/Engineer", "Project/Program Manager", "Executive/Decision-Maker",
            "Researcher/Academic", "Compliance Officer/Regulatory Affairs Manager",
            "Technical Manager/Lead Developer", "Industry Consultant/Advisor",
            "Ontology Engineer/Framework Architect", "Data Scientist/Analyst",
            "Middleware/API Developer", "Governance Specialist", "Semantic Web Technologist",
            "Platform Developer", "Other"
        ],
        "section": "community_composition"  # Example section
    },
    "primary_responsibilities": {
        "tag": "primary_responsibilities",
        "question": "What are your primary responsibilities?",
        "type": "select_all",
        "options": [
            "Designing and Implementing", "Strategizing and Directing",
            "Ensuring Compliance", "Advising and Consulting",
            "Developing Tools and Frameworks", "Other"
        ],
        "section": "community_composition"  # Example section
    },
    # Add more questions as needed...
}
