# Checkout Experience A/B Testing & Hypothesis Testing Analysis

## 📌 Executive Summary
This project evaluates visitor checkout conversions comparing **Variant A (Control)** against **Variant B (Treatment)** using statistical hypothesis testing (Two-Sample Z-Test for Proportions) to determine whether design changes drive a statistically significant increase in conversions[cite: 4].

---

## 📋 1. Hypothesis Formulation
* **Null Hypothesis ($H_0$):** $p_A = p_B$ (There is no true difference in conversion rates between Variant A and Variant B).
* **Alternative Hypothesis ($H_1$):** $p_A \neq p_B$ (There is a significant difference in conversion rates between variants).
* **Significance Level ($\alpha$):** $0.05$ (95% Confidence Level).

---

## 📊 2. Experimental Results Summary
* **Control Cohort (Variant A):** 600 visitors | 57 conversions | **9.50% Conversion Rate**
* **Treatment Cohort (Variant B):** 600 visitors | 71 conversions | **11.83% Conversion Rate**
* **Absolute Conversion Lift:** **+2.33%**
* **Test Statistics:**
  * **Z-Statistic:** `-1.3092`
  * **P-Value:** `0.1905`
  * **95% Confidence Interval for Lift:** `[-1.16%, +5.83%]`

---

## 📝 3. Executive Decision Memo
* **Statistical Finding:** Because the p-value ($0.1905$) is greater than $\alpha = 0.05$, we **fail to reject the Null Hypothesis ($H_0$)**. The $95\%$ confidence interval includes $0\%$, indicating that the positive lift could be attributed to random variation.
* **Final Recommendation:** **Keep Control / Extend Testing Period.**
* **Business Justification:** While Variant B demonstrates positive directional growth ($11.83\%$ vs $9.50\%$), current statistical power is insufficient to guarantee long-term lift. It is recommended to collect additional visitor samples to reach statistical significance before committing to a full production rollout.