
from typing import Tuple

from config.tier_config import TierConfig
from models.Tier import Tier

def get_tier_inputs() -> Tier:
    return Tier(
        name=TierConfig.tier_name,
        description= TierConfig.tier_description,
        instrument_codes = TierConfig.required_currencies,
        tier_type=TierConfig.tier_type,
        tradias_entity_id=TierConfig.tradias_entity_id
    )
def get_all_inputs() -> Tuple[str,Tier,str]:
    tier_validation = get_tier_inputs()
    return TierConfig.environment, tier_validation,TierConfig.tier_type