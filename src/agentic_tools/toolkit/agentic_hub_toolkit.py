import os

from typing import List, Optional
import copy

from pydantic import BaseModel
from agentic_tools.tools.base import BaseTool


class AgenticHubToolkit:
    credentials: Optional[BaseModel] = None

    def get_tools_from_operations(self, operation) -> List[BaseTool]:
        tools = operation.get_tools()

        for tool in tools:
            tool.credentials = self.credentials

        return tools
