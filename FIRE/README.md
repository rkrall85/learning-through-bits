

Table of Contents

<!-- TOC -->
* [Fire Reports](#fire-reports)
    * [HeatMaps](#heatmaps)
    * [Various Reports](#various-reports)
* [Fire Calculations](#fire-calculations-)
    * [Rate of Return](#rate-of-return-)
    * [Compound Annual Growth Rate](#compound-annual-growth-rate)
    * [IRR](#irr)
<!-- TOC -->



----
**********************
*********************
*********************



# Fire Reports


### HeatMaps

We have different types of HeatMaps.  The code is located [here](HeatMaps).

### Various Reports

1. [Fire Tracker](/reports/fire_trackers.ipynb)
2. [Current Year Tracker](/reports/current_year_tracker.ipynb)
3. [Yearly Balance](/reports/yearly_balance.ipynb)
4. [Yearly Contributions](/reports/yearly_contributions.ipynb)


----
**********************
*********************
*********************


# Fire Calculations 


### Rate of Return 

This is the calc we use for Rate of Return.  This seems like the most accurate for the data being collected currently.

```

market_gains = ('Ending Balance' - 'Total Contributions' - 'Initial Balance' - 'Initial Roll Over' - 'Starting Balance')
rate_of_return = market_gains / 'Ending Balance'

```

----


### Compound Annual Growth Rate

One of the calculations we do to track the FIRE progress is the CAGR <i>(Compound Annual Growth Rate)</i>. <br/>
Here is the formula is in the simplest terms.  We modified it a little to account for Roll Over Contributions to get an accurate measure. <br>

```python
((BV / EV)**(1/n)-1)×100
```

```markdown
EV = Ending Value
BV = Beginning Value
n = Number of Years
```
Learn more [here](https://www.investopedia.com/terms/c/cagr.asp).

---

### IRR

<i>WIP</i>
