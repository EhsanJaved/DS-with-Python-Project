import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.ensemble import RandomForestRegressor
import joblib

# Load the car data
df = pd.read_csv('MainCarsData.csv')

# Split the data into features (X) and target (y)
X = df.drop('Price', axis=1)
y = df['Price']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define preprocessing steps
categorical_cols = ['Model', 'Brand', 'Fuel']
categorical_transformer = OneHotEncoder(drop='first')

numeric_cols = ['Year', 'Mileage']
numeric_transformer = StandardScaler()

preprocessor = ColumnTransformer(
    transformers=[
        ('cat', categorical_transformer, categorical_cols),
        ('num', numeric_transformer, numeric_cols)
    ])

# Create a pipeline with preprocessing and model
pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('model', RandomForestRegressor(n_estimators=100, random_state=42))
])

# Train the pipeline on training data
pipeline.fit(X_train, y_train)

# Save the trained model using joblib
joblib.dump(pipeline, 'random_forest_model.joblib')

print("Model saved successfully!")
