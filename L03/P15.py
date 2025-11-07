def check_pm25_aqi():
    
    pm25_input = input("PM2.5: ")
    pm25_level = float(pm25_input)

    if pm25_level <= 12.0:
        aqi_category = "Good"
    elif pm25_level <= 35.4:
        aqi_category = "Moderate"
    elif pm25_level <= 55.4:
        aqi_category = "Unhealthy for Sensitive Groups"
    elif pm25_level <= 150.4:
        aqi_category = "Unhealthy"
    elif pm25_level <= 250.4:
        aqi_category = "Very Unhealthy"
    else:
        aqi_category = "Hazardous"
    

    print("AQI: {}".format(aqi_category))

if __name__ == '__main__':
    check_pm25_aqi()