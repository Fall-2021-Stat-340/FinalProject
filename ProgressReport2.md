> The names and NetIDs of all group members. 

Names/NetID:

-	Justin Chan: jachan
-	Tambre Hu: thu53
-	Oat Sukcharoenyingyong: sukcharoenyi
-	James Ma: yma255
-	Shawn Riemer: seriemer

> A description of your data set and a summary of your statistical question(s) of interest (you may copy-paste this from your proposal, if you wish). 

This dataset is a comprehensive collection of indicators of economic development for every country that is collected by the World bank. We think this dataset is good because it is a rich dataset so there would be plenty of interesting patterns to find. Also, the conclusions will be grounded in measures of economic development (i.e. "Adolescent fertility rate negatively correlates with GDP"). Since the dataset is so thorough, we can find both simple and complex patterns (using a wide range of techniques). The specific statistical questions that we are aiming to explore and answer throughout our research are as follows:

1.	What indicators have the greatest impact on economic stability?
2.	How do those indicators relate to each other?
3.	How do those trends differ between a developed country, the United States, and a developing country, Mexico?
4.	Based on the relationships we found between the United States and Mexico, how could we extend our analysis to other countries and regions of the world?

> A brief description of why your group found this data set in particular to be of interest and why your reader should care. 

There is so much data available in this dataset that has major significance in the real world: data about health, wealth, energy use and more. Obviously these metrics differ significantly between different countries and regions in the world, but we were curious to see if we could uncover the relationships. It is important to understand why the citizens of one country have more wealth than another, or why some countries have restricted internet access. While we cannot expect to completely solve these questions, as so much goes into them, this data can highlight the main driving forces of those inequalities. 

> A description of the variables available in your data set, with more details for the variables that are likely to be relevant to your question (you may copy-paste this from your proposal, if you wish). 

With over 700 total features there are too many to name them all, but some stand out. Gross Domestic Product (GDP) is a particularly interesting feature, as a country’s economic growth, success, and stability impact so many decisions worldwide. It will be insightful to both predict a country’s GDP based on its other characteristics, as well as finding the impact GDP per capita has on health and other outcomes of the country’s citizens. There are 18 different versions of GDP that we have access to, including GDP per capita, GDP per person employed, and GDP growth (annual %). To simplify our analysis, we will be using just the GDP per capita in US$, (code: NY.GDP.PCAP.CD).

Health metrics are another category of features that we will explore. Among them we will use Age dependency ratio (% of working-age population), Adolescent fertility rate (births per 1,000 women ages 15-19), and Birth rate, crude (per 1,000 people). These columns will be analyzed to determine their effect on economic stability.

Other intriguing indicators include energy use. Numerous different versions of it are included, among them Fossil fuel energy consumption, Energy use per capita, and CO2 emissions (metric tons per capita). As electricity consumption rises across the globe, we can investigate how different countries are managing those changes and see if energy use correlates with other important indicators. Al of the mentioned features will be useful in identifying patterns and clusters when it comes to a country’s health and prosperity.

> A block of code showing how to load the data into R (if your data set is too large to permit this, please speak to us promptly). 

The zip file available for the dataset on Kaggle contains more files than necessary. For our analysis we are working with the Indicators.csv file, which we loaded in and formatted as shown below.

```{r}
ind <- read.csv("data/Indicators.csv")
mex <- ind %>% filter(CountryName == "Mexico")
mex_ <- mex %>% group_by(IndicatorCode) %>% 
  summarise(
    n = n(),
    CountryName,
    Year,
    IndicatorCode,
    IndicatorName = str_replace_all(IndicatorName, " ", "_"),
    Value
  ) %>% filter(n > 50) %>% ungroup()
mex2 <- mex_ %>% select(CountryName, Year, IndicatorCode, Value) %>%
pivot_wider(
  names_from = IndicatorCode,
  values_from = Value,
  values_fill = 0
)
```

> At least one plot summarizing some aspect of the data set that is interesting to you and your group. Your plot should be well-labeled, have an appropriate title, and your document should include a reasonably detailed description of what the plot shows as well as any discussion/interpretation of the contents of the plot (e.g., if the plot shows a clear trend in your data, discuss that trend, why it is or isn’t surprising, etc.).

Talk about plot

<div align="center">
	<img width="45%" src="https://user-images.githubusercontent.com/53503018/141596183-3dde91c0-2082-4b25-a088-683a8b701a40.png"></img>
	<img width="45%" src="https://user-images.githubusercontent.com/53503018/141595932-960c7362-6bfa-4265-875f-dc1a844edcbf.png"></img>
	<p>US on the left and Mexico on the right</p>
</div>

For ease of coding we labeled the plots with `Indicator Code` instead of `Indicator Name`. Here is the mapping from `Indicator Code` to `Indicator Name`:

