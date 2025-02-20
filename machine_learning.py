# machine_learning.py
import numpy as np
import pandas as pd
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Set seed for reproducibility
np.random.seed(42)

# Simulate a dummy dataset with 500 samples
n_samples = 500
data = {
    'points_accrued': np.random.randint(50, 500, n_samples),
    'transactions': np.random.randint(1, 20, n_samples),
    'referrals': np.random.randint(0, 10, n_samples)
}
df = pd.DataFrame(data)
df['engagement_score'] = 0.05 * df['points_accrued'] + 2.0 * df['transactions'] + 3.0 * df['referrals'] + np.random.normal(0, 5, n_samples)

X = df[['points_accrued', 'transactions', 'referrals']].values
y = df['engagement_score'].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model = Sequential([
    Dense(16, activation='relu', input_shape=(X_train_scaled.shape[1],)),
    Dense(8, activation='relu'),
    Dense(1)
])

model.compile(optimizer='adam', loss='mean_squared_error')
history = model.fit(X_train_scaled, y_train, epochs=50, batch_size=16, validation_split=0.2, verbose=1)
loss = model.evaluate(X_test_scaled, y_test)
print("\nTest Loss (Mean Squared Error):", loss)
predictions = model.predict(X_test_scaled)
print("\nSample Predictions (first 5):", predictions[:5])
model.save('poontoz_model.h5')
