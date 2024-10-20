from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import pandas as pd
df = pd.read_excel(r"Crime Predictor\crimelog1.xlsx")
df.columns = ['Nature_Classification', 'Date_Time_Occurred', 'Street_Name']
df['Nature_Classification'] = df['Nature_Classification'].str.replace('\n', ' ')
df['Nature_Classification_Code'] = df['Nature_Classification'].astype('category').cat.codes
df['Date_Time_Occurred'] = pd.to_datetime(df['Date_Time_Occurred'],format='%m/%d/%y %H:%M')
df['Hour'] = df['Date_Time_Occurred'].dt.hour
df['Minute'] = df['Date_Time_Occurred'].dt.minute
df['Day'] = df['Date_Time_Occurred'].dt.day
df['Street_Name_Code'] = df['Street_Name'].astype('category').cat.codes
features = df[['Hour', 'Minute', 'Day','Street_Name_Code']]
target = df['Nature_Classification_Code']
print(df.head())
street_name = "e apache blvd"
street_code_series = df[df['Street_Name'] == street_name.upper()]['Street_Name_Code']
if not street_code_series.empty:
    street_code = street_code_series.iloc[0]
    print(street_code)
else:
    print(f"No street found with the name '{street_name.upper()}'")

X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.3, random_state=42)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)
example_features = pd.DataFrame({'Hour':[3],'Minute':[58],'Day':[21],'Street_Name_Code':[2]})
predicted_probabilities = model.predict_proba(example_features)
category_mapping = dict(enumerate(df['Nature_Classification'].astype('category').cat.categories))

# Print probabilities for each crime category
max = 0
max_category = ""
for i, probability in enumerate(predicted_probabilities[0]):
    crime_category = category_mapping[i]
    print(f"Probability of {crime_category}: {probability:.2f}")
    if probability > max:
      max = probability
      max_category = crime_category

print(f"The most likely crime to happen is: {max_category}")