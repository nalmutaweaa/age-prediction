# Age Prediction Using CNN

## Overview
This project uses a Convolutional Neural Network (CNN) to predict a person's approximate age from facial images.

## Dataset
- **Source:** UTKFace Dataset (Kaggle)
- **Total Images:** 23,708
- **Age Range:** 1–116 years
- **Distribution:** Most images represent individuals aged 20–40, indicating an imbalanced age distribution.

## Tools and Libraries
- Python
- TensorFlow / Keras
- NumPy
- Pandas
- Matplotlib
- Scikit-learn
- Gradio
- Pillow (PIL)

## Process
1. Extracted age labels from image filenames.
2. Split the dataset into 80% training and 20% testing using Scikit-learn.
3. Resized images to 64×64 pixels and normalized pixel values between 0 and 1.
4. Built a baseline neural network and a CNN for age regression.
5. Trained the CNN using Mean Absolute Error (MAE) as the loss function and Mean Squared Error (MSE) as an additional metric.

## Model Results
The CNN was trained for 12 epochs.

- **Training MAE:** 6.30 years
- **Validation MAE:** 7.41 years
- **Training MSE:** 83.26
- **Validation MSE:** 116.83

The model achieved an average training error of approximately 6.3 years and a validation error of approximately 7.4 years.

## Deployment
The model is integrated into a Gradio application that allows users to upload an image or use their webcam to predict their approximate age.
