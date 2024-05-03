class Solution(object):
    def convertTemperature(self, celsius):
        """
        :type celsius: float
        :rtype: List[float]
        """
        # convert to kelvin using known formula
        kelvin = celsius + 273.15
        # convert to fahrenheit using known formula
        fahrenheit = celsius * 1.80 + 32.00
        # return output
        return [kelvin, fahrenheit]