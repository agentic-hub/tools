from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import OpenweathermapCredentials

class OpenweathermapCurrentweatherToolInput(BaseModel):
    language: Optional[str] = Field(None, description="The two letter language code to get your output in (eg. en, de, ...).")
    longitude: Optional[str] = Field(None, description="The longitude of the location to return the weather of")
    zip_code: Optional[str] = Field(None, description="The ID of city to return the weather of. List can be downloaded here: http://bulk.openweathermap.org/sample/.")
    city_id: Optional[float] = Field(None, description="The ID of city to return the weather of. List can be downloaded here: http://bulk.openweathermap.org/sample/.")
    location_selection: Optional[str] = Field(None, description="How to define the location for which to return the weather")
    format: Optional[str] = Field(None, description="The format in which format the data should be returned")
    latitude: Optional[str] = Field(None, description="The latitude of the location to return the weather of")
    city_name: Optional[str] = Field(None, description="The name of the city to return the weather of")
    operation: Optional[str] = Field(None, description="Operation")


class OpenweathermapCurrentweatherTool(BaseTool):
    name: str = "openweathermap_currentweather"
    connector_id: str = "nodes-base.openWeatherMap"
    description: str = "Tool for openWeatherMap currentWeather operation - currentWeather operation"
    args_schema: type[BaseModel] | None = OpenweathermapCurrentweatherToolInput
    credentials: Optional[OpenweathermapCredentials] = None
