# Techfest Hackathon Final - Personal Shopping Assistant Agent
Personal Shopping Assistant Agent using uAgent library

# Personal Shopping Assistant Agent

Personal Shopping Assistant Agent is an intelligent agent designed to assist users with various shopping tasks, including product searches, price comparisons, checking product availability, and making purchases on behalf of the user. 

## Setup

### 1. Clone the Project

Clone the project repository using the following command:

```bash
git clone https://github.com/001ak/techfest-HackAI-Final.git
```
### 2. Installation
2.1 Install Poetry
For Linux and macOS:
```bash
curl -sSL https://install.python-poetry.org | python3 -
```
For Windows (Run it in PowerShell):
```bash
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
```
2.2 Install Dependencies
Navigate to the project's python directory and install dependencies using Poetry:
```bash
cd python
poetry install
poetry shell
```

2.3 Install the python-decouple library:
```bash
pip install python-decouple
```
### 3. Dataset
We have created a dataset products.py file that has sample data used for this project.

### 4. Running the Project
First, run shopping_assistant.py in one terminal:
```bash
python shopping_assistant.py
```
It runs on port 8000.

Then, run user_agent.py in another terminal( Again perform **poetry shell** in this new terminal). 
```bash
python user_agent.py 
```
It runs on port 8001


## Description
The shopping assistant agent is running on port 8000, and for each user, a new agent will be created, running on a provided port. Each user should be given a different port number where no other process is running. Each user agent will call the shopping assistant agent after a specific amount of time for shopping-related tasks. The seed for the user agent will be made using the port number, ensuring that each user has a different address. The response from the shopping assistant agent will be sent back to the specific user using the user's address. we used a temporary list for  storing the products(any database can be connected to replace the array)
tasks completed:
    search a product : user can input product name to be searched
    price comparison : price for each type of product is displayed for comparison
    availability : no of available units for each type are displayed
    buying a product : user can input product name and type to buy a product. shopping assistant checks if input product is available or not and makes the purchase 
