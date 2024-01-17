import pandas as pd
import matplotlib.pyplot as plt
ipl_data=pd.read_csv("/Users/suyashsrivastav/Vidhi_Project/ipl1.csv")
# Prompt the user for what information to display
task = input("Choose a task to perform \n1: First few rows, \n2: Basic statistics, \n3: Information, \n4: Matches per season, \n5: Teams with most wins, \n6: Average win by runs, \n7: Plot matches per season): ")

if task == '1':
    # Display the first few rows of the dataset
    print("First few rows of the dataset:")
    print(ipl_data.head())

elif task == '2':
    # Basic statistics of the dataset
    print("\nBasic statistics of the dataset:")
    print(ipl_data.describe())

elif task == '3':
    # Information about the dataset, including data types and missing values
    print("\nInformation about the dataset:")
    print(ipl_data.info())

elif task == '4':
    # Example: Count the number of matches in each season
    matches_per_season = ipl_data['season'].value_counts().sort_index()
    print("\nNumber of matches in each season:")
    print(matches_per_season)

elif task == '5':
    # Example: Teams with the most wins
    teams_with_most_wins = ipl_data['winner'].value_counts()
    print("\nTeams with the most wins:")
    print(teams_with_most_wins)

elif task == '6':
    # Example: Average win-by-runs
    average_win_by_runs = ipl_data['win_by_runs'].mean()
    print("\nAverage win by runs:", average_win_by_runs)

elif task == '7':
    # Example: Plotting number of matches in each season
    matches_per_season = ipl_data['season'].value_counts().sort_index()
    matches_per_season.plot(kind='bar', color='skyblue')
    plt.title('Number of Matches in Each Season')
    plt.xlabel('Season')
    plt.ylabel('Number of Matches')
    plt.show()

else:
    print("Invalid input. Please enter a number between 1 and 7.")
