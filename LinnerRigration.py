import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder, MinMaxScaler

def reg(data):
    
    Label_Encoder = LabelEncoder()
    data['Brand_encoded'] = Label_Encoder.fit_transform(data['Brand']).astype(float)
    data['Fuel_encoded'] = Label_Encoder.fit_transform(data['Fuel']).astype(float)
    data['Model_encoded'] = Label_Encoder.fit_transform(data['Model']).astype(float)
    # error found 
    
    numeric_columns = ['Mileage', 'Year']
    # scaler = StandardScaler()
    scaler = MinMaxScaler()
    data[numeric_columns] = scaler.fit_transform(data[numeric_columns])
    # data[numeric_columns] = scaler.fit_transform(data[numeric_columns]).astype(float)
    # error found 
    
    drop_columns = ['Model','Brand','Fuel']
    data = data.drop(columns= drop_columns)
    
    data.rename(columns={"Brand_encoded": "Brand"}, inplace=True)
    data.rename(columns={"Model_encoded": "Model"}, inplace=True)
    data.rename(columns={"Fuel_encoded": "Fuel"}, inplace=True)
    
    new_order = ['Model', 'Brand', 'Mileage', 'Year', 'Fuel']
    # Reorder the columns
    data = data[new_order]
    
    print(data)
    x_test = data
    df = pd.read_csv('./processed_data.csv')
    x_train = df.drop('Price',axis=1)
    y_train = df['Price']

    model = LinearRegression()
    model.fit(x_train, y_train)

    y_pred = model.predict(x_test)    
    # result = scaler.inverse_transform(y_pred)
    scaler.fit(y_train.values.reshape(-1, 1))  
    original_prediction = scaler.inverse_transform(y_pred.reshape(-1, 1))

    # print(original_prediction)
    # print(y_pred)
    # print(x_test)
    return original_prediction ;
    