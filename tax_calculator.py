# ============================================
# SRI LANKAN TAX CALCULATOR
# Effective April 1, 2025
# ============================================
# Annual Income Tax Brackets (LKR):
#   Up to 1,800,000          :  0%
#   1,800,001  -  2,800,000  :  6%
#   2,800,001  -  3,300,000  : 18%
#   3,300,001  -  3,800,000  : 24%
#   3,800,001  -  4,300,000  : 30%
#   Above 4,300,000          : 36%
# ============================================


def calculate_income_tax(annual_income):
    """
    Calculate progressive income tax based on Sri Lankan tax brackets
    (effective April 1, 2025).

    Args:
        annual_income: Annual income in LKR (float or int)

    Returns:
        Total income tax amount (float)

    Example:
        >>> calculate_income_tax(4000000)
        330000.0
    """
    # Pre-compute the maximum tax contribution of each bracket
    bracket1 = 1000000 * 0.06   # 1,800,001 – 2,800,000 @ 6%
    bracket2 = 500000 * 0.18    # 2,800,001 – 3,300,000 @ 18%
    bracket3 = 500000 * 0.24    # 3,300,001 – 3,800,000 @ 24%
    bracket4 = 500000 * 0.30    # 3,800,001 – 4,300,000 @ 30%
    bracket5 = (annual_income - 4300000) * 0.36  # Above 4,300,000 @ 36%

    # Accumulate tax from all brackets the income falls into
    if annual_income <= 1800000:
        return 0.0
    elif annual_income <= 2800000:
        return (annual_income - 1800000) * 0.06
    elif annual_income <= 3300000:
        return bracket1 + (annual_income - 2800000) * 0.18
    elif annual_income <= 3800000:
        return bracket1 + bracket2 + (annual_income - 3300000) * 0.24
    elif annual_income <= 4300000:
        return bracket1 + bracket2 + bracket3 + (annual_income - 3800000) * 0.30
    else:
        return bracket1 + bracket2 + bracket3 + bracket4 + bracket5


def calculate_effective_tax_rate(annual_income):
    """
    Calculate effective tax rate as a percentage.

    Args:
        annual_income: Annual income in LKR (float or int)

    Returns:
        Effective tax rate as percentage (float)

    Example:
        >>> calculate_effective_tax_rate(4000000)
        8.25
    """
    total_tax = calculate_income_tax(annual_income)
    return round((total_tax / annual_income) * 100, 2)


def calculate_take_home(annual_income):
    """
    Calculate take-home income after tax.

    Args:
        annual_income: Annual income in LKR (float or int)

    Returns:
        Take-home income (float)

    Example:
        >>> calculate_take_home(4000000)
        3670000.0
    """
    return annual_income - calculate_income_tax(annual_income)


# ============================================
# DISPLAY HELPERS
# ============================================

def print_taxpayer_details(income):
    """Print detailed tax information for a single taxpayer."""
    tax = calculate_income_tax(income)
    effective_rate = calculate_effective_tax_rate(income)
    take_home = calculate_take_home(income)
    monthly_take_home = take_home / 12

    print(f"\nAnnual Income:          Rs. {income:,.2f}")
    print(f"  Income Tax:           Rs. {tax:,.2f} ({effective_rate:.2f}%)")
    print(f"  Take-Home (Annual):   Rs. {take_home:,.2f}")
    print(f"  Take-Home (Monthly):  Rs. {monthly_take_home:,.2f}")
    print("-" * 60)


def print_ranking(sorted_income_tax_pairs):
    """Print ranked list of taxpayers by tax paid."""
    for rank, (income, tax) in enumerate(sorted_income_tax_pairs, start=1):
        print(f"{rank}. Rs. {income:,.2f} - Tax Paid: Rs. {tax:,.2f}")


def print_high_earners(high_earner_incomes):
    """Print details for high earners (>= Rs. 4,300,000)."""
    for income in high_earner_incomes:
        tax = calculate_income_tax(income)
        print(f"Income: Rs. {income:,.2f} - Tax: Rs. {tax:,.2f}")


# ============================================
# MAIN
# ============================================

def main():
    """Run tax calculations and display reports for a set of taxpayer incomes."""

    incomes = [2500000, 4000000, 5000000, 1500000, 3500000]

    # Compute tax for every income, filter top-bracket earners,
    # and rank all taxpayers from highest to lowest tax paid
    taxes = list(map(calculate_income_tax, incomes))
    high_earners = list(filter(lambda income: income >= 4300000, incomes))
    sorted_incomes_taxes = sorted(
        zip(incomes, taxes), key=lambda pair: pair[1], reverse=True
    )

    print("=" * 60)
    print("   SRI LANKAN TAX CALCULATOR (April 2025 Tax Reforms)")
    print("=" * 60)

    print("\n" + "=" * 60)
    print("DETAILED TAX REPORTS")
    print("=" * 60)
    for income in incomes:
        print_taxpayer_details(income)

    print("\n" + "=" * 60)
    print("TOP TAXPAYERS (Ranked by Tax Paid)")
    print("=" * 60)
    print_ranking(sorted_incomes_taxes)

    print("\n" + "=" * 60)
    print("HIGH EARNERS (>= Rs. 4,300,000 — Top Tax Bracket)")
    print("=" * 60)
    print_high_earners(high_earners)

    print("\n" + "=" * 60)
    print("SUMMARY STATISTICS")
    print("=" * 60)

    # Aggregate totals and derive averages across all taxpayers
    incomes_total = sum(incomes)
    total_tax_revenue = sum(taxes)
    avg_effective_tax_rate = round(
        (total_tax_revenue / incomes_total) * 100, 2)
    avg_yearly_income = incomes_total / len(incomes)
    avg_tax = total_tax_revenue / len(taxes)
    avg_monthly_take_home = round((avg_yearly_income - avg_tax) / 12, 2)

    print(f"Total Tax Revenue:          {total_tax_revenue:,.2f} LKR")
    print(f"Average Effective Tax Rate: {avg_effective_tax_rate}%")
    print(f"Highest Tax Amount:         {max(taxes):,.2f} LKR")
    print(f"Lowest Tax Amount:          {min(taxes):,.2f} LKR")
    print(f"Average Monthly Take-home:  {avg_monthly_take_home:,.2f} LKR")


if __name__ == "__main__":
    main()
