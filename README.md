# SMS/EMAIL Spam Predictor

This project focuses on classifying messages as spam or not spam using machine learning techniques. The project includes data cleaning, exploratory data analysis (EDA), and processing using the Natural Language Toolkit (NLTK).

### Steps

- Data cleaning: Removing unwanted characters, converting text to lowercase, etc.
- EDA: Analyzing the distribution of spam and non-spam messages.
- Processing: Tokenization, removing stop words, and stemming/lemmatization.
- Machine learning models: Trying multiple algorithms and selecting a voting classifier (SVC, MultinomialNB, ExtraTreesClassifier) for its high precision score.
- Model evaluation: Using precision score (0.9911) and accuracy score (0.9836) as metrics for model performance.
- Deployment: Using Streamlit to deploy the model for real-time predictions.

### Usage

To run the project locally, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/Veer6693/sms-email-spam-predictor.git
   
Make sure you have the following libraries installed:
- NLTK
- Scikit-learn
- Pandas
- Streamlit

  ```bash
  pip install nltk scikit-learn pandas streamlit

2. Run the Streamlit app:

   ```bash
   streamlit run app.py

3. Open your browser and navigate to http://localhost:8501 to access the web interface for spam prediction.


### Model Improvement
- To improve the model, you can experiment with different algorithms, feature engineering techniques, or hyperparameter tuning.

### Why Precision Score is Important
In SMS/EMAIL spam classification, precision is more important than recall because we want to minimize false positives (i.e., classifying non-spam messages as spam). False positives can be more harmful in this scenario as important messages might be marked as spam, leading to potential loss of information or opportunities.

![Screenshot 2024-02-22 165545](https://github.com/Veer6693/sms-email-spam-predictor/assets/102231617/ef2c181c-02a8-493b-8a65-d3d41aaaf62d)

![Screenshot 2024-02-22 165800](https://github.com/Veer6693/sms-email-spam-predictor/assets/102231617/2981dd20-8360-469d-926b-60181c33945a)

