from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class ThehivetriggerDefaultToolInput(BaseModel):
    notice: Optional[str] = Field(None, description="You must set up the webhook in TheHive — instructions <a href=\"https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.thehivetrigger/#configure-a-webhook-in-thehive\" target=\"_blank\">here</a>")
    events: Optional[str] = Field(None, description="events")


class ThehivetriggerDefaultTool(BaseTool):
    name = "thehivetrigger_default"
    description = "Tool for theHiveTrigger default operation - default operation"
    
    def _run(self, **kwargs):
        """Run the theHiveTrigger default operation."""
        # Implement the tool logic here
        return f"Running theHiveTrigger default operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the theHiveTrigger default operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
