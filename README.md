# Local LLM Integration & Chatbot for Recipe Suggestions

**Important Note:** The fine-tuned LLM model (`finetuned_model.gguf`) is a large file and is not hosted on GitHub.
Please download it separately from this link:
**[Download `finetuned_model.gguf` from Google Drive](https://drive.google.com/file/d/14WzbiwnGTBZInh_vkw9YkMkoatM3jgdp/view?usp=sharing)**
Make sure to place the downloaded file in the `finetuned_model/` directory of this project.

This project demonstrates how to set up a local Large Language Model (LLM), fine-tune it for recipe suggestions, and integrate it into a user-friendly chatbot interface.

## Key Deliverables

* **Server Setup:** Utilizes Ollama to run a fine-tuned open-source model locally.
* **Fine-Tuning:** The model is fine-tuned on a custom dataset of recipes.
* **API Integration:** A FastAPI endpoint exposes the fine-tuned model, accepting queries and returning JSON responses.
* **Chatbot Development:** A Streamlit-based web UI allows users to interact with the model conversationally.

## Project Structure

```

.
├── finetuned\_model/
│   ├── finetuned\_model.gguf  \# The fine-tuned model in GGUF format (download separately)
│   └── Modelfile             \# Ollama Modelfile for the fine-tuned model
├── unsloth\_finetuning.ipynb  \# Jupyter notebook for fine-tuning the model (run on Colab)
├── api\_endpoint.py           \# FastAPI application to expose the model
└── user\_interface.py         \# Streamlit chatbot UI
├── pyproject.toml            \# Python dependencies
└── README.md                 \# This README file

````

## Setup Instructions

This project is designed to be runnable on a standard Windows/Linux laptop.

### Prerequisites

* **Ollama:** Ensure Ollama is installed on your system. You can download it from [ollama.com](https://ollama.com/).
* **Python:** Python 3.8+ is recommended.
* **uv:** A modern Python package installer and dependency resolver. Install `uv` globally or via pipx: `pip install uv` or `pipx install uv`.

### Step 1: Obtain the Fine-tuned Model

You have two options to get the fine-tuned model:

**Option 1: Run the Fine-tuning Notebook (Recommended for understanding the process)**

1.  Open `unsloth_finetuning.ipynb` in Google Colab (or any Jupyter environment with GPU access).
2.  Run all cells in the notebook. This will fine-tune a base LLM with your recipe dataset and output a GGUF formatted model.
3.  Download the generated `.gguf` model file and place it in the `finetuned_model/` directory.

**Option 2: Use the Provided Fine-tuned Model (Recommended for quick setup)**

If you prefer not to run the fine-tuning process yourself (due to resource limitations or time), you can directly use the pre-trained `finetuned_model.gguf` file. As noted at the beginning of this README, **this file must be downloaded from the provided Google Drive link** and placed into the `finetuned_model/` directory.

### Step 2: Configure Ollama with the Fine-tuned Model

1.  Open your command line or terminal.
2.  Navigate to the `finetuned_model/` directory:
    ```bash
    cd finetuned_model/
    ```
3.  Create the Ollama model using the `Modelfile`:
    ```bash
    ollama create finetuned_model -f Modelfile
    ```
    This command registers your fine-tuned model with Ollama, making it available to be served.

### Step 3: Set up the Python Environment and Run the API

1.  Navigate back to the main project directory (the directory containing `api_endpoint.py` and `user_interface.py`):
    ```bash
    cd .. # Or navigate to your main project directory
    ```
2.  Create a virtual environment using `uv`:
    ```bash
    uv venv
    ```
3.  Activate the virtual environment:
    * **Windows:**
        ```bash
        .venv\Scripts\activate
        ```
    * **Linux/macOS:**
        ```bash
        source .venv/bin/activate
        ```
4.  Install the required Python dependencies:
    ```bash
    uv sync
    ```
    This will install `fastapi`, `uvicorn`, `ollama`, `pydantic`, and `streamlit` from your `pyproject.toml`.

5.  Run the FastAPI backend using Uvicorn:
    ```bash
    uvicorn api_endpoint:app --host 0.0.0.0 --port 8000
    ```
    This will start the API server, typically accessible at `http://127.0.0.1:8000`. Keep this terminal window open and running.

### Step 4: Run the Chatbot UI

1.  Open a **new** command line or terminal window.
2.  Navigate to the main project directory.
3.  Activate the virtual environment (if you haven't already in this new terminal):
    * **Windows:**
        ```bash
        .venv\Scripts\activate
        ```
    * **Linux/macOS:**
        ```bash
        source .venv/bin/activate
        ```
4.  Run the Streamlit chatbot application:
    ```bash
    streamlit run user_interface.py
    ```
    This will open the chatbot UI in your web browser.

## How to Run the Project

1.  Follow "Setup Instructions" completely to get the fine-tuned model, configure Ollama, and set up the Python environment.
2.  Ensure the FastAPI server (`api_endpoint.py`) is running in one terminal (from Step 3).
3.  Ensure the Streamlit UI (`user_interface.py`) is running in another terminal (from Step 4).
4.  Open your web browser and navigate to the address provided by Streamlit (usually `http://localhost:8501`).

## Sample Input and Expected Output

**Sample Input:**

In the chatbot UI, enter:

````

Provide Instructions for recipe.Crispy Salt and Pepper Potatoes

```

**Expected Output:**

The chatbot should respond with a recipe for "Crispy Salt and Pepper Potatoes" similar to the following:

```

Ingredients: ['1 1/2 pounds Russet potatoes, cut into 1/4-inch-thick slices (about 3 cups)', '1 cup all-purpose flour', '1 teaspoon salt', '1/2 teaspoon freshly ground black pepper', '1/2 cup milk or buttermilk', 'Vegetable oil for frying']
Instructions: 'Place 1 tablespoon salt and 1 teaspoon pepper in a shallow dish. Add the potatoes to the dish, tossing gently to coat evenly with the seasoning mixture.
In a separate shallow dish, combine the flour, salt, and pepper. Stir in the milk or buttermilk (you can also make a slurry by whisking together 2 tablespoons flour and 1 tablespoon milk, then whisking into the remaining 3/4 cup milk). Bring a large pot of water to a boil, fill it with ice water, and add the potatoes. Boil for about 10 minutes, until they have doubled in size.
Meanwhile, heat enough oil in a deep frying pan or skillet to reach a temperature of 350°F (175°C). Carefully drain the potatoes on paper towels, allowing any excess water to drip away. Add the potatoes to the hot oil, being careful not to overcrowd the pan. Fry until golden brown and crispy in batches if necessary, about 2 minutes per batch.
Transfer the potatoes to a baking sheet lined with parchment paper. Sprinkle with additional salt and pepper to taste, then bake at 400°F (200°C) for an additional 10-15 minutes, until golden brown on top, if desired.'

```

*(Note: The exact formatting and wording of the ingredients and instructions might vary slightly based on the fine-tuning data and model's generation capabilities, but the core recipe should be provided.)*

## Testing and Verification

To verify the project locally, follow the "How to Run the Project" steps and use the "Sample Input and Expected Output" to confirm the chatbot's functionality. Ensure both the FastAPI server and Streamlit UI are running without errors. You can also test the FastAPI endpoint directly using tools like Postman or `curl` to send POST requests to `http://127.0.0.1:8000/generate/` with a JSON body `{"query": "Provide Instructions for recipe.Crispy Salt and Pepper Potatoes"}`.
```
