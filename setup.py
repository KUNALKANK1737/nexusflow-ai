from pathlib import Path

# ==========================
# Project Configuration
# ==========================

PROJECT_NAME = "nexusflow-ai"
WORKSPACE = Path("D:/Workspace/Projects")

ROOT = WORKSPACE / PROJECT_NAME

FOLDERS = [
    "apps/backend",
    "apps/frontend",

    "packages/shared",
    "packages/ai-core",
    "packages/ui",

    "docs/product",
    "docs/architecture",
    "docs/adr",
    "docs/api",
    "docs/deployment",

    "infrastructure/docker",
    "infrastructure/nginx",
    "infrastructure/github-actions",

    "scripts",
    "tests",

    ".github/workflows",
]

FILES = [
    "README.md",
    ".gitignore",
    ".env.example",
    "docker-compose.yml",
    "LICENSE",

    "docs/product/vision.md",
    "docs/product/brd.md",
    "docs/product/prd.md",
    "docs/product/roadmap.md",

    "docs/architecture/system-design.md",
    "docs/architecture/database.md",
    "docs/architecture/deployment.md",

    "docs/api/api-spec.md",

    "docs/deployment/deployment-guide.md",

    "docs/adr/ADR-001-project-setup.md",
]


# ==========================
# Helper Functions
# ==========================

def create_folders():
    print("\nCreating folders...\n")

    for folder in FOLDERS:
        path = ROOT / folder
        path.mkdir(parents=True, exist_ok=True)
        print(f"[OK] {folder}")


def create_files():
    print("\nCreating files...\n")

    for file in FILES:
        filepath = ROOT / file

        filepath.parent.mkdir(parents=True, exist_ok=True)

        if not filepath.exists():
            filepath.touch()

        print(f"[OK] {file}")


def create_readme():
    readme = ROOT / "README.md"

    content = f"""# {PROJECT_NAME}

Enterprise AI Workflow Platform

## Tech Stack

- FastAPI
- React
- TypeScript
- LangGraph
- Docker
- GitHub Actions
- AWS
- PostgreSQL
- ChromaDB

"""

    readme.write_text(content, encoding="utf-8")


def create_gitignore():
    gitignore = ROOT / ".gitignore"

    content = """
# Python
__pycache__/
*.pyc
.venv/
.env

# Node
node_modules/
dist/

# VS Code
.vscode/

# Logs
*.log

# OS
.DS_Store
Thumbs.db
"""

    gitignore.write_text(content.strip(), encoding="utf-8")


def create_env():
    env = ROOT / ".env.example"

    content = """
APP_NAME=NexusFlow

ENVIRONMENT=development

SECRET_KEY=

DATABASE_URL=

GEMINI_API_KEY=

OPENAI_API_KEY=
"""

    env.write_text(content.strip(), encoding="utf-8")


def main():
    print("=" * 60)
    print(" NexusFlow Project Bootstrap ")
    print("=" * 60)

    ROOT.mkdir(parents=True, exist_ok=True)

    create_folders()
    create_files()

    create_readme()
    create_gitignore()
    create_env()

    print("\nProject created successfully!")
    print(f"\nLocation:\n{ROOT}")


if __name__ == "__main__":
    main()