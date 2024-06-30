# Mobile-app-prediction


This repository contains a Streamlit web application that predicts the price of mobile phones based on various features. The prediction is made using a pre-trained machine learning model.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Model and Data](#model-and-data)
- [Contributing](#contributing)
- [License](#license)

## Overview

The Mobile Price Predictor app allows users to input various specifications of a mobile phone and predicts its price. The application is built using Streamlit for the web interface and a machine learning model for the prediction.

## Features

- Select mobile phone features such as brand, processor, RAM, battery capacity, etc.
- Predict the price of a mobile phone based on the selected features.
- User-friendly interface built with Streamlit.

## Installation

To run this application locally, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/mobile-price-predictor.git
   cd mobile-price-predictor
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv env
   ```

3. **Activate the virtual environment:**
   - On Windows:
     ```bash
     .\env\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source env/bin/activate
     ```

4. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the Streamlit app:**
   ```bash
   streamlit run app.py
   ```

## Usage

After running the app, open your web browser and go to `http://localhost:8501`. You will see the Streamlit interface where you can input the mobile phone specifications and get the predicted price.

## Model and Data

- The pre-trained machine learning model and the dataset are loaded from pickle files (`pipe.pkl` and `df.pkl`).
- The model was trained using various mobile phone features such as brand, processor, RAM, battery capacity, etc.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes. Ensure that your code adheres to the project's coding standards and includes appropriate tests.
