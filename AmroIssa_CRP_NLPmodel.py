import pandas as pd
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Load CSV file
file_path = "phishing_site_urls.csv"
df = pd.read_csv(file_path)
df = df.rename(columns={'URL': 'url', 'Label': 'label'})

# Clean data
df = df[df['url'].notnull() & df['label'].notnull()]
df = df[df['url'].str.strip() != '']
df['label'] = df['label'].str.strip().map({'bad': 1, 'good': 0})

# Vectorize URLs
vectorizer = TfidfVectorizer(ngram_range=(1, 3), max_features=10000)
X = vectorizer.fit_transform(df['url'])
y = df['label']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=42)

# Train model
model = LogisticRegression(max_iter=1000, class_weight='balanced', solver='liblinear')
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluate
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

print(f"Accuracy: {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall: {recall:.4f}")
print(f"F1 Score: {f1:.4f}")

# Top 10 phishing features
feature_names = vectorizer.get_feature_names_out()
coefs = model.coef_[0]
top_indices = coefs.argsort()[-10:][::-1]
top_features = [feature_names[i] for i in top_indices]
top_weights = [coefs[i] for i in top_indices]

# Plot Top Phishing Indicators
plt.figure(figsize=(10, 6))
plt.barh(top_features[::-1], top_weights[::-1], color='crimson')
plt.xlabel("Coefficient (Importance)")
plt.title("Top 10 Phishing URL Indicators")
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()

# Function to plot a single metric
def plot_metric(name, value, color):
    plt.figure(figsize=(4, 5))
    bar = plt.bar([name], [value], color=color)
    plt.ylim(0, 1.1)
    plt.ylabel("Score")
    plt.title(f"{name} Score")
    plt.text(bar[0].get_x() + bar[0].get_width() / 2, bar[0].get_height() + 0.01,
             f'{value:.4f}', ha='center', va='bottom', fontsize=12, fontweight='bold')
    plt.grid(axis='y', linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.show()

# Display four separate metric charts
plot_metric("Accuracy", accuracy, 'dodgerblue')
plot_metric("Precision", precision, 'darkorange')
plot_metric("Recall", recall, 'seagreen')
plot_metric("F1 Score", f1, 'orchid')
