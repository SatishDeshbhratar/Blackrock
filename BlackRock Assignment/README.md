# Black Rock Case Study

This project simulates a discrete time dynamical system and consists of a simple backend implementation.

## Setup

To initialize the project, follow these steps:

1. Clone the repository to your local machine.
2. Navigate to the `backend` directory.
3. Set up a Python virtual environment with `python -m venv venv` and activate it. For windows in command prompt - `venv\Scripts\activate` and For macOS or Linux in bash, sh, zsh, or dash - `source venv/bin/activate`
4. Install the required dependencies with `pip install -r requirements.txt`.
5. To run the development server, use `uvicorn simulation:app --reload` from within the `backend` directory.

## Testing

To run unit tests, use the following command from within the `backend` directory:

```bash
python -m unittest discover -v
```

## Infrastructure

The `infrastructure` directory contains Terraform configuration files for deploying the application to AWS. Note there might be other variables required for the actual deployment as per the requirements.
