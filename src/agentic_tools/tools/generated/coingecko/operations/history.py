from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class CoingeckoHistoryToolInput(BaseModel):
    date: Optional[str] = Field(None, description="The date of data snapshot")
    baseCurrency: Optional[str] = Field(None, description="The first currency in the pair. For BTC:ETH this is BTC. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    resource: Optional[str] = Field(None, description="Resource")
    baseCurrencies: Optional[str] = Field(None, description="baseCurrencies")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    quoteCurrencies: Optional[str] = Field(None, description="quoteCurrencies")
    coinId: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    operation: Optional[str] = Field(None, description="Operation")


class CoingeckoHistoryTool(BaseTool):
    name = "coingecko_history"
    description = "Tool for coinGecko history operation - history operation"
    
    def _run(self, **kwargs):
        """Run the coinGecko history operation."""
        # Implement the tool logic here
        return f"Running coinGecko history operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the coinGecko history operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
