# Database management
CONNECTION_STRING_ENV: str = "CONNECTION_STRING"
DATABASE_NAME_ENV: str = "DB_NAME"
COLLECTION_NAME_ENV: str = "COLLECTION_NAME"

# Application management
START_TIMESTAMP_STATE_KEY: str = "start_timestamp"
USER_ID_STATE_KEY: str = "_id"
SURVEY_SUBMITTED_STATE_KEY: str = "survey_submitted"
ERROR_MESSAGES_STATE_KEY: str = "error_messages"
VALID_CAPTCHA_ENTRY_STATE_KEY: str = "controllo"
CAPTCHA_TEXT_STATE_KEY: str = "Captcha"

# Consent Page Keys
CONSENT_QUESTIONS: int = 10
CONSENT_STATE_KEY: str = "consent"
ALL_CONSENT_STATE_KEYS: list[str] = [
    f"{CONSENT_STATE_KEY}_{index}" for index in range(CONSENT_QUESTIONS)
]

# Community Page Keys
SECTOR_STATE_KEY: str = "sector"
LOCATION_STATE_KEY: str = "location"
ROLE_STATE_KEY: str = "role"
RESPONSIBILITIES_STATE_KEY: str = "primary_responsibilities"
ESTABLISHED_DT_STATE_KEY: str = "established_dt"
TYPE_DT_STATE_KEY: str = "type_dt"
TYPE_DT_OTHER_STATE_KEY: str = "type_dt_other"
PURPOSE_DT_STATE_KEY: str = "purpose_dt"
PURPOSE_DT_OTHER_STATE_KEY: str = "purpose_dt_other"
NO_DT_REASON_STATE_KEY: str = "no_dt_reason"

# Current Practices Page Keys
ASSURANCE_MEANING_STATE_KEY: str = "assurance_meaning"
ASSURANCE_MECHANISMS_STATE_KEY: str = "assurance_mechanisms"
ASSURANCE_MECHANISM_OTHER_STATE_KEY: str = "assurance_mechanism_other"
ASSURED_PROPERTIES_STATE_KEY: str = "assured_properties"
ASSURED_PROPERTIES_OTHER_STATE_KEY: str = "assured_properties_other"
ASSURANCE_EXPERIENCE_STATE_KEY: str = "Assurance_experience"
ASSET_DATA_SHARING_STATE_KEY: str = "asset_data_sharing"
PARTNER_TRUST_DIFFICULTY_STATE_KEY: str = "partner_trust_difficulty"
PARTNER_TRUST_CHALLENGES_STATE_KEY: str = "partner_trust_challenges"
RELIANCE_ON_EVIDENCE_STATE_KEY: str = "reliance_on_evidence"

# Satisfaction Page Keys
INTEGRATE_ASSURANCE_STATE_KEY: str = "integrate_assurance"
COMMUNICATION_IMPACT_STATE_KEY: str = "communication_impact"
LINK_ASSURANCE_ACTIVITIES_STATE_KEY: str = "link_assurance_activities"
SATISFACTION_JUSTIFICATION_STATE_KEY: str = "satisfaction_justification"


# Goals Framework Page Keys
ETHICAL_FRAMEWORK_EXISTENCE_STATE_KEY: str = "ethical_framework_existence"
FRAMEWORK_DESCRIPTION_STATE_KEY: str = "framework_description"
FRAMEWORK_DEVELOPMENT_STATE_KEY: str = "framework_development"
VALUE_OF_GUIDING_PRINCIPLES_STATE_KEY: str = "value_of_guiding_principles"
FAMILIARITY_WITH_GEMINI_PRINCIPLES_STATE_KEY: str = (
    "familiarity_with_gemini_principles"
)
RELEVANCE_GOOD_STATE_KEY: str = "relevance_good"
RELEVANCE_VALUE_STATE_KEY: str = "relevance_value"
RELEVANCE_INSIGHT_STATE_KEY: str = "relevance_insight"
RELEVANCE_SECURITY_STATE_KEY: str = "relevance_security"
RELEVANCE_OPENNESS_STATE_KEY: str = "relevance_openness"
RELEVANCE_QUALITY_STATE_KEY: str = "relevance_quality"
RELEVANCE_FEDERATION_STATE_KEY: str = "relevance_federation"
RELEVANCE_CURATION_STATE_KEY: str = "relevance_curation"
RELEVANCE_EVOLUTION_STATE_KEY: str = "relevance_evolution"
CHALLENGE_GOOD_STATE_KEY: str = "challenge_good"
CHALLENGE_VALUE_STATE_KEY: str = "challenge_value"
CHALLENGE_INSIGHT_STATE_KEY: str = "challenge_insight"
CHALLENGE_SECURITY_STATE_KEY: str = "challenge_security"
CHALLENGE_OPENNESS_STATE_KEY: str = "challenge_openness"
CHALLENGE_QUALITY_STATE_KEY: str = "challenge_quality"
CHALLENGE_FEDERATION_STATE_KEY: str = "challenge_federation"
CHALLENGE_CURATION_STATE_KEY: str = "challenge_curation"
CHALLENGE_EVOLUTION_STATE_KEY: str = "challenge_evolution"
OPERATIONALIZATION_CHALLENGES_STATE_KEY: str = "operationalization_challenges"


