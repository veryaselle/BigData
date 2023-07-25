import csv
from sklearn.model_selection import train_test_split

# 2 liste vergleichen - ob tracks aus der track_i.csv (nur tracks) in track_playlist.csv vorhanden -> output: track_allowed_list.csv Anzahl: 91325


def list_manufactory_allowed(infile1, infile2, outfile):
    with open(infile1, 'r', newline='') as tr_list_file:
        with open(infile2, 'r', newline='') as tr_from_pl_list_file:
            with open(outfile, 'w', newline='') as file:
                tr_list = csv.reader(tr_list_file)
                tr_from_pl_list = csv.reader(tr_from_pl_list_file)
                writer = csv.writer(file)

                track_set = set(line[0].strip() for line in tr_from_pl_list)
                allowed_tracks = []

                for line in tr_list:
                    track = line[0].strip()
                    if track in track_set:
                        allowed_tracks.append(line)

                writer.writerows(allowed_tracks)
                print("Allowed tracks:")
                for track in allowed_tracks:
                    print(track)


# Neue Liste namens --track_allowed_list-- erstellen:
track_path = 'C:/Users/verya/Desktop/DS23/BigData/track_i.csv'
track_playlist1_path = 'C:/Users/verya/Desktop/DS23/BigData/track_playlist1.csv'
new_track_allowed_list_path = 'C:/Users/verya/Desktop/DS23/BigData/track_allowed_list.csv'

list_manufactory_allowed(track_playlist1_path, track_path, new_track_allowed_list_path)

# Split the data into training, validation, and test sets
track_allowed_list_path = 'C:/Users/verya/Desktop/DS23/BigData/track_allowed_list.csv'

# Read the allowed tracks CSV into a pandas DataFrame
import pandas as pd
df = pd.read_csv(track_allowed_list_path)

# Splitting into training, validation, and test sets
train_df, temp_df = train_test_split(df, test_size=0.3, random_state=42)
val_df, test_df = train_test_split(temp_df, test_size=0.5, random_state=42)

# Save the split DataFrames to CSV files
train_df.to_csv('C:/Users/verya/Desktop/DS23/BigData/train_set.csv', index=False) # 70% 63927 rows
val_df.to_csv('C:/Users/verya/Desktop/DS23/BigData/validation_set.csv', index=False) # 15% 13700 rows
test_df.to_csv('C:/Users/verya/Desktop/DS23/BigData/test_set.csv', index=False) #15% 13700 rows

# 91327 total for track_allowed_list.csv





