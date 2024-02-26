# import joblib
# from pydantic import BaseModel
# from fastapi import FastAPI, HTTPException
# from fastapi.responses import JSONResponse

# # 1. Load the trained model
# model = joblib.load(r'C:\Users\admin\Documents\credit_card_project\Credit_card_Fraud_Detection-main\Credit_card_Fraud_Detection-main\frauddetection_02.pkl')

# # 2. Define the input data schema using Pydantic BaseModel
# class InputData(BaseModel):
#     Year: int
#     Month: int
#     UseChip: int
#     Amount: int
#     MerchantName: int
#     MerchantCity: int
#     MerchantState: int
#     mcc: int
#     # Add the rest of the input features (feature9, feature10, ..., feature12)

# # 3. Create a FastAPI app
# app = FastAPI()

# # 4. Define the root endpoint
# @app.get("/")
# def read_root():
#     return {"message": "Welcome to the FastAPI app"}

# # 5. Define the prediction route
# @app.post('/predict')
# def predict(data: InputData):
#     try:
#         # Convert the input data to a dictionary
#         input_data = data.dict()

#         # Extract the input features from the dictionary
#         feature1 = input_data['Year']
#         feature2 = input_data['Month']
#         feature3 = input_data['UseChip']
#         feature4 = input_data['Amount']
#         feature5 = input_data['MerchantName']
#         feature6 = input_data['MerchantCity']
#         feature7 = input_data['MerchantState']
#         feature8 = input_data['mcc']
#         # Extract the rest of the input features (feature9, feature10, ..., feature12)

#         # Perform the prediction using the loaded model
#         prediction = model.predict([[feature1, feature2, feature3, feature4, feature5, feature6, feature7, feature8]])  # Replace ... with the rest of the features

#         # Convert the prediction to a string (or any other format you prefer)
#         result = "Fraud" if prediction[0] == 1 else "Not a Fraud"

#         return {"prediction": result}

#     except Exception as e:
#         # Handle exceptions, return a meaningful error response
#         return JSONResponse(content={"error": str(e)}, status_code=500)




import joblib
import uvicorn
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse

# 1. Load the trained model
model = joblib.load(r'C:\Users\admin\Documents\credit_card_project\Credit_card_Fraud_Detection-main\Credit_card_Fraud_Detection-main\frauddetection_02.pkl')

# 2. Define the input data schema using Pydantic BaseModel
class InputData(BaseModel):
    Year: int
    Month: int
    UseChip: int
    Amount: int
    MerchantName: int
    MerchantCity: int
    MerchantState: int
    mcc: int
    # Add the rest of the input features (feature9, feature10, ..., feature12)

# 3. Create a FastAPI app
app = FastAPI()

# 4. Define the root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI app"}

# 5. Define the prediction route
@app.post('/predict')
def predict(data: InputData):
    try:
        # Convert the input data to a dictionary
        input_data = data.dict()

        # Extract the input features from the dictionary
        feature1 = input_data['Year']
        feature2 = input_data['Month']
        feature3 = input_data['UseChip']
        feature4 = input_data['Amount']
        feature5 = input_data['MerchantName']
        feature6 = input_data['MerchantCity']
        feature7 = input_data['MerchantState']
        feature8 = input_data['mcc']
        # Extract the rest of the input features (feature9, feature10, ..., feature12)

        # Perform the prediction using the loaded model
        prediction = model.predict([[feature1, feature2, feature3, feature4, feature5, feature6, feature7, feature8]])  # Replace ... with the rest of the features

        # Convert the prediction to a string (or any other format you prefer)
        result = "Fraud" if prediction[0] == 1 else "Not a Fraud"

        return {"prediction": result}

    except ValueError as ve:
        # Handle the ValueError related to the prediction
        return JSONResponse(content={"error": f"ValueError: {ve}"}, status_code=400)

    except Exception as e:
        # Handle other exceptions
        return JSONResponse(content={"error": f"An unexpected error occurred: {e}"}, status_code=500)
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=7000)