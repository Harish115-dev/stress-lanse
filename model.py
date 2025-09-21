# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


# Load data
data = pd.read_csv('students.csv')
df = pd.DataFrame(data)

# Features and target
feature_cols = [
	"Age",
	"Academic Pressure",
	"Study Satisfaction",
	"Study Hours",
	"Financial Stress"
]
# Encode categorical columns
cat_cols = [
	"Gender",
	"Sleep Duration",
	"Dietary Habits",
	"Have you ever had suicidal thoughts ?",
	"Family History of Mental Illness"
]
df_encoded = pd.get_dummies(df, columns=cat_cols, drop_first=True)



# Final feature set: only numeric and one-hot columns
exclude_cols = [col for col in df_encoded.columns if df_encoded[col].dtype == 'object']
X = df_encoded.drop(columns=exclude_cols + ['Depression'])

# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import joblib


data = pd.read_csv('Stress_Dataset.csv')
df = pd.DataFrame(data)

# Use all columns except target and Gender as features
target_col = 'Which type of stress do you primarily experience?'
feature_cols = [col for col in df.columns if col != target_col and col != 'Gender']
X = df[feature_cols]
# Encode target as categorical labels
le = LabelEncoder()
y = le.fit_transform(df[target_col])

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train multi-class model
model = LogisticRegression(random_state=42, max_iter=1000, multi_class='multinomial')
model.fit(X_train_scaled, y_train)

# Evaluate
y_pred = model.predict(X_test_scaled)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy:.2f}")
print(classification_report(y_test, y_pred, target_names=le.classes_))

# Save model, scaler, feature names, and label encoder
joblib.dump(model, 'model.joblib')
joblib.dump(scaler, 'scaler.joblib')
joblib.dump(le, 'label_encoder.joblib')
import json
with open('model_features.json', 'w') as f:
    json.dump(list(X.columns), f)
