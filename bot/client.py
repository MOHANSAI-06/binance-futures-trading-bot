import os
import time
from binance.client import Client
from binance.exceptions import BinanceAPIException, BinanceRequestException

from bot.logging_config import setup_logger

logger = setup_logger()


def get_binance_client():
    api_key = os.getenv("BINANCE_API_KEY")
    api_secret = os.getenv("BINANCE_API_SECRET")

    if not api_key or not api_secret:
        logger.error("Binance API key or secret not found in environment variables")
        raise ValueError("API credentials are missing")

    try:
        client = Client(api_key, api_secret, testnet=True)


        client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

        server_time = client.get_server_time()
        client.timestamp_offset = server_time["serverTime"] - int(time.time() * 1000)

        logger.info("Binance Futures Testnet client initialized successfully")
        return client

    except (BinanceAPIException, BinanceRequestException) as e:
        logger.error(f"Error initializing Binance client: {e}")
        raise
