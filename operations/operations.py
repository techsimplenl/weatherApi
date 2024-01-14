"""Operation program"""
class Operations:
    """All operations"""
    @staticmethod
    def retrieve_important_forecast(data_: dict,weather:any):
        """Retrieve important forecast information from the given data."""
        for item, details in data_.items():
            if 'location' == item:
                weather.assign_location(weather,details)
            if 'current' == item:
                weather.assign_current(weather,details)
            if 'forecast' == item:
                weather.assign_forecast(weather,details)
    