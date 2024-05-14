# survey_questions.py
import pycountry
from typing import Any

countries = ["Select", "Global", "United Kingdom"] + sorted(
    [country.name for country in pycountry.countries]
)

questions: dict[str, Any] = {
    "sector": {
        "tag": "sector",
        "question": "What sector best represents your field of work?",
        "type": "multiple_choice",
        "options": [
            "Select",
            "Aerospace",
            "Architecture",
            "Artificial Intelligence",
            "Automotive",
            "Aviation",
            "Construction",
            "Consumer Goods",
            "Defence",
            "Education",
            "Electronics",
            "Engineering",
            "Environment and Conservation",
            "Finance",
            "Food and Agriculture",
            "Freight",
            "Healthcare",
            "Information technology / Software",
            "International Government",
            "Local Government",
            "Manufacturing",
            "Maritime",
            "Media",
            "Mining",
            "National Government",
            "Energy",
            "Oil and Gas",
            "Place Leadership",
            "Rail",
            "Research",
            "Smart Cities",
            "Supply Chain and Logistics",
            "Technology",
            "Telecommunications",
            "Transport",
            "Utilities",
            "Waste and Recycling",
            "Water",
            "Other",
        ],
        "section": "community_composition",  # Example section
    },
    "location": {
        "tag": "location",
        "question": "Where is your organisation (mainly) located?",
        "type": "multiple_choice",
        "options": countries,
        "section": "community_composition",  # Example section
    },
    "role": {
        "tag": "role",
        "question": "What is your role within your organisation?",
        "type": "multiple_choice",
        "options": [
            "Senior Management (e.g., CEO, CFO, CTO)",
            "Strategic/Business Lead "
            "(e.g., Business Unit Head, Project/Program Manager, "
            "Operations Manager)",
            "Strategic Advisor "
            "(e.g., Compliance Officer, Regulatory Affairs Manager, "
            "Legal Advisor)",
            "In-house Technical Specialist "
            "(e.g., Developer/Engineer, Data Scientist/Analyst, "
            "IT Specialist)",
            "Digital Twin Support Specialist "
            "(e.g., Ontology Developer, Dashboard Developer, "
            "Data Integration Specialist)",
            "Consultant/External Specialist "
            "(e.g., Industry Consultant, External IT Consultant, "
            "Freelance Technical Expert)",
            "Research and Development "
            "(e.g., Researcher/Academic, Innovation Specialist, "
            "Product Development Scientist)",
            "Other (Please specify)",
        ],
        "section": "community_composition",  # Example section
    },
    "primary_responsibilities": {
        "tag": "primary_responsibilities",
        "question": "What are your primary responsibilities?"
        " Please select all that apply.",
        "type": "select_all",
        "options": [
            "Strategic Direction (e.g., setting goals and strategies)",
            "Budget Management (e.g., budget holder or budget influence)",
            "Ensuring Compliance (e.g., uphold standards and regulations)",
            "Project Leadership (e.g., lead project execution)",
            "Technical Decision-Making (e.g., technology selection "
            "and implementation)",
            "Operational Management (e.g., oversee daily operations)",
            "Governance Influence (e.g., guide decision-making and policies)",
            "Research and Innovation (e.g., conduct R&D for innovation)",
            "Other (Please specify):",
        ],
        "section": "community_composition",  # Example section
    },
    "established_dt": {
        "tag": "established_dt",
        "question": "Has your organisation established one"
        " or more digital twins?",
        "type": "radio",
        "options": [
            "Yes",
            "No",
            "Indirectly "
            "(We support clients or provide components"
            " for digital twins)",
        ],
        "section": "community_composition",
    },
    "type_dt": {
        "tag": "type_dt",
        "question": "What type of digital twin(s)?"
        " Please select all that apply.",
        "type": "select_all",
        "options": [
            "System (e.g., IT systems, organizational structure)",
            "Place/Infrastructure Digital Twin "
            "(e.g., cities, transportation networks)"
            "Product (e.g., consumer goods, industrial machines)",
            "Process (e.g., manufacturing processes, workflow optimization)",
            "Physical asset "
            "(e.g. building, manufacturing plant, power station)",
            "Other",
        ],
        "section": "community_composition",
    },
    "purpose_dt": {
        "tag": "primary_purpose_dt",
        "question": "Which of the following best describes the purpose"
        " of the digital twin(s) you have (helped) establish?"
        " Select all that apply",
        "type": "select_all",
        "options": [
            "Internal Operations "
            "(enhancing internal decision-making, process optimization, "
            "and operational efficiency within our organization)",
            "External Collaboration "
            "(facilitating collaboration with business partners "
            "or stakeholders outside the organization)",
            "Public Impact (directly affect the public or consumers)",
            "Market / Customer Engagement "
            "(e.g. enhancing customer experience or market understanding.",
            "Research and Development",
            "Other",
        ],
        "section": "community_composition",
    },
    "type_dt_other": {
        "tag": "type_dt_other",
        "question": "Please specify the type",
        "type": "text_area",
        "section": "community_composition",
    },
    "no_dt_reason": {
        "tag": "no_dt_reason",
        "question": "What is the main reason? Please select all that apply.",
        "type": "select_all",
        "options": [
            "Unclear business case/ROI",
            "Insufficient digital awareness/skills",
            "Lack of goodwill/competence/data assurance"
            "trust in partner organisation",
            "Concerns re confidentiality of data",
            "Intellectual property rights",
            "Regulatory concerns re DP",
            "Info security",
            "Legal agreement barriers",
            "Other",
        ],
        "section": "community_composition",  # Example section
    },
    ###
    # section Current practices & Understanding
    ###
    "assurance_meaning": {
        "tag": "assurance_meaning",
        "question": "What do you understand ‘assurance’ to mean in the context"
        " of your work in the digital twinning sector?",
        "type": "text_area",
        "section": "current_assurance_practices",
    },
    "assurance_mechanisms": {
        "tag": "assurance_mechanisms",
        "question": "Which of the following assurance mechanisms do you"
        " **currently** rely on for your own "
        "(or your client's) digital twin(s)?"
        " Please select all that apply.",
        "type": "select_all",
        "options": [
            "Bias Reviews (e.g., identifying and mitigating biases in "
            "processes or outputs)",
            "Compliance Audits (e.g., verifying adherence to laws and "
            "regulations)",
            "Conformity Assessments (e.g., alignment with standards and"
            " expectations, verification of engineering requirements)",
            "Stakeholder Feedback Systems (e.g. processes and tools to collect"
            " and evaluate feedback from DT users, operators etc.)",
            "Risk Assessment (e.g., evaluating potential risks in projects)",
            "Impact Assessment (e.g., assessing effects on stakeholders and "
            "environments)",
            "Information Security Reviews (e.g., safeguarding data and "
            "systems)",
            "Data Quality Checks (e.g., ensuring accuracy and reliability of"
            " data)",
            "Formal Verification (e.g., rigorously proving system properties)",
            "Post-Implementation Evaluation (e.g., reviewing performance and"
            " outcomes after deployment)",
            "Service Continuity Management (e.g., ensuring ongoing operational"
            " reliability)",
            "Performance Monitoring (e.g., continuous assessment of system"
            " efficiency and effectiveness)",
            "Operational Audits (e.g., reviewing operational processes to"
            " ensure they meet standards and are efficient)",
            "Service Quality Reviews (e.g., assessing and improving the"
            " quality and reliability of ongoing services)",
            "Other (Please specify)",
            "None",
        ],
        "section": "current_assurance_practices",
    },
    "assurance_mechanism_other": {
        "tag": "assurance_mechanism_other",
        "question": "Please specify which other assurance mechanism",
        "type": "text_area",
        "section": "current_assurance_practices",
    },
    "assured_properties": {
        "tag": "assured_properties",
        "question": "Which of the following properties (or goals) do you"
        " currently consider when assuring your (or your client's)"
        " digital twinning technology?"
        " Please select all that apply.",
        "type": "select_all",
        "options": [
            "Accountability",
            "Contestability",
            "Data Quality",
            "Data Stewardship",
            "Ethical Integrity",
            "Evolution",
            "Explainability",
            "Fairness",
            "Federation",
            "Financial Performance",
            "Fit-for-purpose",
            "Governance",
            "Interoperability",
            "Openness",
            "Public Good",
            "Reliability/Robustness",
            "Resilience / Fault-tolerance",
            "Safety",
            "Security",
            "Sustainability",
            "Transparency",
            "Trustworthiness",
            "Value Creation" "None",
            "Other (Please specify)",
        ],
        "section": "current_assurance_practices",
    },
    "assured_properties_other": {
        "tag": "assured_properties_other",
        "question": "Please specify which other property",
        "type": "text_area",
        "section": "current_assurance_practices",
    },
    "asset_data_sharing": {
        "tag": "asset_data_sharing",
        "question": "Have you considered sharing data or models"
        " with other organisations (or across partners within an organisation)"
        " to form **connected digital twins**?",
        "type": "radio",
        "options": ["Yes", "No"],
        "section": "current_assurance_practices",
    },
    "partner_trust_difficulty": {
        "tag": "partner_trust_difficulty",
        "question": "When partnering with other organisations for building"
        " connected digital twins, how difficult is it to establish trust "
        "in the competence, goodwill and value"
        " of the resulting shared digital twin?",
        "type": "likert",
        "options": [
            "Very Easy",
            "Somewhat Easy",
            "Neutral",
            "Somewhat Difficult",
            "Very Difficult",
            "Not Applicable",
        ],
        "section": "current_assurance_practices",
    },
    "partner_trust_challenges": {
        "tag": "partner_trust_challenges",
        "question": "What are/were the major challenges to overcome?"
        " Please select all that apply.",
        "type": "select_all",
        "options": [
            "Unclear business case and issues around fairly distributed "
            "return on investment",
            "Insufficient digital awareness/skills",
            "Lack of trust in partner organisation",
            "Concerns re confidentiality of data",
            "Loss of control of data",
            "Intellectual Property Rights",
            "Regulatory concerns around data protection",
            "Competition",
            "Info security etc",
            "Technical architecture",
            "Interoperability",
            "Lawyer mis-alignment / legal agreement barriers",
            "Business Change",
            "Client Sponsor",
        ],
        "section": "current_assurance_practices",
    },
    "reliance_on_evidence": {
        "tag": "reliance_on_evidence",
        "question": "To what extent did you rely"
        "/are you relying on communication"
        " of assurance mechanisms (such as those selected in **Q2.2**)"
        " to establish trust between the parties of a connected"
        " digital twin ecosystem?",
        "type": "likert",
        "options": [
            "Not at all",
            "Slightly",
            "Moderately",
            "Very much",
            "Completely",
        ],
        "section": "current_assurance_practices",
    },
    ###
    # Section Satisfaction
    ###
    "integrate_assurance": {
        "tag": "integrate_assurance",
        "question": "Our assurance activities extend beyond mere checklist"
        " compliance and are substantively integrated into"
        " our (or our client's) operational "
        "practices.",
        "type": "likert",
        "options": [
            "Strongly disagree",
            "Disagree",
            "Neutral",
            "Agree",
            "Strongly agree",
        ],
        "section": "satisfaction_assurance",
    },
    "communication_impact": {
        "tag": "communication_impact",
        "question": "The way we communicate our assurance activities"
        " significantly contributes to building and maintaining trust "
        "and confidence among our (or our client's) stakeholders.",
        "type": "likert",
        "options": [
            "Strongly disagree",
            "Disagree",
            "Neutral",
            "Agree",
            "Strongly agree",
        ],
        "section": "satisfaction_assurance",
    },
    "link_assurance_activities": {
        "tag": "link_assurance_activities",
        "question": "We can clearly link specific assurance activities"
        " directly to higher-level principles guiding our"
        " (or our client's) system's "
        "trustworthiness and ethical standards.",
        "type": "likert",
        "options": [
            "Strongly disagree",
            "Disagree",
            "Neutral",
            "Agree",
            "Strongly agree",
        ],
        "section": "satisfaction_assurance",
    },
    "lifecycle_assurance": {
        "tag": "lifecycle_assurance",
        "question": "At which stages in the project lifecycle are you"
        " implementing assurance? Please select all that apply.",
        "type": "select_all",
        "options": [
            "Project planning",
            "Problem formulation",
            "Data extraction & procurement",
            "Data analysis",
            "Preprocessing & feature engineering",
            "Model selection & training",
            "Model testing & validation",
            "Model reporting",
            "System implementation",
            "User training",
            "System use & monitoring",
            "Model updating & deprovisioning",
            "Not applicable",
        ],
        "section": "satisfaction_assurance",
    },
    "satisfaction_justification": {
        "tag": "satisfaction_justification",
        "question": "How satisfied are you currently with justification and"
        " documentation around your assurance process?",
        "type": "likert",
        "options": [
            "Very unsatisfied",
            "Somewhat unsatisfied",
            "Neutral",
            "Somewhat satisfied",
            "Very satisfied",
        ],
        "section": "satisfaction_assurance",
    },
    ###
    # Section: High-Level Assurance Goals and Ethical Frameworks
    ###
    "ethical_framework_existence": {
        "tag": "ethical_framework_existence",
        "question": "Does your organisation have an established definition or"
        " framework for 'trustworthy' and 'ethical' digital twins?",
        "type": "radio",
        "options": [
            "Yes  / Something similar",
            "No",
            "I don’t know",
        ],
        "section": "ethical_assurance_frameworks",
    },
    "framework_description": {
        "tag": "framework_description",
        "question": "If your framework is publicly available, please provide a"
        " link; else please describe the definition or framework.",
        "type": "text_area",
        "section": "ethical_assurance_frameworks",
    },
    "framework_development": {
        "tag": "framework_development",
        "question": "How was this definition or framework developed?",
        "type": "multiple_choice",
        "options": [
            "Select",
            "Consensus-based process (e.g., collaborative efforts of industry"
            " consortia)",
            "Internal governance process",
            "Developed by an external consultant",
            "Reused existing framework / standards",
            "Adapted existing framework / standards",
        ],
        "section": "ethical_assurance_frameworks",
    },
    "value_of_guiding_principles": {
        "tag": "value_of_guiding_principles",
        "question": "How valuable do you find high-level guiding principles in"
        " general, e.g., the Gemini principles, OECD AI principles, "
        "or ethical principles like SAFE-D or "
        "any other guiding principles for your work?",
        "type": "likert",
        "options": [
            "Not valuable at all",
            "Slightly valuable",
            "Moderately valuable",
            "Very valuable",
            "Extremely valuable",
        ],
        "section": "ethical_assurance_frameworks",
    },
    "familiarity_with_gemini_principles": {
        "tag": "familiarity_with_gemini_principles",
        "question": "How familiar are you with the Gemini principles?",
        "type": "multiple_choice",
        "options": [
            "Select",
            "This is the first time I've heard of them.",
            "I've heard of them but don't know much.",
            "I've seen them but don't use them in my work.",
            "I incorporate them in my work as guidelines.",
            "I have helped develop them.",
        ],
        "section": "ethical_assurance_frameworks",
    },
    "relevance_of_principles": {
        "tag": "relevance_of_principles",
        "question": "Please rate, for each of the following Gemini principles,"
        " the extent to which it focuses on issues that you believe to be"
        " relevant for your work",
        "type": "likert",
        "options": [
            "Not Relevant",
            "Slightly",
            "Moderately",
            "Very",
            "Extremely Relevant",
        ],
        "section": "ethical_assurance_frameworks",
    },
    "challenge_in_application": {
        "tag": "challenge_in_application",
        "question": "Please rate, for each of the following Gemini principles:"
        " How challenging is it to define and/or"
        " to know how to currently address it in practices?",
        "type": "likert",
        "options": [
            "Not at all challenging",
            "Slightly",
            "Moderately",
            "Very",
            "Extremely challenging",
        ],
        "section": "ethical_assurance_frameworks",
    },
    "operationalization_challenges": {
        "tag": "operationalization_challenges",
        "question": "For those rated very challenging or extremely challenging"
        " to operationalize, what are the main challenges you "
        "(or your clients) face?",
        "type": "text_area",
        "section": "ethical_assurance_frameworks",
    },
    ###
    # Section: Argument Based Assurance
    ###
    "communication_methods": {
        "tag": "communication_methods",
        "question": "How do you currently communicate your assurance"
        " strategies to stakeholders, partner organisations or your clients?"
        " Please select all that apply.",
        "type": "select_all",
        "options": [
            "Written Reports following established standards",
            "Non-standardized written Reports",
            "Meetings",
            "Visual Aids",
            "Digital Communications",
            "Interactive Platforms",
            "Not Systematically / ad hoc",
            "Other",
        ],
        "section": "evidence_based_assurance",
    },
    "need_for_visual_tool": {
        "tag": "need_for_visual_tool",
        "question": "Would a tool that helps you structure and"
        " communicate how your assurance measures align "
        "with key ethical goals enhance trust in your digital twin(s)?",
        "type": "radio",
        "options": [
            "Yes",
            "No",
            "I need to know more about this tool to decide",
        ],
        "section": "evidence_based_assurance",
    },
    "benefits_of_visual_tool": {
        "tag": "benefits_of_visual_tool",
        "question": "What do you believe are the main benefits?",
        "type": "text_area",
        "section": "evidence_based_assurance",
    },
    "reasons_against_visual_tool": {
        "tag": "reasons_against_visual_tool",
        "question": "Why not?",
        "type": "text_area",
        "section": "evidence_based_assurance",
    },
    "preparedness_for_argument": {
        "tag": "preparedness_for_argument",
        "question": "How prepared do you feel to develop a structured argument"
        " for how your current assurance activities relate to broader ethical "
        "goals?",
        "type": "likert",
        "options": [
            "Not prepared at all",
            "Somewhat unprepared",
            "Neutral",
            "Somewhat prepared",
            "Very prepared",
        ],
        "section": "evidence_based_assurance",
    },
    "support_for_assurance": {
        "tag": "support_for_assurance",
        "question": "What type of support might help you in creating sound"
        " assurance arguments around ethical principles for your digital"
        " twin project? Please select all that apply.",
        "type": "select_all",
        "options": [
            "Step-by-Step Guidance / Skills Training",
            "Awareness Programs for Assurance",
            "Tools to easily create Assurance Cases",
            "Regulatory Clarity and Compliance Guidance",
            "Value demonstration (e.g. Business case justification)",
            "Community Forums and Collaboration Platforms to share example"
            " assurance arguments / best practices",
            "Other (Please specify)",
        ],
        "section": "evidence_based_assurance",
    },
    "support_for_assurance_other": {
        "tag": "support_for_assurance_other",
        "question": "Please specify which support",
        "type": "text_area",
        "section": "evidence_based_assurance",
    },
    "ranking_support_options": {
        "tag": "ranking_support_options",
        "question": "Please rank the selected options in order of their"
        " potential impact.",
        "type": "ranking",
        "options": [
            "Step-by-Step Guidance / Skills Training",
            "Awareness Programs for Assurance",
            "Tools to easily create Assurance Cases",
            "Regulatory Clarity and Compliance Guidance",
            "Value demonstration",
            "Business case justification",
            "Community Forums and Collaboration Platforms to share example"
            " assurance arguments / best practices",
        ],
        "section": "evidence_based_assurance",
    },
}
