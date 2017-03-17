# Implementation 3
### Yingshi Huang, Annie Lei

This repository contains three directories-- ``bestfit`` is for the first
question, ``temperature`` is for the second question, and ``bonus`` is for the
bonus question. It also contains the report, ``imp3.pdf``.

## Part I, Warm-up question

- ``cd bestfit``
- ``python bestfit.py``. Note: requires that ``pulp`` is installed.
- See the report for the plot.

## Part II, Warming-up question

- ``cd temperature``
- ``python tempChange.py`` to find the optimal solution. Requires ``pulp``.
- ``warmUp2.png`` contains the plot of the points, best fit curve, and linear
part of the best fit curve. To regenerate it, run ``python warm_up2_plot.py``
(requires ``matplotlib``)

## Part III, Bonus

- ``cd bonus``
- ``orig_download.csv`` contains the original info downloaded from NOAA.
``Birmingham_clean.csv`` contains the cleaned version. To reclean the
data, run ``python clean_birmingham.py``. This script finds each day's
average temperature, TAVG, from (TMIN + TMAX) / 2.
- ``python bonus.py`` to find the optimal solution. Requires ``pulp``.
- ``Bonus.png`` contains the plot of the points, best fit curve, and linear
part of the best fit curve. To regenerate it, run ``bonus_fig.py`` (requires
``matplotlib``)
