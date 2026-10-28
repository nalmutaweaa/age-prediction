import gradio as gr
from PIL import Image
import numpy as np
from tensorflow.keras.models import load_model

#prediction function 
model_age= load_model("age_model.keras")
def predict_age(img):
    img = Image.fromarray(img).convert("RGB").resize((64,64)) 
    img = np.array(img)/ 255.0 
    img = np.expand_dims(img,axis=0)
    pred= model_age.predict(img, verbose=0)[0][0]
    return round(float(pred))

#app interface
app = gr.Interface(
    fn=predict_age,
    inputs=gr.Image(sources=["upload", "webcam"], type="numpy"),
    outputs=gr.Number(label="Predicted Age"),
    title="Age Predection App 👵👶👦",
    description="Please upload or take an image via web cam!"
)

app.launch()