# Communicating Assurance Page Keys
COMMUNICATION_METHODS_STATE_KEY: str = "communication_methods"
NEED_FOR_VISUAL_TOOL_STATE_KEY: str = "need_for_visual_tool"
BENEFITS_OF_VISUAL_TOOL_STATE_KEY: str = "benefits_of_visual_tool"
REASONS_AGAINST_VISUAL_TOOL_STATE_KEY: str = "reasons_against_visual_tool"
PREPAREDNESS_FOR_ARGUMENT_STATE_KEY: str = "preparedness_for_argument"
CHALLENGES_ADOPTION: str = "challenges_adoption"
SUPPORT_FOR_ASSURANCE_STATE_KEY: str = "support_for_assurance"
SUPPORT_FOR_ASSURANCE_OTHER_STATE_KEY: str = "support_for_assurance_other"

# Follow-up Page Keys
ADDITIONAL_INSIGHTS_STATE_KEY: str = "additional_insights"
WORKSHOP_INTEREST_STATE_KEY: str = "workshop_interest"
PROJECT_INTEREST_STATE_KEY: str = "project_interest"
EMAIL_INTEREST_STATE_KEY: str = "email_interest"
EVENT_INTEREST_STATE_KEY: str = "event_interest"
EMAIL_STATE_KEY: str = "email"

ALL_SESSION_KEYS: list[str] = ALL_CONSENT_STATE_KEYS + [
    START_TIMESTAMP_STATE_KEY,
    USER_ID_STATE_KEY,
    SECTOR_STATE_KEY,
    LOCATION_STATE_KEY,
    ROLE_STATE_KEY,
    RESPONSIBILITIES_STATE_KEY,
    ESTABLISHED_DT_STATE_KEY,
    TYPE_DT_STATE_KEY,
    TYPE_DT_OTHER_STATE_KEY,
    PURPOSE_DT_STATE_KEY,
    PURPOSE_DT_OTHER_STATE_KEY,
    NO_DT_REASON_STATE_KEY,
    ASSURANCE_MEANING_STATE_KEY,
    ASSURANCE_MECHANISMS_STATE_KEY,
    ASSURANCE_MECHANISM_OTHER_STATE_KEY,
    ASSURED_PROPERTIES_STATE_KEY,
    ASSURED_PROPERTIES_OTHER_STATE_KEY,
    ASSURANCE_EXPERIENCE_STATE_KEY,
    ASSET_DATA_SHARING_STATE_KEY,
    PARTNER_TRUST_DIFFICULTY_STATE_KEY,
    PARTNER_TRUST_CHALLENGES_STATE_KEY,
    RELIANCE_ON_EVIDENCE_STATE_KEY,
    INTEGRATE_ASSURANCE_STATE_KEY,
    COMMUNICATION_IMPACT_STATE_KEY,
    LINK_ASSURANCE_ACTIVITIES_STATE_KEY,
    SATISFACTION_JUSTIFICATION_STATE_KEY,
    ETHICAL_FRAMEWORK_EXISTENCE_STATE_KEY,
    FRAMEWORK_DESCRIPTION_STATE_KEY,
    FRAMEWORK_DEVELOPMENT_STATE_KEY,
    VALUE_OF_GUIDING_PRINCIPLES_STATE_KEY,
    FAMILIARITY_WITH_GEMINI_PRINCIPLES_STATE_KEY,
    RELEVANCE_GOOD_STATE_KEY,
    RELEVANCE_VALUE_STATE_KEY,
    RELEVANCE_INSIGHT_STATE_KEY,
    RELEVANCE_SECURITY_STATE_KEY,
    RELEVANCE_OPENNESS_STATE_KEY,
    RELEVANCE_QUALITY_STATE_KEY,
    RELEVANCE_FEDERATION_STATE_KEY,
    RELEVANCE_CURATION_STATE_KEY,
    RELEVANCE_EVOLUTION_STATE_KEY,
    CHALLENGE_GOOD_STATE_KEY,
    CHALLENGE_VALUE_STATE_KEY,
    CHALLENGE_INSIGHT_STATE_KEY,
    CHALLENGE_SECURITY_STATE_KEY,
    CHALLENGE_OPENNESS_STATE_KEY,
    CHALLENGE_QUALITY_STATE_KEY,
    CHALLENGE_FEDERATION_STATE_KEY,
    CHALLENGE_CURATION_STATE_KEY,
    CHALLENGE_EVOLUTION_STATE_KEY,
    OPERATIONALIZATION_CHALLENGES_STATE_KEY,
    COMMUNICATION_METHODS_STATE_KEY,
    NEED_FOR_VISUAL_TOOL_STATE_KEY,
    BENEFITS_OF_VISUAL_TOOL_STATE_KEY,
    REASONS_AGAINST_VISUAL_TOOL_STATE_KEY,
    PREPAREDNESS_FOR_ARGUMENT_STATE_KEY,
    CHALLENGES_ADOPTION,
    SUPPORT_FOR_ASSURANCE_STATE_KEY,
    SUPPORT_FOR_ASSURANCE_OTHER_STATE_KEY,
    ADDITIONAL_INSIGHTS_STATE_KEY,
    WORKSHOP_INTEREST_STATE_KEY,
    PROJECT_INTEREST_STATE_KEY,
    EMAIL_INTEREST_STATE_KEY,
    EVENT_INTEREST_STATE_KEY,
    EMAIL_STATE_KEY,
]

