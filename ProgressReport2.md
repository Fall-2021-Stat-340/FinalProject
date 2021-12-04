# STAT 340 Progress Report II
Names/NetID:

-	Justin Chan: jachan
-	Tambre Hu: thu53
-	Oat Sukcharoenyingyong: sukcharoenyi
-	James Ma: yma255
-	Shawn Riemer: seriemer


## Data Set & Statistical Questions
> A description of your data set and a summary of your statistical question(s) of interest (you may copy-paste this from your proposal, if you wish). 
This dataset is a comprehensive collection of indicators of economic development for every country that is collected by the World bank. We think this dataset is good because it is a rich dataset so there would be plenty of interesting patterns to find. Also, the conclusions will be grounded in measures of economic development (i.e. "Adolescent fertility rate negatively correlates with GDP"). Since the dataset is so thorough, we can find both simple and complex patterns (using a wide range of techniques). The specific statistical questions that we are aiming to explore and answer throughout our research are as follows:

1.	What indicators have the greatest impact on economic stability?
2.	How do those indicators relate to each other?
3.	How do those relationships differ between countries, and is there a cluster structure present? (i.e. developed countries and developing countries)

The corresponding hypotheses that we will test are as follows:
1. 	Indicators in the World Bank dataset have no relationship to GDP per capita.
2. 	Indicators in the World Bank dataset do not correlate with each other. 
3. 	There is no clear cluster structure present in the dataset that groups countries together.

## World Bank Dataset
> A brief description of why your group found this data set in particular to be of interest and why your reader should care. 

There is so much data available in this dataset that has major significance in the real world: data about health, wealth, energy use and more. Obviously these metrics differ significantly between different countries and regions in the world, but we were curious to see if we could uncover the relationships. It is important to understand why the citizens of one country have more wealth than another, or why some countries have restricted internet access. While we cannot expect to completely solve these questions, as so much goes into them, this data can highlight the main driving forces of those inequalities. 

## Variables
> A description of the variables available in your data set, with more details for the variables that are likely to be relevant to your question (you may copy-paste this from your proposal, if you wish). 

With over 700 total features there are too many to name them all, but some stand out. Gross Domestic Product (GDP) is a particularly interesting feature, as a country’s economic growth, success, and stability impact so many decisions worldwide. It will be insightful to both predict a country’s GDP based on its other characteristics, such as health outcomes, technological advancement, and more. There are 18 different versions of GDP that we have access to, including GDP per capita, GDP per person employed, and GDP growth (annual %). To simplify our analysis, we will be using just the GDP per capita in US$, (code: NY.GDP.PCAP.CD).

There are many metrics that we will explore. For example, Health is one category of features that we will look at. Some of them include Age dependency ratio (% of working-age population), Adolescent fertility rate (births per 1,000 women ages 15-19), and Birth rate, crude (per 1,000 people). These columns will be analyzed to determine their effect on economic stability.

Other intriguing indicators include energy use. Numerous different versions of it are included, among them Fossil fuel energy consumption, Energy use per capita, and CO2 emissions (metric tons per capita). As electricity consumption rises across the globe, we can investigate how different countries are managing those changes and see if energy use correlates with other important indicators. All of the mentioned features will be useful in identifying patterns and clusters when it comes to a country’s health and prosperity.

## Loading Dataset
> A block of code showing how to load the data into R (if your data set is too large to permit this, please speak to us promptly). 

The zip file available for the dataset on Kaggle contains more files than necessary. For our analysis we are working with the Indicators.csv file, which we loaded in and formatted as shown below.

```{r}
country <- read_csv("data/Country.csv", col_types = cols())
ind <- read_csv("data/Indicators.csv", col_types = cols())

names <- read_tsv("world-country-names.tsv")
data_names <- names$name
ind_names <- ind$CountryName %>% unique()
overlap_names <- intersect(ind_names, data_names)
overlap_names %>% length()

ind <- ind %>% 
  mutate(
    IndicatorName = str_replace_all(IndicatorName, " ", "_")
  ) 
ind <- ind %>% filter(
    CountryName != "Channel Islands" # remove bc it has an entire missing year
  ) %>% filter(
    CountryName %in% overlap_names
  )

# pivot wider to add missing values
ind2 <- ind %>%
  select(CountryName, IndicatorName, Year, Value) %>%
  pivot_wider(names_from = IndicatorName,
              values_from = Value,
              values_fill = NA)
)
```

## Plot
> At least one plot summarizing some aspect of the data set that is interesting to you and your group. Your plot should be well-labeled, have an appropriate title, and your document should include a reasonably detailed description of what the plot shows as well as any discussion/interpretation of the contents of the plot (e.g., if the plot shows a clear trend in your data, discuss that trend, why it is or isn’t surprising, etc.).

Talk about plot


<div align="center">
	<img width="45%" src="https://user-images.githubusercontent.com/44740178/144689997-715b705e-f077-4c7e-863a-ad44b6129dc9.png"></img>
	<img width="45%" src="https://user-images.githubusercontent.com/44740178/144690011-505ae1d7-3320-4cf1-b14b-f61fe6d8a263.png"></img>
</div>

