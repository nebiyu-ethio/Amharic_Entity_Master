# EthioMart Telegram E-commerce Hub - Amharic Named Entity Recognition (NER)

## Overview

EthioMart aims to become the primary hub for all Telegram-based e-commerce activities in Ethiopia. With the growing use of Telegram for business, many independent e-commerce channels have emerged, presenting challenges for both vendors and customers. EthioMart's goal is to create a centralized platform to consolidate real-time data from these multiple channels, providing a seamless experience for product discovery and interaction.

This project focuses on fine-tuning a large language model (LLM) for Amharic Named Entity Recognition (NER). The system will extract key business entities such as product names, prices, and locations from text, images, and documents shared across Telegram e-commerce channels. The extracted data will populate EthioMart’s centralized database, making it a comprehensive e-commerce hub.

## Key Objectives

- Real-time data extraction from Telegram channels
- Fine-tuning LLMs to extract entities such as product names, prices, and locations
- Creating a unified, searchable database for customers

## Possible Entities

- **Product Names** or Types
- **Materials** or Ingredients
- **Location Mentions**
- **Monetary Values** or Prices

## Data

- **Sources**: Messages and data from Ethiopian-based Telegram e-commerce channels
- **Types**:
  - Text (Amharic language messages)
  - Images (Product images, marketing materials)

## Technologies and Tools

- **Text Processing**: Handling Amharic text, tokenization, and preprocessing techniques.
- **LLM Fine-tuning**: Adapting large language models for Amharic NER tasks.
- **Model Evaluation**: Using metrics such as F1-score, precision, and recall to compare model performance.
- **Model Interpretability**: Using tools like SHAP and LIME to explain model predictions.

## Learning Outcomes

By the end of the project, the following outcomes are expected:

- A fully functional pipeline for extracting entities from Amharic Telegram messages
- Comparative analysis of models and their interpretability
- Insights into how the extracted data can drive business intelligence in the e-commerce space

## Tasks Breakdown

### Task 1: Data Ingestion and Preprocessing

- Set up a data ingestion system to fetch messages from Ethiopian-based Telegram e-commerce channels.
- Preprocess the data for NER tasks (tokenization, normalization, and structuring).

### Task 2: Data Labeling

- Label a subset of the data in CoNLL format.
- Entities: Product names, locations, and prices.

### Task 3: Model Fine-tuning

- Fine-tune an LLM (such as XLM-Roberta or AfroXLMR) for the NER task.
- Train and evaluate using the labeled data.

### Task 4: Model Comparison

- Compare multiple models (e.g., XLM-Roberta, BERT) for their NER performance.
- Select the best-performing model based on speed, accuracy, and robustness.

### Task 5: Model Interpretability

- Implement SHAP and LIME for model interpretability to explain entity extraction.

## Installation and Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/nebiyu-ethio/Amharic_Entity_Master.git
    cd Amharic_Entity_Master
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Set up the environment for model training (e.g., Google Colab or local GPU setup).

4. Ingest the data from Telegram channels using the provided scripts.


## References

- [Hugging Face NER Guide](https://huggingface.co/tasks/token-classification)
- [SHAP Documentation](https://shap.readthedocs.io/en/latest/)
- [LIME Repository](https://github.com/marcotcr/lime)
- [Amharic NER Dataset](https://github.com/uhh-lt/ethiopicmodels)

## License

This project is licensed under the MIT License.