# Page catalogue
HOME_PAGE: str = "home"
CONSENT_PAGE: str = "Consent"
COMMUNITY_PAGE: str = "1 - Community"
COMMUNITY_RESULTS_PAGE: str = "Community_Results"
CURRENT_PRACTICES_PAGE: str = "2 - Current_Practices"
CURRENT_PRACTICES_RESULTS_PAGE: str = "Current_Practices_Results"
SATISFACTION_PAGE: str = "3 - Satisfaction"
GOALS_FRAMEWORK_PAGE: str = "4 - Goals_Frameworks"
GOALS_FRAMEWORK_RESULTS_PAGE: str = "Frameworks_Results"
COMMUNICATING_ASSURANCE_PAGE: str = "5 - Communicating_Assurance"
FOLLOW_UP_PAGE: str = "6 - Follow_up"
SUCCESS_PAGE: str = "Success"

# Required logic
REQUIRED_MESSAGE = (
    "*Fields marked with*"
    " <span style='color:red;'>*</span>"
    " *are required.*"
)

# REQUIRED_QUESTIONS
ALL_REQUIRED_KEYS: list[str] = [
    SECTOR_STATE_KEY,
    LOCATION_STATE_KEY,
    ROLE_STATE_KEY,
    RESPONSIBILITIES_STATE_KEY,
    ESTABLISHED_DT_STATE_KEY,
    TYPE_DT_STATE_KEY,
    TYPE_DT_OTHER_STATE_KEY,
    PURPOSE_DT_STATE_KEY,
    PURPOSE_DT_OTHER_STATE_KEY,
    NO_DT_REASON_STATE_KEY,
    ASSURANCE_MECHANISMS_STATE_KEY,
    ASSURANCE_MECHANISM_OTHER_STATE_KEY,
    ASSURED_PROPERTIES_STATE_KEY,
    ASSURED_PROPERTIES_OTHER_STATE_KEY,
    ASSET_DATA_SHARING_STATE_KEY,
    PARTNER_TRUST_DIFFICULTY_STATE_KEY,
    PARTNER_TRUST_CHALLENGES_STATE_KEY,
    RELIANCE_ON_EVIDENCE_STATE_KEY,
    INTEGRATE_ASSURANCE_STATE_KEY,
    COMMUNICATION_IMPACT_STATE_KEY,
    LINK_ASSURANCE_ACTIVITIES_STATE_KEY,
    SATISFACTION_JUSTIFICATION_STATE_KEY,
    ETHICAL_FRAMEWORK_EXISTENCE_STATE_KEY,
    FRAMEWORK_DESCRIPTION_STATE_KEY,
    FRAMEWORK_DEVELOPMENT_STATE_KEY,
    VALUE_OF_GUIDING_PRINCIPLES_STATE_KEY,
    FAMILIARITY_WITH_GEMINI_PRINCIPLES_STATE_KEY,
    RELEVANCE_GOOD_STATE_KEY,
    RELEVANCE_VALUE_STATE_KEY,
    RELEVANCE_INSIGHT_STATE_KEY,
    RELEVANCE_SECURITY_STATE_KEY,
    RELEVANCE_OPENNESS_STATE_KEY,
    RELEVANCE_QUALITY_STATE_KEY,
    RELEVANCE_FEDERATION_STATE_KEY,
    RELEVANCE_CURATION_STATE_KEY,
    RELEVANCE_EVOLUTION_STATE_KEY,
    CHALLENGE_GOOD_STATE_KEY,
    CHALLENGE_VALUE_STATE_KEY,
    CHALLENGE_INSIGHT_STATE_KEY,
    CHALLENGE_SECURITY_STATE_KEY,
    CHALLENGE_OPENNESS_STATE_KEY,
    CHALLENGE_QUALITY_STATE_KEY,
    CHALLENGE_FEDERATION_STATE_KEY,
    CHALLENGE_CURATION_STATE_KEY,
    CHALLENGE_EVOLUTION_STATE_KEY,
    OPERATIONALIZATION_CHALLENGES_STATE_KEY,
    COMMUNICATION_METHODS_STATE_KEY,
    NEED_FOR_VISUAL_TOOL_STATE_KEY,
    REASONS_AGAINST_VISUAL_TOOL_STATE_KEY,
    PREPAREDNESS_FOR_ARGUMENT_STATE_KEY,
    CHALLENGES_ADOPTION,
    SUPPORT_FOR_ASSURANCE_STATE_KEY,
    SUPPORT_FOR_ASSURANCE_OTHER_STATE_KEY,
]

