# Efficient Hindi Text Summarization via Knowledge Distillation of MT5 📝

This project focuses on Hindi text summarization using a Hindi news Article [dataset](https://ilsum.github.io/ilsum/2024/index.html) utilizing advanced techniques in natural language processing. Most of the multilingual Models available are quite large in size and require high computaional resources .By leveraging the knowledge distillation of the **mT5** model, we aim to create a more efficient and smaller version of **mT5** (Distill mT5) that retains the essential capabilities for summarizing Hindi texts.

## Demo
<div style="display: flex; justify-content: center;">
    <img src="/demo.png" width="400" style="margin-right: 5px;" />
    <img src="/demo2.png" width="400" />
</div>

## Architecture

This project utilizes a modular architecture for Hindi text summarization through knowledge distillation of the MT5 model. The key components include:

- **Dataset Gathering**: Collecting a relevant dataset of Hindi news articles.
- **Preprocessing**: Cleaning and preparing the data for model training.
- **Indic BART Testing**: Evaluating the **Indic BART model** for baseline performance.
- **MT5 Fine-tuning**: Fine-tuning the **mT5** model on the processed Hindi dataset to adapt it for summarization tasks.
- **Knowledge Distillation**: Creating a distilled version of the **mT5** model to optimize performance and reduce size.
- **Frontend Development**: Building a user-friendly interface using **Streamlit** for displaying summaries.

This architecture ensures an efficient workflow from data collection to model deployment, providing a streamlined experience for users interested in Hindi text summarization.

