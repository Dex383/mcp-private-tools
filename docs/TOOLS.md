# Private Tools Documentation

This directory contains the documentation for the custom tools implemented in the `PrivateTools` MCP server.

## Architecture Overview
The server is built using `FastMCP` and follows a modular architecture. Each functional area (e.g., Web, Repository, System) is isolated into its own module within `src/tools/`.

## Available Tools

### Web Module
Tools focused on retrieving and cleaning information from the internet.

#### `enhanced_search`
- **Description**: Performs a robust search using DuckDuckGo.
- **Parameters**:
  - `query` (string): The search term.
- **Returns**: A formatted list of the top 5 results with title, URL, and snippet.

#### `enhanced_fetch`
- **Description**: Extracts the main textual content from a web page, removing noise (boilerplate).
- **Parameters**:
  - `url` (string): The target URL.
- **Returns**: The cleaned main text of the page.

#### `private_fetch_html`
- **Description**: Fetches the full raw HTML content of a URL.
- **Parameters**:
  - `url` (string): The target URL.
- **Returns**: The complete HTML source code of the page.


### Repository Module
Tools focused on discovering code and models on GitHub and Hugging Face.

#### `search_github_repos`
- **Description**: Searches for the most popular repositories on GitHub based on the query.
- **Parameters**:
  - `query` (string): The search term.
- **Returns**: A formatted list of the top 5 repositories including stars and descriptions.

#### `search_huggingface_models`
- **Description**: Searches for the most downloaded models on Hugging Face based on the query.
- **Parameters**:
  - `query` (string): The search term.
- **Returns**: A formatted list of the top 5 models including downloads and descriptions.

---
*Last Updated: 2026-05-26*

