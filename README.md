# Binance Futures Trading Bot (Testnet)

A Python-based trading bot that places MARKET and LIMIT orders on the Binance Futures Testnet using a clean command-line interface.

---

## Features
- Binance Futures Testnet integration
- MARKET and LIMIT order support
- Input validation and error handling
- Environment variable–based API key management
- Structured logging
- Command-line interface using argparse


---

## Project Structure
bot/
 ├── client.py          # Binance client setup
 ├── validators.py      # Input validation
 ├── orders.py          # Order placement logic
 ├── cli.py             # CLI entry point
 ├── logging_config.py  # Logging configuration
logs/
 └── app.log            # Application logs


---

## Setup Instructions

### 1. Create and activate virtual environment
```bash
python -m venv venv

**Linux / macOS**
```bash
source venv/bin/activate


**Windows (PowerShell)**
```powershell
venv\Scripts\activate


---

### 2. Install dependencies
```bash
pip install -r requirements.txt


---

### 3. Set environment variables
**Linux / macOS**
```bash
export BINANCE_API_KEY="your_api_key"
export BINANCE_API_SECRET="your_api_secret"

**Windows (PowerShell)**
$env:BINANCE_API_KEY="your_api_key"
$env:BINANCE_API_SECRET="your_api_secret"


---

## Usage
### Market Order
```bash
python -m bot.cli --symbol BTCUSDT --side BUY --type MARKET --quantity 0.003

### Limit Order
```bash
python -m bot.cli --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.003 --price 71000

---

## Logging
All actions, order responses, and errors are logged to:
logs/app.log

---

## Notes
- Uses Binance Futures Testnet (no real funds involved)
- Handles exchange constraints such as minimum notional value and price bands
