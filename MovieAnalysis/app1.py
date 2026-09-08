
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os



# =========================================================
# TITLE
# =========================================================

st.title("🎬 IMDB Movie Data Analysis")
st.subheader("Data Analysis Using Python & Streamlit")


# =========================================================
# UPLOAD DATASET
# =========================================================




if True:

    # Read CSV
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(BASE_DIR, "IMDB-Movie-Data.csv")

    data = pd.read_csv(csv_path)

    

    
# =========================================================
# MOVIE SEARCH / MOVIE INFORMATION
# =========================================================

    st.header("🎬 Search Information About a Particular Movie")


# ---------------------------------------------------------
# SELECT MOVIE
# ---------------------------------------------------------

    movie_list = data["Title"].dropna().sort_values().unique()

    selected_movie = st.selectbox(
    "Select a Movie",
    movie_list
)


# ---------------------------------------------------------
# GET SELECTED MOVIE
# ---------------------------------------------------------

    movie_data = data[
        data["Title"] == selected_movie
    ]


# ---------------------------------------------------------
# SELECT COLUMN
# ---------------------------------------------------------

    st.subheader("Select Information You Want To See")

    selected_column = st.selectbox(
        "What information do you want?",
        data.columns
    )


# ---------------------------------------------------------
# DISPLAY SELECTED COLUMN VALUE
# ---------------------------------------------------------

    if selected_column:

        value = movie_data.iloc[0][selected_column]

        st.write(
            f"### {selected_column}"
        )

        st.success(
            str(value)
        )


