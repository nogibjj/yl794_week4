# Negative Number Checker

## Overview
Negative Number Checker is a Python-based project that consists of a simple function to determine whether a given number is negative. The project has an organized structure comprising the main functionality, unit tests, and a CI/CD workflow using GitHub Actions.

## Table of Contents
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Testing](#testing)
- [Continuous Integration](#continuous-integration)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Getting Started
To get started with the project, follow the instructions below to set up a local development environment.

### Prerequisites
- Python
- pytest
```sh
pip install pytest
```

### Installation
```sh
# Clone the repository
git clone https://github.com/YourUsername/NegativeNumberChecker.git

# Change to the project directory
cd NegativeNumberChecker

# (Optional) Set up a virtual environment and activate it
python -m venv venv
source venv/bin/activate  # For Windows use `venv\Scripts\activate`

# Install the required packages
pip install -r requirements.txt  # If you have a requirements file
```

## Usage
To use the `negative_number` function from the `main.py` file, run the following command:
```sh
python main.py
```

## Testing
The `testmain.py` file contains the tests for the `negative_number` function. To run the tests, use the following command:
```sh
pytest testmain.py
```

## Continuous Integration
The project uses a GitHub Actions workflow that triggers on `push`, `pull_request`, and `workflow_dispatch` events to the `main` branch. The workflow runs the project in different Python environments, performs linting, runs tests, and formats the code.

Refer to the `.github/workflows/CI.yml` file (replace with your actual workflow file name and path) for the workflow configuration details.

