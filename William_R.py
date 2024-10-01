def williams_percent_r(df, period=14):
    """
    Williams %R compares the close price to the high-low range over a specified period to detect overbought/oversold levels.
    """
    highest_high = df['high'].rolling(window=period).max()
    lowest_low = df['low'].rolling(window=period).min()

    df['wpr'] = -100 * (highest_high - df['close']) / (highest_high - lowest_low)

    df['indicator_signals'] = 0
    df.loc[df['wpr'] > -20, 'indicator_signals'] = 1
    df.loc[df['wpr'] < -80, 'indicator_signals'] = -1
    
    return df.drop(columns=['wpr'])