# ---------------------------------------------------------
# DISPLAY ALL INFORMATION
# ---------------------------------------------------------

    st.subheader("📋 Complete Information About The Movie")

    if st.checkbox("Show All Information"):

    # Convert row into a DataFrame
        movie_info = movie_data.iloc[0]

        for column in data.columns:

            st.write(
                f"**{column}:**"
            )

            st.write(
                movie_info[column]
            )

            st.divider()


    # =====================================================
    # 1. PREVIEW DATASET
    # =====================================================

    st.header("1. Preview Dataset")

    preview = st.selectbox(
            "Choose what you want to see",
            ["Select", "Head", "Tail"]
        )

    if preview == "Head":

        st.write(data.head())

    elif preview == "Tail":

        st.write(data.tail())


    # =====================================================
    # 2. DATATYPE OF EACH COLUMN
    # =====================================================

    st.header("2. DataType of Each Column")

    if st.checkbox("Show Data Types"):

        st.write(data.dtypes)


    # =====================================================
    # 3. SHAPE OF DATASET
    # =====================================================

    st.header("3. Shape of Dataset")

    dimension = st.radio(
        "What Dimension Do You Want To Check?",
        ["Rows", "Columns"]
    )

    if dimension == "Rows":

        st.write(
            "Number of Rows:",
            data.shape[0]
        )

    elif dimension == "Columns":

        st.write(
            "Number of Columns:",
            data.shape[1]
        )


    # =====================================================
    # 4. NULL VALUES
    # =====================================================

    st.header("4. Missing Values")

    null_count = data.isnull().sum()

    st.write(null_count)

    if data.isnull().values.any():

        st.warning(
            "This Dataset Contains Missing Values"
        )

        fig, ax = plt.subplots()

        sns.heatmap(
            data.isnull(),
            yticklabels=False,
            cbar=False,
            ax=ax
        )

        ax.set_title("Missing Values")

        st.pyplot(fig)

    else:

        st.success(
            "Congratulations!!! No Missing Values"
        )


    # =====================================================
    # 5. DUPLICATE VALUES
    # =====================================================

    st.header("5. Duplicate Values")

    duplicate_count = data.duplicated().sum()

    st.write(
        "Number of Duplicate Rows:",
        duplicate_count
    )

    if duplicate_count > 0:

        st.warning(
            "This Dataset Contains Duplicate Values"
        )

        remove_duplicate = st.selectbox(
            "Do You Want To Remove Duplicate Values?",
            ["Select One", "Yes", "No"]
        )

        if remove_duplicate == "Yes":

            data = data.drop_duplicates()

            st.success(
                "Duplicate Values Removed"
            )

        elif remove_duplicate == "No":

            st.info(
                "Duplicate Values Were Not Removed"
            )

    else:

        st.success(
            "No Duplicate Values Found"
        )


    # =====================================================
    # 6. OVERALL STATISTICS
    # =====================================================

    st.header("6. Overall Statistics")

    if st.checkbox("Get Overall Statistics About The DataFrame"):

        st.write(
            data.describe(include="all")
        )


    # =====================================================
    # 7. DATASET INFORMATION
    # =====================================================

    st.header("7. Dataset Information")

    if st.checkbox("Show Dataset Information"):

        info_df = pd.DataFrame({
            "Column": data.columns,
            "Data Type": data.dtypes.astype(str),
            "Non-Null Values": data.notnull().sum().values,
            "Null Values": data.isnull().sum().values
        })

        st.write(info_df)


    # =====================================================
    # 8. TOTAL NUMBER OF MOVIES
    # =====================================================

    st.header("8. Total Number of Movies")

    st.metric(
        "Total Movies",
        len(data)
    )


    # =====================================================
    # 9. MOVIES WITH RUNTIME >= 180 MINUTES
    # =====================================================

    st.header(
        "9. Movie Titles Having Runtime Greater Than or Equal To 180 Minutes"
    )

    long_movies = data[
        data["Runtime (Minutes)"] >= 180
    ]

    st.write(
        long_movies[
            [
                "Title",
                "Runtime (Minutes)"
            ]
        ].sort_values(
            by="Runtime (Minutes)",
            ascending=False
        )
    )


    # =====================================================
    # 10. YEAR WITH HIGHEST AVERAGE VOTING
    # =====================================================

    st.header(
        "10. Year With The Highest Average Voting"
    )

    avg_votes_year = (
        data.groupby("Year")["Votes"]
        .mean()
        .sort_values(ascending=False)
    )

    highest_vote_year = avg_votes_year.idxmax()
    highest_vote_average = avg_votes_year.max()

    st.success(
        f"Year: {highest_vote_year}"
    )

    st.write(
        "Highest Average Votes:",
        round(highest_vote_average, 2)
    )

    st.write(
        avg_votes_year
    )


    # =====================================================
    # 11. YEAR WITH HIGHEST AVERAGE REVENUE
    # =====================================================

    st.header(
        "11. Year With The Highest Average Revenue"
    )

    avg_revenue_year = (
        data.groupby("Year")["Revenue (Millions)"]
        .mean()
        .sort_values(ascending=False)
    )

    highest_revenue_year = avg_revenue_year.idxmax()
    highest_revenue_average = avg_revenue_year.max()

    st.success(
        f"Year: {highest_revenue_year}"
    )

    st.write(
        "Highest Average Revenue:",
        round(highest_revenue_average, 2),
        "Million"
    )

    st.write(
        avg_revenue_year
    )


    # =====================================================
    # 12. AVERAGE RATING FOR EACH DIRECTOR
    # =====================================================

    st.header(
        "12. Average Rating For Each Director"
    )

    director_rating = (
        data.groupby("Director")["Rating"]
        .mean()
        .sort_values(ascending=False)
    )

    director_rating_df = director_rating.reset_index()

    director_rating_df.columns = [
        "Director",
        "Average Rating"
    ]

    st.write(
        director_rating_df
    )


    # =====================================================
    # 13. TOP 10 LENGTHY MOVIES
    # =====================================================

    st.header(
        "13. Top 10 Lengthy Movies"
    )

    top_10_lengthy = (
        data.sort_values(
            by="Runtime (Minutes)",
            ascending=False
        )
        .head(10)
    )

    st.write(
        top_10_lengthy[
            [
                "Title",
                "Runtime (Minutes)"
            ]
        ]
    )


    # =====================================================
    # 14. NUMBER OF MOVIES PER YEAR
    # =====================================================

    st.header(
        "14. Display Number of Movies Per Year"
    )

    movies_per_year = (
        data["Year"]
        .value_counts()
        .sort_index()
    )

    st.write(
        movies_per_year
    )

    st.line_chart(
        movies_per_year
    )


    # =====================================================
    # 15. MOST POPULAR MOVIE
    # =====================================================

    st.header(
        "15. Most Popular Movie (Highest Revenue)"
    )

    highest_revenue_index = (
        data["Revenue (Millions)"].idxmax()
    )

    popular_movie = data.loc[
        highest_revenue_index
    ]

    st.success(
        f"Movie: {popular_movie['Title']}"
    )

    st.write(
        "Revenue:",
        popular_movie["Revenue (Millions)"],
        "Million"
    )


    # =====================================================
    # 16. TOP 10 HIGHEST RATED MOVIES
    # =====================================================

    st.header(
        "16. Top 10 Highest Rated Movie Titles And Their Directors"
    )

    top_10_rated = (
        data.sort_values(
            by="Rating",
            ascending=False
        )
        .head(10)
    )

    st.write(
        top_10_rated[
            [
                "Title",
                "Rating",
                "Director"
            ]
        ]
    )


    # =====================================================
    # 17. TOP 10 HIGHEST REVENUE MOVIES
    # =====================================================

    st.header(
        "17. Top 10 Highest Revenue Movie Titles"
    )

    top_10_revenue = (
        data.sort_values(
            by="Revenue (Millions)",
            ascending=False
        )
        .head(10)
    )

    st.write(
        top_10_revenue[
            [
                "Title",
                "Revenue (Millions)"
            ]
        ]
    )


    # =====================================================
    # 18. AVERAGE RATING YEAR WISE
    # =====================================================

    st.header(
        "18. Average Rating Of Movies Year Wise"
    )

    avg_rating_year = (
        data.groupby("Year")["Rating"]
        .mean()
    )

    st.write(
        avg_rating_year
    )

    st.line_chart(
        avg_rating_year
    )


    # =====================================================
    # 19. DOES RATING AFFECT REVENUE?
    # =====================================================

    st.header(
        "19. Does Rating Affect The Revenue?"
    )

    correlation = data[
        [
            "Rating",
            "Revenue (Millions)"
        ]
    ].corr()

    rating_revenue_corr = correlation.loc[
        "Rating",
        "Revenue (Millions)"
    ]

    st.metric(
        "Correlation Between Rating And Revenue",
        round(rating_revenue_corr, 3)
    )

    if rating_revenue_corr > 0:

        st.info(
            "There is a positive relationship between Rating and Revenue."
        )

    elif rating_revenue_corr < 0:

        st.info(
            "There is a negative relationship between Rating and Revenue."
        )

    else:

        st.info(
            "There is no linear relationship between Rating and Revenue."
        )


    # Scatter Plot

    fig, ax = plt.subplots()

    sns.scatterplot(
        data=data,
        x="Rating",
        y="Revenue (Millions)",
        ax=ax
    )

    ax.set_title(
        "Rating vs Revenue"
    )

    st.pyplot(fig)


    # =====================================================
    # 20. CLASSIFY MOVIES BASED ON RATINGS
    # =====================================================

    st.header(
        "20. Classify Movies Based On Ratings"
    )


    def classify_rating(rating):

        if rating >= 7:

            return "Excellent"

        elif rating >= 5:

            return "Good"

        else:

            return "Average"


    data["Rating Category"] = (
        data["Rating"]
        .apply(classify_rating)
    )


    st.write(
        data[
            [
                "Title",
                "Rating",
                "Rating Category"
            ]
        ]
    )


    rating_category_count = (
        data["Rating Category"]
        .value_counts()
    )

    st.write(
        rating_category_count
    )

    st.bar_chart(
        rating_category_count
    )


    # =====================================================
    # 21. COUNT NUMBER OF ACTION MOVIES
    # =====================================================

    st.header(
        "21. Count Number Of Action Movies"
    )

    action_movies = data[
        data["Genre"]
        .str.contains(
            "Action",
            case=False,
            na=False
        )
    ]

    st.metric(
        "Number Of Action Movies",
        len(action_movies)
    )

    if st.checkbox("Show Action Movies"):

        st.write(
            action_movies[
                [
                    "Title",
                    "Genre",
                    "Rating"
                ]
            ]
        )


    # =====================================================
    # 22. UNIQUE VALUES FROM GENRE
    # =====================================================

    st.header(
        "22. Find Unique Values From Genre"
    )


    unique_genres = set()


    for genre in data["Genre"].dropna():

        genres = str(genre).split(",")

        for g in genres:

            unique_genres.add(
                g.strip()
            )


    unique_genres = sorted(
        unique_genres
    )


    st.write(
        "Number Of Unique Genres:",
        len(unique_genres)
    )

    st.write(
        unique_genres
    )


    # =====================================================
    # 23. NUMBER OF FILMS OF EACH GENRE
    # =====================================================

    st.header(
        "23. How Many Films Of Each Genre Were Made?"
    )


    genre_count = {}


    for genre in data["Genre"].dropna():

        genres = str(genre).split(",")

        for g in genres:

            g = g.strip()

            if g in genre_count:

                genre_count[g] += 1

            else:

                genre_count[g] = 1


    genre_df = pd.DataFrame(
        list(genre_count.items()),
        columns=[
            "Genre",
            "Number of Movies"
        ]
    )


    genre_df = genre_df.sort_values(
        by="Number of Movies",
        ascending=False
    )


    st.write(
        genre_df
    )


    st.bar_chart(
        genre_df.set_index("Genre")
    )


    # =====================================================
    # ABOUT
    # =====================================================

    st.header("About App")


    if st.button("About App"):

        st.text(
            "Built With Python, Pandas, Seaborn and Streamlit"
        )

        st.text(
            "IMDB Movie Data Analysis Dashboard"
        )


    # =====================================================
    # BY
    # =====================================================

    if st.checkbox("By"):

        st.success(
            "Puja Sri"
        )
