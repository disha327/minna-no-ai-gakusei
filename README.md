# Minna no AI Gakusei (みんなのAI学生)

A Python project using `uv` and Python 3.12 for AI student portfolio work.

## Setup

This project uses `uv` for dependency management and Python 3.12.

### Prerequisites

1. Install `uv` (if not already installed):
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. Add `uv` to your PATH:
   ```bash
   source $HOME/.local/bin/env
   ```

### Installation

1. Clone the repository
2. Install Python 3.12:
   ```bash
   uv python install 3.12
   ```

3. Create a virtual environment:
   ```bash
   uv venv --python 3.12
   ```

4. Install dependencies:
   ```bash
   uv sync
   ```

### Usage

Run Python scripts using `uv run`:

```bash
# Run the hello world example
uv run python student_portfolio/00_hello_world/main.py
```

### Environment Variables

Create a `.env` file in the root directory with your OpenAI API key:

```
OPENAI_API_KEY=your_api_key_here
```

### Development

- **Format code**: `uv run black .`
- **Lint code**: `uv run flake8 .`
- **Run tests**: `uv run pytest`

## Project Structure

- `student_portfolio/` - Main project directory
  - `00_hello_world/` - Hello world example
  - `reflections/` - Weekly reflections