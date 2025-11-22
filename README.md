# chemspace-mcp

A Model Context Protocol (MCP) server that provides a wrapper for the Chemspace API, enabling AI agents to search for synthesizable building blocks and screening compounds through exact, substructure, and similarity searches.

## Features

- **Exact Search**: Find exact molecular matches by SMILES
- **Substructure Search**: Find compounds containing a specific substructure
- **Similarity Search**: Find structurally similar compounds by SMILES
- **Multiple Product Categories**: Search across in-stock and make-on-demand compounds
- **Global Shipping**: Specify shipping countries with ISO country codes

## Requirements

- Python 3.13+
- Chemspace API key

## Installation

### Prerequisites

Install `uv` (universal Python package installer):

```sh
# macOS
brew install uv

# Linux/WSL2  
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Setup

1. Clone the repository and navigate to the project directory

2. Set your Chemspace API key as an environment variable:
   ```bash
   export CHEMSPACE_API_KEY="your-api-key-here"
   ```

3. Install dependencies and run:
   ```bash
   uv run chemspace-mcp
   ```

## Configuration

### For use with FastAgent

Configure `example/fastagent.secrets.yaml`:

```yaml
anthropic:
  api_key: your-anthropic-api-key

mcp:
  servers:
    chemspace:
      env:
        CHEMSPACE_API_KEY: your-chemspace-api-key
```

Then run the example interface with FastAgent:
```bash
cd example
uv run --extra agent agent.py
```

## Usage

The MCP server exposes the following tools:

### search_exact
Searches for exact molecular matches by SMILES string.

**Parameters:**
- `smiles` (string): The SMILES string to search for
- `shipToCountry` (string): Two-letter ISO country code (default: "US")
- `count` (integer): Maximum results per page (default: 10)
- `page` (integer): Page number for pagination (default: 1)
- `categories` (list): Product categories to search:
  - `CSSB`: In-stock building blocks
  - `CSSS`: In-stock screening compounds
  - `CSMB`: Make-on-demand building blocks
  - `CSMS`: Make-on-demand screening compounds
  - `CSCS`: Custom requests

### search_substructure
Searches for compounds containing a specific substructure.

**Parameters:** Same as `search_exact`

### search_similarity
Searches for structurally similar compounds.

**Parameters:** Same as `search_exact`

## Project Structure

```
chemspace-mcp/
├── src/
│   └── chemspace_mcp/
│       ├── __init__.py          # Entry point and MCP server initialization
│       ├── tools.py             # Tool definitions for chemical searches
│       └── tokenmanager.py       # Token management for API authentication
├── example/
│   ├── agent.py                 # Example FastAgent integration
│   ├── fastagent.config.yaml    # FastAgent configuration
│   └── fastagent.secrets.yaml   # Secrets configuration (not in version control)
├── pyproject.toml               # Project metadata and dependencies
└── README.md                    # This file
```

## Development

### Dependencies

- `fastmcp>=2.13.1`: Core MCP server framework
- `fast-agent-mcp>=0.2.25`: FastAgent integration

## License

MIT License

## Support

For issues or questions, please open an issue on the project repository.