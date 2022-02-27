# 🔍 Advanced metrics - WIP

{% hint style="warning" %}
Caveat : these features are not implemented yet and are just for information, feel free to fill out the questionnaire if you want to see them in the next release.
{% endhint %}



## Performance metrics



### Basic parameters

#### TVL

The total value locked of a strategy shows some things about that strategy. The TVL level of a strategy is an opportunity because it allows the strategy to open up to any DeFi market in order to generate returns. It is also a weakness because it is more difficult to generate returns for greater liquidity with constant activity.&#x20;

Also the TVL can evoke how juvenile the strategy is and how concentrated the liquidity is. As in Tradfi with the Holding Ratio, it is unlikely that an investor will want to represent too large a percentage of the pool, his exit or entry can destabilize the strategy.

#### Strategy age

The inception date of a strategy is an interesting indicator before considering an investment. An older strategy with stable performance despite changing historical market conditions will be considered by some investors as better than a strategy with better performance but much more recent.

### Volatility of APY

The volatility of the APY is expressed as the standard deviation of the weekly APY calculated. By nature of the calculation, the APY is smoothed over an average of the last 7 days, and its volatility is therefore artificially decreased. This method is preferred to the volatility of the daily APY because the daily APY presents too many zero returns on certain days.

The lower the volatility, the closer the calculated historical APYs will be to the investor's real returns.

### Trend of APY

A regression line is fitted on the monthly APY. The sign of the a-coefficient of this line shows if the strategy performance increase(+) or decrease (-) accross time. The p-value of the regression shows if this trend is significant or not.

### Correlation of APY vs. TVL

A pearson correlation is computed between the TVL and the monthly APY of a strategy. This correlation factor shows whether the strategy performance increase when liquidity is added or not.&#x20;

Empirically, this correlation is negative which tends to highlight that it is harder and harder to maintain a performance when liquidity is added.

### Correlation of APY vs. underlying token performance in USD

When your performance is USD denominated, you will need to correlate the monthly APY value and the token performance. If correlation is great.&#x20;

Delta neutral strategies have 0 correlation on this aspect.&#x20;

### Volatility of underlying token performance in USD

Volatility of the underlying token in USD denominated strategy are important to monitor. You might not want considering a strategy on some vaults if your strategy is based in USD.

### Ratio liquidity rewards on total rewards

One could say that liquidity rewards are non-native rewards that are here to boost APY figures. It is crucial to take into consideration the ratio between liquidity rewards and total rewards accross time so as to understand how APY was built.&#x20;





## Resilience metrics

Ok, now than you some clues in order to assess performance of your favorite strategy, you still need to know how these strategies are behaving in a risk management perspective.

### Protocol safety score

Number of hacks : [https://rekt.news/en/](https://rekt.news/en/)

Protocol safety score : [https://www.defisafety.com/](https://www.defisafety.com)





