# FinalProject

## Comment

Your statistical questions are WAY too broad here. Pick one question, and perhaps even focus it to one small set of variables. "Are there any interesting correlations between variables" is not a helpful statistical question. Try phrasing your questions as specific questions about specific variables and their relationships, or even as null hypotheses to be tested. You were asked, as part of the assignment, to select a few variables that are likely relevant to your project. Your broad questions meant that you couldn't really do this. You questions about indicators of economic stability are perhaps a good starting direction. There is a variable/model selection problem here, especially because the number of predictors is not that much smaller than the number of observations (~120 predictors, ~200 countries). These tools are the topic of our next few lectures, conveniently.

We are not sure that you have fully explored your data-- the documentation on Kaggle suggests that there are far more indicators than you state (1000s of indicators, per Kaggle?). The lack of specificity in your writeup makes it hard to give you full credit, sadly.

Keith Levin, Nov 4 at 2:02pm

# Proposals

This Readme.md file is our proposal.

Instructions: https://kdlevin-uwstat.github.io/STAT340-Fall2021/projects/STAT340_proposal_instructions.pdf

## James Dataset Proposal: (Voted for by: Avery)
URL: https://www.kaggle.com/imakash3011/customer-personality-analysis

This is a dataset with consumer information such as what they buy and their demographics. Columns are roughly divided into two categories: customer characteristics (age, marital status, etc.) and the products they purchse (meat, wine, etc.) This could be an interesting dataset to explore if we want to analyze consumer behavior. There is a wide variety of methods we could use to discover patterns: clustering, regression, and other methods of exploratory data analysis. This dataset has a usability score of 9.7 and is pretty large (29 columns, 2240 rows).

## Tambre Dataset Propsal: (Voted for by: )

URL: https://www.kaggle.com/imdevskp/corona-virus-report

This dataset is about COVID in a geographical and temporal context. There are features like confirmed, deaths, recovered, etc. by country and day. It has a lot of observations and a usabillity score of 10/10 on Kaggle.

## Avery Dataset Proposal: (Voted for by: Oat, James, Shawn)

URL: https://www.kaggle.com/kaggle/world-development-indicators

> The World Development Indicators from the World Bank contain over a thousand annual indicators of economic development from hundreds of countries around the world.

This dataset has 118 columns for each country (so ~200 rows). There are a lot of interesting colums such as:

- SystemOfNationalAccounts (economic activity)
- Adolescent fertility rate (births per 1,000 women ages 15-19)
- Age dependency ratio (% of working-age population)
- Birth rate, crude (per 1,000 people)
- CO2 emissions (metric tons per capita)

I think this would be a good choice because it is a rich dataset so there would be plenty of interesting patterns to find. Also, the conclusions would be grounded in measures of economic development (i.e. "Adolescent fertility rate negatively correlates with GDP"). Since the dataset is so rich we could find both simple and complex patterns (to use more advanced techniques).

This might be a bad choice because it is so large. I expect we would need to do a lot of data exploration and possibly some cleaning.

## Shawn Dataset Proposal: (Voted for by: Oat)

URL: https://www.kaggle.com/harlfoxem/housesalesprediction

This dataset includes house sales in King County, Washington. It has 21 columns including features like # of bedrooms, # of bathrooms, sqare footage, and the price that the house sold for. The topic is a little unoriginal but it would be easy to analyze and make predictions on.
