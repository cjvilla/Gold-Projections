# Gold-Projections

# Project Background

In 2020, the average closing price of Gold on the US Stock market was $1,773.73. Compared to June of 1971, when Gold was averaging $248.53, that's an increase of 613%! But... why?

Throughout the project, all reference to Gold prices are based on 24k / per oz.

Does the price of Gold see an impact from Inflation Rate fluxuation? The change in the US Dollar index? Is there impact from the exchange rate of other currencies? In this project, our group set out to understand what (if any) correlation these factors had with each other.

The major factors we chose to use when analyzing correlation of historical (and future) Gold prices were Inflation Rates, and the US Dollar Index. For background, those can be defined as:

US Dollar Index

The US Dollar Index is used to measure the value of the dollar against a basket of six world currencies - Euro, Swiss Franc, Japanese Yen, Canadian dollar, British pound, and Swedish Krona.
The index was established shortly after the Bretton Woods Agreement dissolved in 1973 with a base of 100, and values since then are relative to this base.
The value of the index is fair indication of the dollar’s value in global markets.
Historical Inflation Rates

The inflation rate is the percentage increase or decrease in prices during a specified period, usually a month or a year. The percentage tells you how quickly prices rose during the period. For example, if the inflation rate for a gallon of gas is 2% per year, then gas prices will be 2% higher next year.
The inflation rate is a critical component of the misery index, which is an economic indicator that helps to determine an average citizen's financial health.
The most common is demand-pull inflation. That's when demand outpaces supply for goods or services. Buyers want the product so much that they're willing to pay higher prices.

# Database

We chose to use an AWS RDS Database (Postgres build) paired with AWS S3 Buckets for our data.

We created a Bucket in AWS to hold our raw data, and used Postgres to manipulate, merge, and process the data. From Postgres, data was loaded into Jupyter Notebooks to run our Machine Learning code.

In Postgres, we first standardized the data files to ensure data was formatted correctly (headers were the same, data types were the same, etc). From there, we merged the Gold Prices, Inflation Data, and US Dollar index by Month & Year to create a final data set we could feed into our Machine Learning code.

We ran into small hiccups when processing the Year and Month data in Postgres, especially as some data was daily and others were by Year / Month, but we were able to use our knowledge of data groups to process the information.


# Hosting Service

We chose to use an AWS EC2 to host our website, to create a public IP that could be accessed from anywhere and by anyone.

We chose to host using Ubuntu / Flask within the EC2 instance as a way to display out information.

We ran into issues when deploying the Flask app into EC2, especially around installing and managing the proper requirements for hosting on EC2. Working with the security groups, key pairings, and Ubuntu / linux commands were not something we spent a ton of time on in class, but through reserach and help from our instructor and TA's we were able to successfully host the EC2 intance to share our data.

# Machine Learning

After several courses of analysis, we decided to use the Long Short-Term Memory (LSTM) Neural Network to analyze Gold Prices against Inflation and the US Dollar Index to try and predict Gold Prices through 2030. We also chose to review how the Random Forest Regressor presented data as well.


# Additional Skills
Outside of Amazon AWS, Postgres, and Machine Learning networks, we also utilized several other skills / applications to generate our analysis.

They are:
<ul>
<li>Python & Pandas were used to code the Machine Learning Neural Networks, as seen in the links above.</li>
<li>Tableau was used to generate our final analysis (see Analysis tab)</li>
<li>HTML / CSS / Bootstrap was used to code this website</li>
<li>Matplotlib was used to generate graph views within the Collab notesbooks, prior to exporting into Tableau</li>
<ul>
