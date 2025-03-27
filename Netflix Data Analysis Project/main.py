import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

df = pd.read_csv("netflix_titles.csv")
print(df.columns.tolist())
#['show_id', 'type', 'title', 'director', 'cast', 'country', 'date_added', 'release_year', 'rating', 'duration', 'listed_in', 'description']

#Check for missing values
print(df.isnull().sum())
#missing values in director, cast, country, date_added, rating, and duration

#Check the data type of each column
print(df.dtypes)
#releasing year is integer, others are strings

#Fill the missing values (string) with Unknown
for col in df.select_dtypes(include='object').columns:
    print("Filling column:", col)
    df[col] = df[col].fillna("Unknown")

#Fill the missing values(integer) with median number.
median_year = df['release_year'].median()
df['release_year'] = df['release_year'].fillna(median_year)

# Confirm it worked
print("Missing release_years:", df['release_year'].isnull().sum())

#Confirm all worked
print(df.isnull().sum())

#1.Plot a bar chart to compare the number of movies and shows
type_counts =df['type'].value_counts()
ype_counts.plot(kind='bar', color=['skyblue','lightgreen'])
plt.title('Number of Movies vs TV shows on Netflix')
plt.xlabel('type')
plt.ylabel('Number')
plt.tight_layout()
plt.show()

#2. Plot a trend chart to show the increasing programs on Netflix each year
print(df["date_added"].head())

# Remove extra spaces from date strings
df['date_added'] = df['date_added'].str.strip()

# Convert to datetime format
df['date_added'] = pd.to_datetime(df['date_added'])

# Extract the year
df['year_added'] = df['date_added'].dt.year

#Count the number of titles added per year
yearly_counts = df['year_added'].value_counts().sort_index()

#Create a trend chart
yearly_counts.plot(kind='line', marker='o', color = 'teal')
plt.title("Increasing Programs in Netflix Each Year")
plt.xlabel("Year")
plt.ylabel("Amount")
plt.grid(True)
plt.tight_layout()
plt.show()

#3. Plot a pie chart to show the most popular categories
print(df["listed_in"].head())

#Combine all genres into one big string, split by comma, and clean up spaces
all_genres = ', '.join(df['listed_in']).split(',')

#Count each genre
genre_counts = Counter(all_genres)

#Get the top 10 most common genres
top_genres = genre_counts.most_common(10)
print(top_genres)

#Convert to a DataFrame
genre_df = pd.DataFrame(top_genres, columns=['Genre', 'Count'])

plt.figure(figsize=(8,8)) #the size of the pie
plt.pie(genre_df['Count'], labels=genre_df['Genre'], autopct='%1.1f%%', startangle=140)

#use the Count as the portion, Genre as the name of the portion, autopct is the percentage decimal, start angle
plt.title('Top 10 Netflix Genres (Pie Chart)')
plt.tight_layout()
plt.show()



