# NLP-PhsishingModel
# Phishing URL Detection NLP Model

A machine learning project that uses Natural Language Processing (NLP) techniques to detect phishing URLs based on their text patterns and characteristics.

## Project Overview

This project implements a phishing URL detection system using TF-IDF vectorization and Logistic Regression classification. The model analyzes URL text features to identify potentially malicious websites with high accuracy.

## Features

- **Text Vectorization**: Uses TF-IDF with n-grams (1-3) to extract meaningful features from URL text
- **Binary Classification**: Distinguishes between good (0) and bad (1) phishing URLs
- **Performance Metrics**: Comprehensive evaluation including accuracy, precision, recall, and F1 score
- **Feature Analysis**: Identifies and visualizes the top 10 most important phishing indicators
- **Balanced Training**: Uses class weighting to handle potential dataset imbalances

## Requirements

- Python 3.7+
- Required Python packages:
  - pandas
  - matplotlib
  - scikit-learn

Install dependencies:
```bash
pip install pandas matplotlib scikit-learn
```

## Dataset

The model expects a CSV file with the following format:
- **File name**: `phishing_site_urls.csv`
- **Columns**: 
  - `URL` or `url`: The website URL to analyze
  - `Label` or `label`: Classification label ('good' or 'bad')

### Data Requirements
- URLs must be non-null and non-empty
- Labels must be properly formatted ('good' or 'bad')
- Automatic label mapping: 'good' → 0, 'bad' → 1

## Usage

### Basic Execution
Run the main script to train the model and see results:

```bash
python AmroIssa_CRP_NLPmodel.py
```

### Expected Output
The program will display:
1. **Performance Metrics**:
   - Accuracy score
   - Precision score
   - Recall score
   - F1 score

2. **Visualizations**:
   - Top 10 phishing URL indicators (horizontal bar chart)
   - Individual metric charts for each performance score

## Model Architecture

### Vectorization
- **Algorithm**: TF-IDF Vectorizer
- **N-gram Range**: (1, 3) - unigrams, bigrams, and trigrams
- **Max Features**: 10,000 most important features
- **Purpose**: Converts URL text into numerical feature vectors

### Classification
- **Algorithm**: Logistic Regression
- **Solver**: liblinear (optimized for binary classification)
- **Max Iterations**: 1000
- **Class Weight**: Balanced (adjusts for potential dataset imbalances)

### Data Splitting
- **Train/Test Split**: 50/50 ratio
- **Random State**: 42 (ensures reproducible results)

## Performance Metrics

The model is evaluated using four key metrics:

- **Accuracy**: Overall correctness of predictions
- **Precision**: Ratio of true positives to predicted positives
- **Recall**: Ratio of true positives to actual positives
- **F1 Score**: Harmonic mean of precision and recall

## Feature Importance Analysis

The model identifies and ranks the most significant phishing indicators based on coefficient values. These features may include:
- Suspicious domain patterns
- Common phishing keywords
- URL length characteristics
- Special character usage
- Domain name anomalies

## Visualization

The project generates several visualizations:

1. **Top Phishing Indicators**: Horizontal bar chart showing the 10 most important features
2. **Individual Metric Charts**: Separate visualizations for each performance metric

## File Structure

```
project/
├── README.md              # This documentation file
├── AmroIssa_CRP_NLPmodel.py # Main Python script
└── phishing_site_urls.csv # Training dataset (required)
```

## Customization

### Model Parameters
You can modify these parameters in the code:
- `ngram_range`: Adjust the level of text complexity
- `max_features`: Change the number of features considered
- `test_size`: Modify the train/test split ratio
- `random_state`: Ensure reproducibility

### Visualization
- Colors, sizes, and labels can be customized in the plotting functions
- Additional metrics can be added to the evaluation section

## Limitations

- Model performance depends on the quality and representativeness of the training dataset
- May not detect sophisticated phishing techniques not present in training data
- URL-based detection may miss phishing sites that use legitimate domains
- Requires periodic retraining with new phishing patterns

## Future Enhancements

- Implement real-time URL scanning
- Add additional feature extraction methods
- Explore deep learning approaches for better accuracy
- Implement continuous learning with new phishing patterns
- Add web interface for easy URL checking

## Contributing

To contribute to this project:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source and available under the MIT License.

## Contact

For questions or suggestions, please refer to the project maintainer or create an issue in the repository.
