from binance.enums import SIDE_BUY, SIDE_SELL, ORDER_TYPE_MARKET, ORDER_TYPE_LIMIT
from binance.exceptions import BinanceAPIException, BinanceRequestException

from bot.client import get_binance_client
from bot.logging_config import setup_logger

logger = setup_logger()


def place_market_order(symbol, side, quantity):
    client = get_binance_client()

    try:
        logger.info(
            f"Placing MARKET order | Symbol: {symbol}, Side: {side}, Quantity: {quantity}"
        )

        order = client.futures_create_order(
            symbol=symbol,
            side=SIDE_BUY if side == "BUY" else SIDE_SELL,
            type=ORDER_TYPE_MARKET,
            quantity=quantity,
        )

        logger.info(f"Market order placed successfully: {order}")
        return order

    except (BinanceAPIException, BinanceRequestException) as e:
        logger.error(f"Market order failed: {e}")
        raise


def place_limit_order(symbol, side, quantity, price):
    client = get_binance_client()

    try:
        logger.info(
            f"Placing LIMIT order | Symbol: {symbol}, Side: {side}, Quantity: {quantity}, Price: {price}"
        )

        order = client.futures_create_order(
            symbol=symbol,
            side=SIDE_BUY if side == "BUY" else SIDE_SELL,
            type=ORDER_TYPE_LIMIT,
            quantity=quantity,
            price=price,
            timeInForce="GTC",
        )

        logger.info(f"Limit order placed successfully: {order}")
        return order

    except (BinanceAPIException, BinanceRequestException) as e:
        logger.error(f"Limit order failed: {e}")
        raise
