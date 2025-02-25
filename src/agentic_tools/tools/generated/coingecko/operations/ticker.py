from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class CoingeckoTickerToolInput(BaseModel):
    base_currency: Optional[str] = Field(None, description="The first currency in the pair. For BTC:ETH this is BTC. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    resource: Optional[str] = Field(None, description="Resource")
    base_currencies: Optional[str] = Field(None, description="baseCurrencies")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    quote_currencies: Optional[str] = Field(None, description="quoteCurrencies")
    coin_id: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    operation: Optional[str] = Field(None, description="Operation")


class CoingeckoTickerTool(BaseTool):
    name = "coingecko_ticker"
    description = "Tool for coinGecko ticker operation - ticker operation"
    
    def __init__(self, **kwargs):
        """Initialize the tool.
        
        Args:
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
    
    def _run(self, **kwargs):
        """Run the coinGecko ticker operation."""
        # Implement the tool logic here
        return f"Running coinGecko ticker operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the coinGecko ticker operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
