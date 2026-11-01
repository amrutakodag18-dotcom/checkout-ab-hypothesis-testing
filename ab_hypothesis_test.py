import numpy as np
import pandas as pd
from statsmodels.stats.proportion import proportions_ztest

# 1. Load the A/B Test Dataset
file_name = 'checkout_ab_test.csv'
df = pd.read_csv(file_name)

print('--- 1. Dataset Overview ---')
print(df.head(3))
print(f'Total Visitor Records: {len(df):,}\n')

# Standardize column headers to lowercase
df.columns = df.columns.str.strip().str.lower()

# 2. Formulate Hypotheses
print('--- 2. Formal Hypotheses ---')
print(
    'Null Hypothesis (H0): p_A = p_B (No significant difference in conversion'
    ' rates between Variant A and Variant B).'
)
print(
    'Alternative Hypothesis (H1): p_A != p_B (Significant difference in'
    ' conversion rates between Variant A and Variant B).\n'
)

# 3. Calculate Sample Sizes & Conversion Rates
# Convert binary text/flag to numeric (1 for conversion, 0 for no conversion)
df['converted_numeric'] = df['converted'].apply(
    lambda x: 1 if str(x).strip().lower() in ['yes', 'true', '1'] else 0
)

summary = (
    df.groupby('variant')
    .agg(
        total_visitors=('visitorid', 'count'),
        conversions=('converted_numeric', 'sum'),
        total_revenue=('ordervalueinr', 'sum'),
    )
    .reset_index()
)

summary['conversion_rate_%'] = (
    summary['conversions'] / summary['total_visitors']
) * 100
print('--- 3. Performance Summary by Variant ---')
print(summary.to_string(index=False))
print()

# 4. Perform Two-Sample Z-Test for Proportions
control = df[df['variant'].str.upper() == 'A']
treatment = df[df['variant'].str.upper() == 'B']

successes = [
    control['converted_numeric'].sum(),
    treatment['converted_numeric'].sum(),
]
nobs = [len(control), len(treatment)]

z_stat, p_value = proportions_ztest(successes, nobs)

print('--- 4. Statistical Test Results (Two-Sample Z-Test) ---')
print(f'Z-Statistic: {z_stat:.4f}')
print(f'P-Value:     {p_value:.4f}')

alpha = 0.05
if p_value < alpha:
  print(
      'Conclusion:  Reject Null Hypothesis (H0). The conversion lift is'
      ' statistically significant!'
  )
else:
  print(
      'Conclusion:  Fail to Reject Null Hypothesis (H0). The observed'
      ' difference is not statistically significant.'
  )

# 5. Calculate Confidence Interval of Difference
p_a = control['converted_numeric'].mean()
p_b = treatment['converted_numeric'].mean()
se_diff = np.sqrt(
    (p_a * (1 - p_a) / len(control)) + (p_b * (1 - p_b) / len(treatment))
)

ci_low = (p_b - p_a) - 1.96 * se_diff
ci_high = (p_b - p_a) + 1.96 * se_diff

print('\n--- 5. Effect Size & Confidence Interval ---')
print(f'Absolute Rate Difference (B - A): {((p_b - p_a) * 100):.2f}%')
print(
    f'95% Confidence Interval of Difference:'
    f' [{ci_low * 100:.2f}%, {ci_high * 100:.2f}%]'
)