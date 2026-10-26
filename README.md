# Beauty & Wellness Customer Sentiment Analysis

## Project overview
This project demonstrates how customer reviews for beauty and skincare products can be analysed to identify common positive and negative themes and support more informed product discovery.

## Business problem
Online beauty shoppers often see star ratings but may not easily understand why customers like or dislike a product. This project demonstrates a simple, transparent approach to classifying review sentiment and summarising recurring review themes.

## Objectives
- Explore sample customer-review data.
- Demonstrate rule-based sentiment classification.
- Summarise sentiment by product and product aspect.
- Visualise rating and sentiment patterns.
- Outline how a future recommendation prototype could use product attributes and customer preferences.

## Files
- `sentiment_analysis.py` — reproducible Python analysis.
- `sample_reviews.csv` — illustrative sample data created for demonstration.
- `requirements.txt` — Python dependencies.
- `Beauty_Wellness_Data_Science_Report.pdf` — report, if included.
- `visualizations/` — generated charts.

## Run the project
Install dependencies:
```bash
pip install -r requirements.txt
```
Run:
```bash
python sentiment_analysis.py
```
The script creates charts in `visualizations/` and a summary CSV named `sentiment_summary.csv`.

## Important data note
`sample_reviews.csv` is a small illustrative dataset created for demonstrating the workflow. It is **not** a representative real-world market dataset and should not be used to make claims about actual customers or brands. For a full study, replace it with a publicly available dataset whose provenance, licence and permitted use have been checked.

## Methods and limitations
The script uses a simple word-list baseline for sentiment, not a trained machine-learning model. It is suitable for demonstrating a workflow but can miss negation, sarcasm, context, spelling variation and mixed-language reviews. A serious study should use a labelled dataset, a held-out test set, and metrics such as macro-F1 and per-class precision/recall.

## Ethical considerations
Do not infer medical conditions or sensitive personal traits from reviews. Review sentiment does not establish product safety or effectiveness. Follow the source dataset's licence and privacy requirements.

## Next steps
1. Select and document an appropriate public dataset.
2. Audit missing values, duplicates, rating distribution and class balance.
3. Compare a simple baseline with a supervised NLP model if reliable labels are available.
4. Evaluate recommendation relevance only if appropriate interaction data exists.
