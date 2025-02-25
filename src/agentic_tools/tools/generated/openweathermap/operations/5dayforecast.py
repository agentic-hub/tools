from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class Openweathermap5dayforecastToolInput(BaseModel):
    language: Optional[str] = Field(None, description="The two letter language code to get your output in (eg. en, de, ...).")
    longitude: Optional[str] = Field(None, description="The longitude of the location to return the weather of")
    zipCode: Optional[str] = Field(None, description="The ID of city to return the weather of. List can be downloaded here: http://bulk.openweathermap.org/sample/.")
    cityId: Optional[float] = Field(None, description="The ID of city to return the weather of. List can be downloaded here: http://bulk.openweathermap.org/sample/.")
    locationSelection: Optional[str] = Field(None, description="How to define the location for which to return the weather")
    format: Optional[str] = Field(None, description="The format in which format the data should be returned")
    latitude: Optional[str] = Field(None, description="The latitude of the location to return the weather of")
    cityName: Optional[str] = Field(None, description="The name of the city to return the weather of")
    operation: Optional[str] = Field(None, description="Operation")


class Openweathermap5dayforecastTool(BaseTool):
    name = "openweathermap_5dayforecast"
    description = "Tool for openWeatherMap 5DayForecast operation - 5DayForecast operation"
    
    def _run(self, **kwargs):
        """Run the openWeatherMap 5DayForecast operation."""
        # Implement the tool logic here
        return f"Running openWeatherMap 5DayForecast operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the openWeatherMap 5DayForecast operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
