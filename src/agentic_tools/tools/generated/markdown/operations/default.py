from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class MarkdownDefaultToolInput(BaseModel):
    html: Optional[str] = Field(None, description="The HTML to be converted to markdown")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    markdown: Optional[str] = Field(None, description="The Markdown to be converted to html")
    destinationKey: Optional[str] = Field(None, description="The field to put the output in. Specify nested fields using dots, e.g.\"level1.level2.newKey\".")
    mode: Optional[str] = Field(None, description="Mode")


class MarkdownDefaultTool(BaseTool):
    name = "markdown_default"
    description = "Tool for markdown default operation - default operation"
    
    def _run(self, **kwargs):
        """Run the markdown default operation."""
        # Implement the tool logic here
        return f"Running markdown default operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the markdown default operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
