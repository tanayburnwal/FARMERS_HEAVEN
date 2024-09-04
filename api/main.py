from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import numpy as np
from io import BytesIO
from PIL import Image
import tensorflow as tf

app = FastAPI()
origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:5500",
    "http://127.0.0.1:5500"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

MODEL = tf.keras.models.load_model("C:\\Users\\User\\potato-disease\\saved_models\\m21.keras")

model_bell_peper = tf.keras.models.load_model("C:\\Users\\User\\potato-disease\\saved_models\\bp.keras")

class_bell_pepper = ["Bacterial", "Healthy"] 

CLASS_NAMES = ["Early Blight", "Late Blight", "Healthy"]

@app.get("/ping")
async def ping():
    return "Hello, I am alive"

def read_file_as_image(data) -> np.ndarray:
    image = np.array(Image.open(BytesIO(data)))
    return image

@app.post("/predict")
async def predict(
    file: UploadFile = File(...)
):
    image = read_file_as_image(await file.read())
  
    image =Image.fromarray(image)
    # image=image.resize((128,128))
    image=np.array(image)


    img_batch = np.expand_dims(image, 0)
    # img_batch =img_batch.astype('uint8')/255
    

    
    predictions = MODEL.predict(img_batch)

    predicted_class = CLASS_NAMES[np.argmax(predictions[0])]
    confidence = float(np.max(predictions[0]))  # Convert to Python float
    return {
        'class': predicted_class,
        'confidence': confidence*100
    }



@app.post("/predict_bp")
async def predict(
    file: UploadFile = File(...)
):
    image = read_file_as_image(await file.read())
    
    
    image =Image.fromarray(image)
    image=image.resize((256,256))
    image=np.array(image)


    img_batch = np.expand_dims(image, 0)
    img_batch =img_batch.astype('uint8')/255

    
    predictions = model_bell_peper.predict(img_batch)

    predicted_class = class_bell_pepper[np.argmax(predictions[0])]
    confidence = float(np.max(predictions[0]))  # Convert to Python float
    return {
        'class': predicted_class,
        'confidence': confidence*100
    }







if __name__ == "__main__":
    uvicorn.run(app, host='localhost', port=8000)













































































# from fastapi import FastAPI, File, UploadFile
# from fastapi.middleware.cors import CORSMiddleware
# import uvicorn
# import numpy as np
# from io import BytesIO
# from PIL import Image
# import tensorflow as tf

# app = FastAPI()

# origins = [
#     "http://localhost",
#     "http://localhost:3000",
#     "http://127.0.0.1:5500"
# ]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# MODEL = tf.keras.models.load_model("C:\\Users\\User\\potato-disease\\saved_models\\m2.keras")

# CLASS_NAMES = ["Healty", "Late Blight", "Early"]

# @app.get("/")
# async def test():
#     return "Hello, I am alive"

# def read_file_as_image(data): #-> np.ndarray
#     image = np.array(Image.open(BytesIO(data)))


#     return image

# @app.post("/predict")
# async def predict(file: UploadFile = File(...)):
#     image = read_file_as_image(await file.read())

#     image =Image.fromarray(image)
#     image=image.resize((256,256))
#     image=np.array(image)


#     img_batch = np.expand_dims(image, 0)
#     img_batch =img_batch.astype('uint8')/255
    
#     predictions = MODEL.predict(img_batch)

#     predicted_class = CLASS_NAMES[np.argmax(predictions[0])]
#     confidence = np.max(predictions[0])
#     return {
#         'class': predicted_class,
#         'confidence': float(confidence)*100
#         'predictions':predictions.tolist()
#     }

# if __name__ == "__main__":
#     uvicorn.run(app, host='localhost', port=8000)
