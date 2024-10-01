def chande_momentum_oscillator(df, period=14):
    """
    Chande Momentum Oscillator compares the sum of gains and losses over a specified period to detect momentum.
    """
    df['diff'] = df['close'].diff()
    df['gains'] = df['diff'].clip(lower=0)
    df['losses'] = -df['diff'].clip(upper=0)
    sum_gains = df['gains'].rolling(window=period).sum()
    sum_losses = df['losses'].rolling(window=period).sum()

    df['cmo'] = 100 * ((sum_gains - sum_losses) / (sum_gains + sum_losses))

    df['indicator_signals'] = 0
    df.loc[df['cmo'] > 50, 'indicator_signals'] = 1
    df.loc[df['cmo'] < -50, 'indicator_signals'] = -1
    
    return df.drop(columns=['diff', 'gains', 'losses', 'cmo'])