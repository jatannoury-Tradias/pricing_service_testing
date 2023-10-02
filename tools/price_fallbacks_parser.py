from config.OPC_config import OpcConfig
from models.PriceFallbackHierarchy import PriceFallbackHierarchy

def missing_entries_filler(price_fallbacks):
    for price_fallback in price_fallbacks:
        price_fallback_name = price_fallback['name']
        try:
            order = OpcConfig.EXCHANGE_HIERARCHY.index(price_fallback_name)
            price_fallback['order'] = order
            price_fallback['enabled'] = True
        except:
            raise ValueError(
                f"{price_fallback_name} is not configured in the EXCHANGE_HIERARCHY. Kindly go to config/OPC_config and add it.")
    return price_fallbacks

def order_fixer(price_fallbacks):
    price_fallbacks = sorted(price_fallbacks, key=lambda element: element['order'])
    for index, fb in enumerate(price_fallbacks):
       fb['order'] = index
    return price_fallbacks

def parse_price_fallbacks(price_fallbacks):
    print("====================>", price_fallbacks)
    return [PriceFallbackHierarchy.parse_obj(price_fallback) for price_fallback in order_fixer(missing_entries_filler(price_fallbacks))]