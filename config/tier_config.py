import dataclasses

@dataclasses.dataclass
class TierConfig:
    environment = "preprod"
    tier_name = "Tier Joseph Test"
    tier_description = "Tier Testing"
    required_currencies = ['BTC-EUR']
    tradias_entity_id = "53d6389d-99a4-4ed8-a7dd-3682f7bc09c3"
    tier_type = "OTC"