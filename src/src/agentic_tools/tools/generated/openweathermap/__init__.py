# openWeatherMap toolkit
from langchain.tools import BaseTool
from typing import List

def get_openweathermap_tools() -> List[BaseTool]:
    """Get all openWeatherMap tools."""
    from . import operations
    return operations.get_tools()
