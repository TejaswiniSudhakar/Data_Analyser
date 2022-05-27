# Data_Analyser
Data Analyser is an open source data visualization 
web app which can also give automatic visualizations, created using Streamlit,
This visualizer is easy to use and its property of giving automatic visualization 
based on user query is one of its kind, therefore, this can help the Automotive Industry, 
to harness data to take informed decisions.
<br>

<hr>

This visualization web app has a bundle of features
1. VISUALIZER - Visualise various parameters of the dataset
2. DASHBOARD - Compare two different visualizations together based on same attributes
3. QUERY SOLVER - Write a query and get an appropriate visualization
 <br>
 
 In its current state, Data Analyser can be used to create: <br>
 1) Scatterplots
 2) Lineplots
 3) Histogram
 4) Boxplot
 5) Violin plots. <br>
 6) Sunburst
 7) Tree maps
 8) Pie Charts. <br>
 9) Density contour
 10) Density heatmaps
 11) Area charts
 12) Bar charts
 

# How to run the app
1. Clone this repo.
2. Install all requirements using: <br> ```pip install -r requirements.txt``` <br> 
3. From the terminal within the directory: <br> ```streamlit run app.py```

<br>

# Dataset
The vehicle dataset is used here has, 15 columns and 1000 rows.
The dataset consists of the following datatypes:
1. Make - Qualitative Nominal (Categorical)
2. Model - Qualitative Nominal (Categorical)
3. Year - Quantitative Continuous (Interval)
4. Engine - Qualitative Ordinal
5. Hp - Quantitative Discrete
6. Cylinders - Quantitative Discrete
7. Transmission - Qualitative Ordinal
8. Driven - Qualitative Nominal (Categorical)
9. Doors - Quantitative Discrete
10. Size - Qualitative Ordinal
11. Style - Qualitative Nominal (Categorical)
12. Hgmpg - Quantitative Discrete
13. Ctmpg - Quantitative Discrete
14. Popularity - Quantitative Discrete
15. Msrp - Quantitative Discrete

