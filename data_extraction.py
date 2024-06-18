import requests
import pandas as pd

def get_binance_data(symbol='BTCUSDT'):
    url = f"https://api.binance.com/api/v3/klines?symbol={symbol}&interval=1d&limit={1000}"
    response = requests.get(url)
    data = response.json()
    
    df = pd.DataFrame(data, columns=['unix', 'open', 'high', 'low', 'close', 'volume', 'close_time', 'quote_asset_volume', 'number_of_trades', 'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume', 'ignore'])
    
    df['date'] = pd.to_datetime(df['unix'], unit='ms')
    df['symbol'] = symbol  # Manually adding the symbol column
    df = df[['unix', 'date', 'symbol', 'open', 'high', 'low', 'close', 'volume']]
    
    # Reorder DataFrame with latest data first
    df = df[::-1].reset_index(drop=True)
    
    # Format date as MMDDYYYY
    df['date'] = df['date'].dt.strftime('%m-%d-%Y')
    
    return df

# Fetch the latest data
latest_data = get_binance_data(symbol='BTCUSDT')

# Save to CSV file
latest_data.to_csv('latest_binance_data.csv', index=False)


