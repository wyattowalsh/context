"""context/server.py -- main MCP server module

This server contains the following tools:

- `get_context`: asyncronous tool to prepare LLM-ready context/knowledge file from a URL or a file with configurable gathering context.
"""

from typing import Annotated
from pathlib import Path

from fastmcp import Context, FastMCP
from pydantic import Field
from context.models import Config

class Config(BaseModel):
    """Configuration for the context gathering."""
    crawl4ai: Crawl4AIConfig = Field(
        description="configuration for the crawl4ai tool")
    docling: DoclingConfig = Field(
        description="configuration for the docling tool")


class Crawl4AIConfig(BaseModel):
    """Configuration for the crawl4ai tool."""
    urls: list[str] = Field(
        description="list of URLs or file paths to gather context from")
    max_depth: int = Field(description="maximum depth of the crawl", default=2)
    max_pages: int = Field(description="maximum number of pages to crawl",
                           default=10)
    max_wait_time: int = Field(description="maximum wait time for the crawl",
                               default=10)


class DoclingConfig(BaseModel):
    """Configuration for the docling tool."""
    urls: list[str] = Field(
        description="list of URLs or file paths to gather context from")


mcp = FastMCP(name="context",
              instructions="""
        This server provides LLM context gathering tools.
        Call get_context() to gather context from the web or a file.
    """)



@mcp.tool(
    name="get_context",
    description=
    "main function to gather optimized-for-LLM context from the web or a file.",
    tags=['dev', 'conversion'],
    annotations={
        "title": "Gather Context",
        "readOnlyHint": False,
        "destructiveHint": False,
        "idempotentHint": True,
        "openWorldHint": True
    })
async def get_context(
    urls: Annotated[
        list[str],
        Field(
            description="list of URLs or file paths to gather context from")],
    config: Annotated[
        Config,
        Field(description="configuration for the context gathering")],
    ctx: Annotated[Context, Field(description="MCP context object")],
) -> str:
    """
    main function to gather optimized-for-LLMcontext from the web or a file.

    uses [Crawl4AI](https://github.com/unclecode/crawl4ai) to crawl and scrape the web and [Docling](https://github.com/docling-project/docling) for file conversion. 

    Parameters
    ----------
    urls : Annotated[ list[str], Field, optional
        _description_, by default "list of URLs or file paths to gather context from")]

    Other Parameters
    ----------------

    Returns
    -------
    str
        _description_

    Yields
    ------

    Raises
    ------

    Attributes
    ----------

    See Also
    --------

    Notes
    -----

    References
    ----------

    Examples
    --------

    Todo
    ----

    Warns
    -----
    """



@mcp.prompt()
async def get_context_request(urls: Annotated[list[str|Path], Field(pattern=r"^https?://.*$")]) -> str:





if __name__ == "__main__":
    mcp.run()
