from pathlib import Path
import re
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "visualizations"
OUT.mkdir(exist_ok=True)

df = pd.read_csv(ROOT / "sample_reviews.csv")

POSITIVE_WORDS = {
    "good", "great", "soft", "softening", "gentle", "fresh", "comfortable",
    "smooth", "pleasant", "hydrating", "absorbs", "quickly", "convenient",
    "clean", "well", "easy", "value"
}
NEGATIVE_WORDS = {
    "bad", "harsh", "drying", "sticky", "expensive", "leaked", "greasy",
    "strong", "awkward", "tight", "unpleasant", "broken", "broke",
    "difficult", "white", "cast"
}

def classify_sentiment(text):
    """Simple word-list baseline for demonstration; not a trained model."""
    words = set(re.findall(r"[a-z]+", str(text).lower()))
    score = len(words & POSITIVE_WORDS) - len(words & NEGATIVE_WORDS)
    if score > 0:
        return "Positive"
    if score < 0:
        return "Negative"
    return "Neutral"

df["predicted_sentiment"] = df["review_text"].apply(classify_sentiment)
df.to_csv(ROOT / "reviews_with_demo_sentiment.csv", index=False)

summary = (
    df.groupby(["category", "predicted_sentiment"])
      .size().unstack(fill_value=0)
)
summary.to_csv(ROOT / "sentiment_summary.csv")

# Plot 1: rating distribution
plt.figure()
df["rating"].value_counts().sort_index().plot(kind="bar")
plt.title("Sample review rating distribution")
plt.xlabel("Rating")
plt.ylabel("Number of reviews")
plt.tight_layout()
plt.savefig(OUT / "rating_distribution.png", dpi=160)
plt.close()

# Plot 2: sentiment counts
plt.figure()
df["predicted_sentiment"].value_counts().reindex(
    ["Positive", "Neutral", "Negative"], fill_value=0
).plot(kind="bar")
plt.title("Rule-based sentiment counts (illustrative sample)")
plt.xlabel("Predicted sentiment")
plt.ylabel("Number of reviews")
plt.tight_layout()
plt.savefig(OUT / "sentiment_counts.png", dpi=160)
plt.close()

# Plot 3: average rating by product
plt.figure()
df.groupby("product_name")["rating"].mean().sort_values().plot(kind="barh")
plt.title("Average rating by product in sample data")
plt.xlabel("Average rating")
plt.ylabel("Product")
plt.tight_layout()
plt.savefig(OUT / "average_rating_by_product.png", dpi=160)
plt.close()

print("Analysis complete.")
print(f"Rows analysed: {len(df)}")
print(f"Outputs saved in: {OUT}")
print("Reminder: this is illustrative sample data and a simple rule-based baseline.")
