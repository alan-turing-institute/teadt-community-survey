CONNECTION_STRING_ENV: str = "CONNECTION_STRING"
DATABASE_NAME_ENV: str = "DB_NAME"
COLLECTION_NAME_ENV: str = "COLLECTION_NAME"

# TODO: Maybe move them to each page?

# Consent Page Keys
CONSENT_QUESTIONS: int = 10
CONSENT_STATE_KEY: str = "consent"
ALL_CONSENT_STATE_KEYS: list[str] = [
    f"{CONSENT_STATE_KEY}_{index}" for index in range(CONSENT_QUESTIONS)
]

# Community Page Keys
USER_ID_STATE_KEY: str = "_id"
SECTOR_STATE_KEY: str = "sector"
LOCATION_STATE_KEY: str = "location"
ROLE_STATE_KEY: str = "role"
RESPONSIBILITIES_STATE_KEY: str = "primary_responsibilities"
ESTABLISHED_DT_STATE_KEY: str = "established_dt"
TYPE_DT_STATE_KEY: str = "type_dt"
TYPE_DT_OTHER_STATE_KEY: str = "type_dt_other"
NO_DT_REASON_STATE_KEY: str = "no_dt_reason"

# Current Practices Page Keys
ASSURANCE_MEANING_STATE_KEY: str = "assurance_meaning"
ASSURANCE_MECHANISMS_STATE_KEY: str = "assurance_mechanisms"
ASSURANCE_MECHANISM_OTHER_STATE_KEY: str = "assurance_mechanism_other"
ASSURED_PROPERTIES_STATE_KEY: str = "assured_properties"
ASSURED_PROPERTIES_OTHER_STATE_KEY: str = "assured_properties_other"
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
SUPPORT_FOR_ASSURANCE_STATE_KEY: str = "support_for_assurance"
SUPPORT_FOR_ASSURANCE_OTHER_STATE_KEY: str = "support_for_assurance_other"

# Follow-up Page Keys
ADDITIONAL_INSIGHTS_STATE_KEY: str = "additional_insights"
WORKSHOP_INTEREST_STATE_KEY: str = "workshop_interest"
PROJECT_INTEREST_STATE_KEY: str = "project_interest"
EMAIL_INTEREST_STATE_KEY: str = "email_interest"
EMAIL_STATE_KEY: str = "email"

# TODO(cptanalastriste): Refactor. There's a better way of doing this.
ALL_SESSION_KEYS: list[str] = ALL_CONSENT_STATE_KEYS + [
    USER_ID_STATE_KEY,
    SECTOR_STATE_KEY,
    LOCATION_STATE_KEY,
    ROLE_STATE_KEY,
    RESPONSIBILITIES_STATE_KEY,
    ESTABLISHED_DT_STATE_KEY,
    TYPE_DT_STATE_KEY,
    NO_DT_REASON_STATE_KEY,
    ASSURANCE_MEANING_STATE_KEY,
    ASSURANCE_MECHANISMS_STATE_KEY,
    ASSURED_PROPERTIES_STATE_KEY,
    ASSET_DATA_SHARING_STATE_KEY,
    PARTNER_TRUST_DIFFICULTY_STATE_KEY,
    PARTNER_TRUST_CHALLENGES_STATE_KEY,
    RELIANCE_ON_EVIDENCE_STATE_KEY,
    INTEGRATE_ASSURANCE_STATE_KEY,
    COMMUNICATION_IMPACT_STATE_KEY,
    LINK_ASSURANCE_ACTIVITIES_STATE_KEY,
    SATISFACTION_JUSTIFICATION_STATE_KEY,
    USER_ID_STATE_KEY,
    ETHICAL_FRAMEWORK_EXISTENCE_STATE_KEY,
    FRAMEWORK_DESCRIPTION_STATE_KEY,
    FRAMEWORK_DEVELOPMENT_STATE_KEY,
    VALUE_OF_GUIDING_PRINCIPLES_STATE_KEY,
    FAMILIARITY_WITH_GEMINI_PRINCIPLES_STATE_KEY,
    COMMUNICATION_METHODS_STATE_KEY,
    NEED_FOR_VISUAL_TOOL_STATE_KEY,
    BENEFITS_OF_VISUAL_TOOL_STATE_KEY,
    REASONS_AGAINST_VISUAL_TOOL_STATE_KEY,
    PREPAREDNESS_FOR_ARGUMENT_STATE_KEY,
    SUPPORT_FOR_ASSURANCE_STATE_KEY,
    ADDITIONAL_INSIGHTS_STATE_KEY,
    WORKSHOP_INTEREST_STATE_KEY,
    PROJECT_INTEREST_STATE_KEY,
    EMAIL_INTEREST_STATE_KEY,
    EMAIL_STATE_KEY,
]
