# P3: Analyze A/B Test Results
## Overview
In this project, I demonstrated a A/B Test for a e-commerce company's website to decide whether they should implement their new page or keep the old page. Using the data with groups of control, treatment and their conversion, I performed the two-tailed hypothesis test and regression approach to determine results. The technique was primary using Python and I used the Boostrate Sampling method to perform the hypothesis test. Besides, I also demonstrated z-test to compare the results. The regression method was Logit Regression, and the goal was to see if there is a significant difference in conversion based on which page a customer receives.

The whole procedure included three parts:
- Probability: Taking a look on the data set and doing some simple data clearing, finding descriptive statistics to make sure the conversion rates for both group are on the same basis. 

- A/B Test: Stating hypothesis for the website changing decision. Then finding out the necessary statistics for the test by calculating the difference between two groups of conversion rates. Then using Boostrate Sampling method to simulate 10,000 statistic to form a sampling distribution. Then compared the sample statistic I observed to the simulated sampling distribution and find p-valued. I also performed a z-scored test under the assumption that the simulated difference of converted rate has normally distribution.
- Regression approach: I demonstrated a logistic regression to find out whether old/new page type have significant linear relationship with the converted choice. Besides, I also added the country variable to see if country had an impact on conversion. Finally, I added the interaction term between page and country variable to see whether the interaction has significant effects on conversion.

## Results
In A/B Test, with the high p-value 0.9, we do not have evidence to reject the null. It concludes that there is no evidence that new page bring more convert rate for user. In z-test, I got the same result---no significant difference.

In regression approach, the result showed the old/new page type have no significant linear relationship with the converted choice.
And after adding the country variable to see if country had an impact on conversion. The result turned out that country of users are not associated with changes in the convert decision. Finally, I added the interaction term between page and country variable, and the result showed the interaction between page and country have no significant effects on conversion.

## License
[MIT License](https://github.com/onpillow/Udacity-DAND-Term1/blob/master/p3/LICENSE)
