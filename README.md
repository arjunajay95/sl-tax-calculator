# Sri Lankan Tax Calculator

A Python program that calculates progressive income tax based on Sri Lanka's April 2025 tax reforms. It processes multiple taxpayer incomes, generates detailed breakdowns, ranks taxpayers by tax paid, and outputs summary statistics.

<br>

## What It Does

Given a list of annual incomes, the program:

- Calculates income tax, effective tax rate, and take-home pay for each person
- Identifies high earners in the top tax bracket (above Rs. 4,300,000)
- Ranks all taxpayers from highest to lowest tax paid
- Outputs a summary with total tax revenue, averages, and monthly take-home figures

**Tax Brackets (Effective April 1, 2025):**

| Annual Income (LKR) | Rate |
|---|---|
| Up to 1,800,000 | 0% |
| 1,800,001 - 2,800,000 | 6% |
| 2,800,001 - 3,300,000 | 18% |
| 3,300,001 - 3,800,000 | 24% |
| 3,800,001 - 4,300,000 | 30% |
| Above 4,300,000 | 36% |

<br>

## How to Run

No dependencies needed. Just Python 3.

```bash
python tax_calculator.py
```

The `incomes` list in `main()` can be edited to test different values.

<br>

## Key Concepts

**Progressive tax logic** is the core of this project. Rather than applying a single flat rate, the calculator splits income across each bracket and accumulates the tax owed at each tier. Tracing through a manual example first made writing the `if/elif` logic much cleaner.

**Functional programming** is used throughout `main()`. `map()` runs the tax calculation across every income in the list, `filter()` pulls out only the top-bracket earners, and `sorted()` with a lambda key ranks everyone by tax paid. It's a cleaner approach than writing manual loops for each operation.

**`zip()`** pairs the incomes list with the calculated taxes before sorting, so each income stays matched to its corresponding tax figure through the ranking step.

<br>

## What I Learned

This was my first project where multiple Python concepts had to work together rather than being practiced in isolation. Writing the progressive tax function required actual problem-solving, not just syntax recall. Getting the bracket logic right meant understanding the math first, then translating it into code.

The functional programming side was a shift in thinking. Once it clicked that `map()`, `filter()`, and `sorted()` are just cleaner ways to do things I'd already been doing with loops, they became much less intimidating to use.
