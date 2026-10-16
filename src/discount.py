BASE_DISCOUNT_THRESHOLD = 15000
BASE_DISCOUNT_MULTIPLIER = 0.85
SUMMER_PROMO_AMOUNT = 500
VIP_PROMO_MULTIPLIER = 0.90
TIER_MULTIPLIERS = {1: 0.97, 2: 0.93}
MIN_PRICE_RATIO = 0.70


def calculate_cart_total(cart_sum, tier, promos):
    """Итоговая стоимость корзины с учетом скидок и промокодов."""
    price = cart_sum
    if cart_sum > BASE_DISCOUNT_THRESHOLD:
        price = cart_sum * BASE_DISCOUNT_MULTIPLIER
    for promo in promos:
        if promo == "SUMMER":
            price = price - SUMMER_PROMO_AMOUNT
        elif promo == "VIP":
            price = price * VIP_PROMO_MULTIPLIER
    price = price * TIER_MULTIPLIERS.get(tier, 1.0)
    return max(price, cart_sum * MIN_PRICE_RATIO)