## Progress & Challenges Faced
> A brief discussion of the progress and/or challenges faced so far in answering your statistical question(s) of interest. This may include a discussion of the methods and models used; issues that arose when downloading and cleaning the data; shortcomings of the methods/models used so far, etc. 

### Missing Data
In the last progress report we mentioned that we had to deal with a large amount of missing data. Figuring out how to deal with the missing data ended up being much more of a challenge than we initially anticipated. When the dataset is pivoted wider to include columns for every combination of year and indicator, 68.7% of the data is missing. Additionally, no country was missing less than 50% of its total data. We spent a considerable amount of time trying various ways to whittle our dataset down by country and indicators to minimize the amount of missing data while maximizing the number of countries and indicators that remained.

Our approach to deal with this trade-off between countries, indicators, and missing data was an iterative process. Ultimately what we settled on is described here. We first removed non-official countries (such as Sint Maarten (Dutch part)) which took us from 247 countries to 183. This step was done by looking for overlap with the world-country-names.tsv file. Channel Islands was also removed because it was missing an entire year of data, giving us 182 countries.

We then looked at columns and removed indicators that were missing at least 50% of its data. This step took us down to 651 remaining indicators. Next, we looked at each country and removed any country missing over 70% of data from the remaining columns, leaving us with 107 countries. These countries still include a good combination of both developed and developing countries, so our analysis will not be majorly hampered by the countries we are no longer analyzing. The last step was to only keep indicators with at least 90% of the data for the remaining countries. This step left us with 140 final indicators.

There is still missing data in our dataset, so we must use imputation to fill it in. This was done by taking the median of all data for a particular column. We didn't think it was unreasonable to do this, especially since the median makes sense on all of our indicators. A country's infant mortality rate for a year, for example, if missing, would be filled in with the median of all the years we analyze (1960-2015). We decided against using the mean due to the impact of outliers - if a severe disease outbreak during a certain year increased infant mortality, we don't want that to have a high impact on all the years we have missing data for infant mortality.

### Statistical Methods
To answer our first statistical question, we will use the `GDP_per_capita_(current_US$)` column as the measure of economic stability. Every unique year and indicator combination will be a feature used for prediction, with each record being a country. We are still planning to use model fitting to find column’s coefficients and PCA to simplify our model. These methods will tell us the most important indicators.

--- maybe remove this whole part?---
Our second question can be answered by regressing our predictors on each other. We can see if they are correlated with each other or not, and if so, whether or not they all predict our response variable (`GDP_per_capita_(current_US$)`). For that, we can pick out individual predictors and assess how well they predict our response variable and compare those performances to when all predictors are used. This can allow us to eliminate predictors that don't correlate well with our response and are only correlated with other predictors that do predict our response. PCA can also be used here to further simplify our models by finding the most important component directions.

For our first hypothesis, we first fit a linear regression model to predict GDP per capita using all the first five principal components, achieving a multiple R-squared score of 0.7297 and an adjusted R-squared value of 0.7164. We plan to use k-fold cross validation to evaluate our model on unseen data. We also plan to try using regularization (i.e. ridge regression or LASSO) to pick features that best predict our GDP per capita response variable and reduce overfitting. For this part, we are also thinking of using cross validation to choose the optimal alpha value (tuning parameter). Furthermore, we are interested to see if any interaction effects exist between our predictors, and if adding interaction terms will improve our model outcome.


For our third hypothesis, we performed clustering on the major principal components in order to group countries together. There are a couple of approaches we took to accomplish this that may introduce problems later on. First, recall that for every country and every indicator, we have a value for a number of years (1960-2015). Thus, when we clustered on this data set, each data point represented a country-year combination projected onto the first two principal components. It would be difficult to interpret what this cluster structure meant, and our original plan was to cluster based on countries, so we can look at groups of countries, and explain what makes these groups different from one another. Our solution to this was: for every country, we made its value for a specific indicator the average of all indicator values for that country over all the years. Doing this allowed us to cluster based on countries, as we eliminated the "year" dimension, and our data frame now has a row for each country and a column for an indicator. The obvious drawback to this is that we have now lost information in our data related to time (i.e. how a country's manufacturing changed over the years), as we are summmarzing over all years. Our current plan to address this is to use pivot-wider so our columns represent a combination of indicator and year. We would then cluster countries for certain years (i.e. the first year of each decade) or all and observe how our clusters change over time, if they do.

Our second challenge was deciding how many cluster centers to use for k-means. We arbitrarily picked 3, but realize that there is a more systematic/algorithmic way of doing this. We are currently trying to use hierarchical clustering so we can more easily identify the most natural number of clusters that exist in our data.

## Next Steps
> A summary of your next steps (e.g., your goals for the remainder of November, other methods/models you want to try, etc.).


These are the goals we would like to achieve by the listed dates in December.

- 12/10: Finish implementing, evaluating, and interpreting the results of our model (interaction terms, regularization, cross-valudidation), allowing us to test hypothesis 1. To answer hypothesis 2, we will filter our correlation matrix on our chosen indicators. Lastly, we will perform clustering for each year, instead of a summary of all years. We will aim to create clustering graphics to answer hypothesis 3.

- 12/17: Finalize report and presentation, rehearse, and make last-minute changes.

