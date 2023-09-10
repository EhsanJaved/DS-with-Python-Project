import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
def cars(input_data):
        
    # Create a DataFrame from the car data
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
        ('model', LinearRegression())
    ])

    # Train the pipeline on training data
    pipeline.fit(X_train, y_train)

    # Convert the test data to a DataFrame
    test_df = pd.DataFrame([input_data])


    # Make predictions using the pipeline
    predicted_price = pipeline.predict(test_df)

    formatted_price = "{:,.2f}".format(predicted_price[0])

    return formatted_price