| Code | Name |
|-|-|
| AG.LND.ARBL.HA.PC  |  Arable land (hectares per person) |
| EN.URB.MCTY  |  Population in urban agglomerations of more than 1 million |
| NE.IMP.GNFS.ZS  |  Imports of goods and services (% of GDP) |
| NY.GSR.NFCY.CD  |  Net income from abroad (current US$) |
| NE.TRD.GNFS.ZS  |  Trade (% of GDP) |
| SP.POP.TOTL  |  Population, total |
| TG.VAL.TOTL.GD.ZS  |  Merchandise trade (% of GDP) |
| NY.TAX.NIND.CN  |  Net taxes on products (current LCU) |
| EN.POP.DNST  |  Population density (people per sq. km of land area) |
| FI.RES.TOTL.CD  |  Total reserves (includes gold, current US$) |
| SP.POP.65UP.TO.ZS  |  Population ages 65 and above (% of total) |

> A brief discussion of the progress and/or challenges faced so far in answering your statistical question(s) of interest. This may include a discussion of the methods and models used; issues that arose when downloading and cleaning the data; shortcomings of the methods/models used so far, etc. 

In the last progress report we mentioned that we had to deal with a large amount of missing data. Figuring out how to deal with the missing data ended up being much more of a challenge than we initially imagined. When the dataset is pivoted wider to include columns for every combination of year and indicator, 68.7% of the data is missing. Additionally, no country was missing less than 50% of its total data. We spend a considerable amount of time trying various ways to whittle our dataset down by country and indicators to minimize the amount of missing data while maximizing the number of countries and indicators that remained.

Our approach to deal with this trade-off between countries, indicators, and missing data was an iterative process. Ultimately what we settled on is described here. We first removed non-official countries (such as Sint Maarten (Dutch part)) which took us from 247 countries to 183. This step was done by looking for overlap with the world-country-names.tsv file. Channel Islands was also removed because it was missing an entire year of data, giving us 182 countries.

We then looked at columns and removed indicators that were missing at least 50% of its data. This step took us down to 651 remaining indicators. Next, we looked at each country and removed any country missing over 70% of data from the remaining columns, leaving us with 107 countries. These countries still include a good combination of both developed and developing countries, so our analysis will not be majorly hampered by the countries we are no longer analyzing. The last step was to only keep indicators with at least 90% of the data for the remaining countries. This step left us with 140 final indicators.

There is still missing data in our dataset, so we must use imputation to fill it in. This was done using…..

To answer our first statistical question, we will use the `GDP_per_capita_(current_US$)` column as the measure of economic stability. Every unique year and indicator combination will be a feature used for prediction, with each record being a country. We are still planning to use model fitting to find column’s coefficients and PCA to simplify our model. These methods will tell us the most important indicators.

Our second question can be answered by regressing our predictors on each other. We can see if they are correlated with each other or not, and if so, whether or not they all predict our response variable (`GDP_per_capita_(current_US$)`). For that, we can pick out individual predictors and assess how well they predict our response variable and compare those performances to when all predictors are used. This can allow us to eliminate predictors that don't correlate well with our response and are only correlated with other predictors that do predict our response. PCA can also be used here to further simplify our models by finding the most important component directions.
Hypothesis testing will be a useful tool for evaluating the differences between the United States and Mexico. Our null hypotheses will be that there is no difference between how certain features impacts economic stability.

For our fourth question we hope to do k-means clustering of the other countries using the indicators we found were important in our analysis between the United States and Mexico. 

> A summary of your next steps (e.g., your goals for the remainder of November, other methods/models you want to try, etc.).

To figure out what indicators impact economic stability, we will use a couple different approaches. First, we can use correlation matrices to visualize the most important features. Then, we can use model fitting to determine the associated coefficients of each feature when predicting GDP. We can experiment with various models (i.e. linear, quadratic) and evaluate the fit/complexity tradeoff between those models. PCA can be used to simplify our models.

Our second question can be answered by regressing our predictors on each other. We can see if they are correlated with each other or not, and if so, whether or not they all predict our response variable (GDP). For that, we can pick out individual predictors and assess how well they predict our response variable, and compare those performances to when all predictors are used. This can allow us to eliminate predictors that don't correlate well with our response and are only correlated with other predictors that do predict our response. PCA can also be used here to further simplify our models by finding the most important component directions.

Hypothesis testing will be a useful tool for evaluating the differences between the United States and Mexico. Our null hypotheses will be that there is no difference between how certain features impacts economic stability. 

For our fourth question we hope to do k-means clustering of the other countries using the indicators we found were important in our analysis between the United States and Mexico.

These are the goals we would like to achieve by the listed dates in December.

- 12/XX: Decide on and create the necessary plots and graphs for each of the models/methods we chose to use. Based on the results we found in comparing the results from the US and Mexico, make any necessary adjustments to the models/methods we chose to use to analyze the data. Once we understand the results of our findings, we will begin exploring how these results can be duplicated onto other countries.


- 12/XX: After finalizing our data and analysis, we will elaborate on said results and communicate our findings. We will then begin fleshing out our report and making it cohesive so that it effectively shows the significant findings of each of our statistical questions. 
	 

- 12/XX: Finalize report.
