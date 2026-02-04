import argparse

from bot.validators import validate_inputs
from bot.orders import place_market_order, place_limit_order
from bot.logging_config import setup_logger

logger = setup_logger()


def main():
    parser = argparse.ArgumentParser(description="Binance Futures Trading Bot (Testnet)")

    parser.add_argument("--symbol", required=True, help="Trading symbol (e.g., BTCUSDT)")
    parser.add_argument("--side", required=True, help="Order side: BUY or SELL")
    parser.add_argument("--type", required=True, help="Order type: MARKET or LIMIT")
    parser.add_argument("--quantity", required=True, help="Order quantity")
    parser.add_argument("--price", required=False, help="Price (required for LIMIT orders)")

    args = parser.parse_args()

    try:
        data = validate_inputs(
            symbol=args.symbol,
            side=args.side,
            order_type=args.type,
            quantity=args.quantity,
            price=args.price,
        )

        if data["order_type"] == "MARKET":
            order = place_market_order(
                symbol=data["symbol"],
                side=data["side"],
                quantity=data["quantity"],
            )
        else:
            order = place_limit_order(
                symbol=data["symbol"],
                side=data["side"],
                quantity=data["quantity"],
                price=data["price"],
            )

        print("\n✅ Order placed successfully")
        print("Order ID:", order.get("orderId"))
        print("Status:", order.get("status"))
        print("Executed Qty:", order.get("executedQty"))
        print("Average Price:", order.get("avgPrice"))

        logger.info(f"Order placed successfully: {order}")

    except Exception as e:
        logger.error(f"Error placing order: {e}")
        print("\n❌ Error:", e)


if __name__ == "__main__":
    main()
