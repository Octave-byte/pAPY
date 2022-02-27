# 💸 Lending Pool performance

## What is a lending pool ?

It is a place where users give liquidity in a common way, so that other users can borrow this liquidity. The lenders are paid by the borrowers in the form of interest rates.

## Performance based on utilisation



On protocol such as AAVE, Compound or Anchor, interest rates are calibrated in order to "manage liquidity risk and optimise utilisation" (i.e. Aave docs).

This interest rate is discretionary in Anchor protocol. 19.5% are offered even if this rate is only possible thanks to reserves amount being filled up manually.&#x20;

The calculation process of the deposit rate is a bit different in AAVE :&#x20;

Depositors share the interests paid by borrowers corresponding to the average borrow rate times the utilisation rate as well as flash loan rewards.  The utilisation rate is the ratio between borrowed liquidity and total liquidity.

Basically, APY can be computed in two steps :&#x20;

* First, take the daily deposit rate (on annual basis) which can be considered as daily APR
* Then, we compound these APR on a daily basis in order to obtain an approximation of the APY with this formula

![APR to APY formula](<../.gitbook/assets/image (2).png>)









## Similar concerns than for vault

### USD denominated vs. underlying token denominated

As for vaults we can add the fx effect of underlying token to the pool APY.

### Fees

Please find a recap of lending pool fees for major platform.

Withdrawal fees are not included yet in our methodology.

### Native rewards vs. Liquidity rewards

As Aave was able to do at the release of V2, the protocols offer additional interest rate rewards to lenders in the form of governance tokens. These rewards are discretionary, non-resilient and not included in the methodology.





