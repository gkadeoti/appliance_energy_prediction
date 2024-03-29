# Appliance Energy Prediction

## Introduction

This repository is for Appliances Energy Prediction

### Data Source

Luis Candanedo, luismiguel.candanedoibarra '@' umons.ac.be, University of Mons (UMONS).

### Data Set Information:

The data set is at 10 min for about 4.5 months. The house temperature and humidity conditions were monitored with a ZigBee wireless sensor network. Each wireless node transmitted the temperature and humidity conditions around 3.3 min. Then, the wireless data was averaged for 10 minutes periods. The energy data was logged every 10 minutes with m-bus energy meters. Weather from the nearest airport weather station (Chievres Airport, Belgium) was downloaded from a public data set from Reliable Prognosis (rp5.ru), and merged together with the experimental data sets using the date and time column. Two random variables have been included in the data set for testing the regression models and to filter out non predictive attributes (parameters).

For more information about the house, data collection, R scripts and figures, please refer to the paper and to the following github repository:

[Web Link](https://github.com/LuisM78/Appliances-energy-prediction-data)


### Attribute Information:

```

date time year-month-day hour:minute:second
Appliances, energy use in Wh
lights, energy use of light fixtures in the house in Wh
T1, Temperature in kitchen area, in Celsius
RH_1, Humidity in kitchen area, in %
T2, Temperature in living room area, in Celsius
RH_2, Humidity in living room area, in %
T3, Temperature in laundry room area
RH_3, Humidity in laundry room area, in %
T4, Temperature in office room, in Celsius
RH_4, Humidity in office room, in %
T5, Temperature in bathroom, in Celsius
RH_5, Humidity in bathroom, in %
T6, Temperature outside the building (north side), in Celsius
RH_6, Humidity outside the building (north side), in %
T7, Temperature in ironing room , in Celsius
RH_7, Humidity in ironing room, in %
T8, Temperature in teenager room 2, in Celsius
RH_8, Humidity in teenager room 2, in %
T9, Temperature in parents room, in Celsius
RH_9, Humidity in parents room, in %
To, Temperature outside (from Chievres weather station), in Celsius
Pressure (from Chievres weather station), in mm Hg
RH_out, Humidity outside (from Chievres weather station), in %
Wind speed (from Chievres weather station), in m/s
Visibility (from Chievres weather station), in km
Tdewpoint (from Chievres weather station), Â°C
rv1, Random variable 1, nondimensional
rv2, Random variable 2, nondimensional
```

Where indicated, hourly data (then interpolated) from the nearest airport weather station (Chievres Airport, Belgium) was downloaded from a public data set from Reliable Prognosis, rp5.ru. Permission was obtained from Reliable Prognosis for the distribution of the 4.5 months of weather data.




## Environment Setup

If your `conda` base environment is old, it is important that you install the `setuptools` and `wheel` packages that are dependencies for autogluon
```
pip install setuptools wheel

Step 1: Create Environment
```
conda create --name applianceenv python=3.9 -y
```

Step 2: Activate Environment
```
conda activate applianceenv

Setp 3: Install required packages: autogluon, streamlit, jupyter
```bash
pip install torch==1.13.1 torchvision==0.14.1 -f https://download.pytorch.org/whl/cpu/torch_stable.html
pip install autogluon streamlit jupyter



## Code Structure

## Exploratory Data Analysis (EDA)

## Model Building

## Model Evaluation

## Model WebApp (Streamlit)
