from fastmcp import FastMCP
from .tools import register_tools
from .tokenmanager import ChemspaceTokenManager

mgr = ChemspaceTokenManager()
mcp = FastMCP(
    "Chemspace MCP",
    instructions="Tools for retrieving synthesizable building blocks via the Chemspace API",
)
register_tools(mcp, mgr)


def main() -> None:
    mcp.run(transport="stdio")
