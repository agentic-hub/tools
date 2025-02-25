from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class OpenweathermapCredentials(BaseModel):
    """Credentials for openWeatherMap authentication."""
    open_weather_map_api: Optional[Dict[str, Any]] = Field(None, description="openWeatherMapApi")

class OpenweathermapCurrentweatherToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[OpenweathermapCredentials] = Field(None, description="Custom credentials for authentication")
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
    name = "openweathermap_currentweather"
    description = "Tool for openWeatherMap currentWeather operation - currentWeather operation"
    
    def __init__(self, credentials: Optional[OpenweathermapCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the openWeatherMap currentWeather operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running openWeatherMap currentWeather operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running openWeatherMap currentWeather operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the openWeatherMap currentWeather operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
