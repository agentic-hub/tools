# openWeatherMap operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel
from .. import OpenweathermapCredentials

def get_tools() -> List[BaseTool]:
    """Get all openWeatherMap operation tools."""
    tools = []
    from .currentweather import OpenweathermapCurrentweatherTool
    tools.append(OpenweathermapCurrentweatherTool())
    from .5dayforecast import Openweathermap5dayforecastTool
    tools.append(Openweathermap5dayforecastTool())
    return tools
