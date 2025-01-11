# Blog Site Autoformatter

A tool to automatically format blog posts according to specified rules.

## Installation

### Prerequisites

**Install UV (Recommended)**
First, install UV for faster dependency management:

```bash
# On Windows.
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

# On macOS and Linux.
curl -LsSf https://astral.sh/uv/install.sh | sh
```


### Install Dependencies

Using UV (recommended):
```bash
uv venv
uv pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

Using pip (alternative):
```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

## Development Setup

### Automatic Dependency Installation
The project uses pre-commit hooks to automatically install new dependencies:

```bash
# Install pre-commit
uv pip install pre-commit

# Set up the git hooks
pre-commit install --install-hooks -t pre-commit -t post-checkout -t post-merge -t post-rewrite

# Now any changes to requirements.txt will trigger automatic installation
```

### Managing Dependencies
1. Add new dependencies to `requirements.in`:
```bash
# Example: Add new package
echo "requests" >> requirements.in
```

2. The pre-commit hooks will automatically:
   - Generate/update the lockfile
   - Sync your environment with the locked dependencies
   - Keep requirements.txt updated

You can also manually update dependencies:
```bash
uv pip compile requirements.in -o requirements.txt
uv pip sync requirements.txt
```

## Usage

```bash
python main.py --input input.txt --config config.json
```

Or pipe content directly:

```bash
echo "Your text here" | python main.py
```

## Configuration

Edit `config.json` to customize formatting rules:
- `line_length`: Maximum characters per line
- `paragraph_spacing`: Number of newlines between paragraphs
- `capitalize_headings`: Whether to capitalize headings
- `normalize_quotation_marks`: Convert quotes to standard format

## Testing

Run the tests using pytest:
```bash
pytest tests/
```

This will run all test cases and verify the analyzer's functionality.
