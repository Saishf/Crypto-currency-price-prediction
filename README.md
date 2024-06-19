
# Cryptocurrency Price Prediction using GRU and LSTM

This repository contains code for extracting data and implementing neural network models using GRU (Gated Recurrent Unit) and LSTM (Long Short-Term Memory) architectures for time series analysis. The data used for this project is sourced from the Binance cryptocurrency exchange.


## Table of Contents
* Overview
* Installation
* Usage
* File Descriptions
* Data Source
* Results
* Contributing
* License
## Overview

This project aims to provide a comprehensive solution for cryptocurrency price prediction using advanced neural network models. The repository includes:

* Data extraction scripts to preprocess and prepare the dataset.
* Jupyter notebooks and Python scripts implementing GRU and LSTM models for time series forecasting.
## Installation

To get started, clone the repository and install the required dependencies.

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
pip install -r requirements.txt
```
    
## Usage/Examples
1. Data Extraction: Run the data extraction script to prepare your dataset.
```bash
python data_extraction.py

```
2. GRU Model (Initial): Open the GRU (1).ipynb notebook and run all cells to train and evaluate the initial GRU model.
3. GRU Model (Improved): Run the gru2.py script to train and evaluate the improved GRU model.
```bash
python gru2.py

```
4. LSTM Model: Open the LSTM (1).ipynb notebook and run all cells to train and evaluate the LSTM model.


## File Description

* data_extraction.py: Script for data extraction and preprocessing.
* GRU (1).ipynb: Jupyter notebook implementing the initial GRU model for cryptocurrency price forecasting.
* gru2.py: Python script implementing the improved GRU model with additional enhancements.
* LSTM (1).ipynb: Jupyter notebook implementing the LSTM model for cryptocurrency price forecasting.
## Data source

The data used in this project is sourced from the Binance cryptocurrency exchange. Ensure that you have the necessary API keys and permissions to access the data from Binance.
## Result
The results of the models, including performance metrics and visualizations, are documented in their respective Jupyter notebooks and scripts.
## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

1. Fork the Project
2. Create your Feature Branch (git checkout -b feature/AmazingFeature)
3. Commit your Changes (git commit -m 'Add some AmazingFeature')
4. Push to the Branch (git push origin feature/AmazingFeature)
5. Open a Pull Request


## License

[MIT](https://choosealicense.com/licenses/mit/)

