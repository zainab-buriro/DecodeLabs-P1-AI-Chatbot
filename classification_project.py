import numpy as np
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, classification_report, f1_score

print("🔄 Step 1: Loading Iris Dataset...")
# Load the dataset (contains measurements of 150 flowers) 
iris = load_iris()
X = iris.data  # Features: Sepal length/width, Petal length/width [cite: 77, 82]
y = iris.target  # Target labels: Setosa, Versicolor, Virginica [cite: 77, 82]

print("🔄 Step 2: Scaling Features...")
# StandardScaler scales data to mean=0 and variance=1 to remove bias [cite: 81, 83]
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

print("🔄 Step 3: Splitting Dataset into Train and Test sets...")
# Split data into 80% training and 20% testing. Shuffle=True removes order bias[cite: 76, 81, 85].
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42, shuffle=True)

print("🔄 Step 4: Training the KNN Model...")
# Initialize KNN Classifier with 3 neighbors 
knn_model = KNeighborsClassifier(n_neighbors=3)
knn_model.fit(X_train, y_train)

print("🔄 Step 5: Making Predictions on Test Data...")
# Predict labels for the unseen test data
y_pred = knn_model.predict(X_test)

print("\n📊 --- FINAL MODEL REPORT --- 📊")
# Evaluate the model using standard metrics [cite: 71, 81]
conf_matrix = confusion_matrix(y_test, y_pred)
f1 = f1_score(y_test, y_pred, average='macro')

print("\nConfusion Matrix:")
print(conf_matrix)
print(f"\nF1-Score: {f1:.2f}")  # A score of 1.00 means 100% perfect classification 
print("\nDetailed Classification Report:")
print(classification_report(y_test, y_pred, target_names=iris.target_names))