import joblib
import pandas as pd
import numpy as np
import pytest


@pytest.fixture(scope='module')
def model():
    with open('src//modelo//modelo.pkl', 'rb') as file:
        return joblib.load(file)

@pytest.fixture(scope='module')
def df():
    return pd.read_json("""{"EngineSize":{"0":3.5},"Cylinders":{"0":6.0},"Horsepower":{"0":265},"MPG_City":{"0":17},"MPG_Highway":{"0":23},"Weight":{"0":4451},"Wheelbase":{"0":106},"Length":{"0":189},"Make_Acura":{"0":1},"Make_Audi":{"0":0},"Make_BMW":{"0":0},"Make_Buick":{"0":0},"Make_Cadillac":{"0":0},"Make_Chevrolet":{"0":0},"Make_Chrysler":{"0":0},"Make_Dodge":{"0":0},"Make_Ford":{"0":0},"Make_GMC":{"0":0},"Make_Honda":{"0":0},"Make_Hummer":{"0":0},"Make_Hyundai":{"0":0},"Make_Infiniti":{"0":0},"Make_Isuzu":{"0":0},"Make_Jaguar":{"0":0},"Make_Jeep":{"0":0},"Make_Kia":{"0":0},"Make_Land Rover":{"0":0},"Make_Lexus":{"0":0},"Make_Lincoln":{"0":0},"Make_MINI":{"0":0},"Make_Mazda":{"0":0},"Make_Mercedes-Benz":{"0":0},"Make_Mercury":{"0":0},"Make_Mitsubishi":{"0":0},"Make_Nissan":{"0":0},"Make_Oldsmobile":{"0":0},"Make_Pontiac":{"0":0},"Make_Porsche":{"0":0},"Make_Saab":{"0":0},"Make_Saturn":{"0":0},"Make_Scion":{"0":0},"Make_Subaru":{"0":0},"Make_Suzuki":{"0":0},"Make_Toyota":{"0":0},"Make_Volkswagen":{"0":0},"Make_Volvo":{"0":0},"Type_Hybrid":{"0":0},"Type_SUV":{"0":1},"Type_Sedan":{"0":0},"Type_Sports":{"0":0},"Type_Truck":{"0":0},"Type_Wagon":{"0":0},"DriveTrain_All":{"0":1},"DriveTrain_Front":{"0":0},"DriveTrain_Rear":{"0":0}}""")


def test_prediction(model, df):
    prediction = model.predict(df)
    assert len(prediction) == len(df), "Número de linhas da predição deve ser igual ao número de linhas do DataFrame"
    prediction_sample = round(prediction[0],4)
    assert prediction_sample == 36944.9998, "Comparando com o resultado encontrada na etapa de desenvolvimento"