conditional_keys = {
    TYPE_DT_OTHER_STATE_KEY: {
        "depends_on_key": [
            TYPE_DT_STATE_KEY,
        ],
        "depends_on_response": ["Other (Please specify)"],
    },
    PURPOSE_DT_OTHER_STATE_KEY: {
        "depends_on_key": [PURPOSE_DT_STATE_KEY],
        "depends_on_response": ["Other (Please specify)"],
    },
    NO_DT_REASON_STATE_KEY: {
        "depends_on_key": [ESTABLISHED_DT_STATE_KEY],
        "depends_on_response": ["No"],
    },
    TYPE_DT_STATE_KEY: {
        "depends_on_key": [ESTABLISHED_DT_STATE_KEY],
        "depends_on_response": [
            "Yes",
            "Indirectly (We support clients "
            "or provide components for digital twins)",
        ],
    },
    PURPOSE_DT_STATE_KEY: {
        "depends_on_key": [ESTABLISHED_DT_STATE_KEY],
        "depends_on_response": [
            "Yes",
            "Indirectly (We support clients "
            "or provide components for digital twins)",
        ],
    },
    ASSURED_PROPERTIES_OTHER_STATE_KEY: {
        "depends_on_key": [ASSURED_PROPERTIES_STATE_KEY],
        "depends_on_response": ["Other (Please specify)"],
    },
    ASSURANCE_MECHANISM_OTHER_STATE_KEY: {
        "depends_on_key": [ASSURANCE_MECHANISMS_STATE_KEY],
        "depends_on_response": ["Other (Please specify)"],
    },
    SUPPORT_FOR_ASSURANCE_OTHER_STATE_KEY: {
        "depends_on_key": [SUPPORT_FOR_ASSURANCE_STATE_KEY],
        "depends_on_response": ["Other (Please specify)"],
    },
    FRAMEWORK_DESCRIPTION_STATE_KEY: {
        "depends_on_key": [ETHICAL_FRAMEWORK_EXISTENCE_STATE_KEY],
        "depends_on_response": ["Yes  / Something similar"],
    },
    FRAMEWORK_DEVELOPMENT_STATE_KEY: {
        "depends_on_key": [ETHICAL_FRAMEWORK_EXISTENCE_STATE_KEY],
        "depends_on_response": ["Yes  / Something similar"],
    },
    REASONS_AGAINST_VISUAL_TOOL_STATE_KEY: {
        "depends_on_key": [NEED_FOR_VISUAL_TOOL_STATE_KEY],
        "depends_on_response": ["No"],
    },
    BENEFITS_OF_VISUAL_TOOL_STATE_KEY: {
        "depends_on_key": [NEED_FOR_VISUAL_TOOL_STATE_KEY],
        "depends_on_response": ["Yes"],
    },
    PARTNER_TRUST_DIFFICULTY_STATE_KEY: {
        "depends_on_key": [ASSET_DATA_SHARING_STATE_KEY],
        "depends_on_response": ["Yes"],
    },
    PARTNER_TRUST_CHALLENGES_STATE_KEY: {
        "depends_on_key": [PARTNER_TRUST_DIFFICULTY_STATE_KEY],
        "depends_on_response": [
            "Neutral",
            "Somewhat Difficult",
            "Very Difficult",
        ],
    },
    RELIANCE_ON_EVIDENCE_STATE_KEY: {
        "depends_on_key": [ASSET_DATA_SHARING_STATE_KEY],
        "depends_on_response": ["Yes"],
    },
    CHALLENGE_GOOD_STATE_KEY: {
        "depends_on_key": [RELEVANCE_GOOD_STATE_KEY],
        "depends_on_response": [
            "Slightly",
            "Moderately",
            "Very",
            "Extremely Relevant",
        ],
    },
    CHALLENGE_VALUE_STATE_KEY: {
        "depends_on_key": [RELEVANCE_VALUE_STATE_KEY],
        "depends_on_response": [
            "Slightly",
            "Moderately",
            "Very",
            "Extremely Relevant",
        ],
    },
    CHALLENGE_INSIGHT_STATE_KEY: {
        "depends_on_key": [RELEVANCE_INSIGHT_STATE_KEY],
        "depends_on_response": [
            "Slightly",
            "Moderately",
            "Very",
            "Extremely Relevant",
        ],
    },
    CHALLENGE_SECURITY_STATE_KEY: {
        "depends_on_key": [RELEVANCE_SECURITY_STATE_KEY],
        "depends_on_response": [
            "Slightly",
            "Moderately",
            "Very",
            "Extremely Relevant",
        ],
    },
    CHALLENGE_OPENNESS_STATE_KEY: {
        "depends_on_key": [RELEVANCE_OPENNESS_STATE_KEY],
        "depends_on_response": [
            "Slightly",
            "Moderately",
            "Very",
            "Extremely Relevant",
        ],
    },
    CHALLENGE_QUALITY_STATE_KEY: {
        "depends_on_key": [RELEVANCE_QUALITY_STATE_KEY],
        "depends_on_response": [
            "Slightly",
            "Moderately",
            "Very",
            "Extremely Relevant",
        ],
    },
    CHALLENGE_FEDERATION_STATE_KEY: {
        "depends_on_key": [RELEVANCE_FEDERATION_STATE_KEY],
        "depends_on_response": [
            "Slightly",
            "Moderately",
            "Very",
            "Extremely Relevant",
        ],
    },
    CHALLENGE_CURATION_STATE_KEY: {
        "depends_on_key": [RELEVANCE_CURATION_STATE_KEY],
        "depends_on_response": [
            "Slightly",
            "Moderately",
            "Very",
            "Extremely Relevant",
        ],
    },
    CHALLENGE_EVOLUTION_STATE_KEY: {
        "depends_on_key": [RELEVANCE_EVOLUTION_STATE_KEY],
        "depends_on_response": [
            "Slightly",
            "Moderately",
            "Very",
            "Extremely Relevant",
        ],
    },
    OPERATIONALIZATION_CHALLENGES_STATE_KEY: {
        "depends_on_key": [
            CHALLENGE_GOOD_STATE_KEY,
            CHALLENGE_VALUE_STATE_KEY,
            CHALLENGE_INSIGHT_STATE_KEY,
            CHALLENGE_SECURITY_STATE_KEY,
            CHALLENGE_OPENNESS_STATE_KEY,
            CHALLENGE_QUALITY_STATE_KEY,
            CHALLENGE_FEDERATION_STATE_KEY,
            CHALLENGE_CURATION_STATE_KEY,
            CHALLENGE_EVOLUTION_STATE_KEY,
        ],
        "depends_on_response": [
            "Slightly",
            "Moderately",
            "Very",
            "Extremely challenging",
        ],
    },
}
