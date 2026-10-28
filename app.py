from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier


def train_model():
    iris = load_iris()

    model = DecisionTreeClassifier(random_state=42)
    model.fit(iris.data, iris.target)

    return model, iris.target_names


def predict_flower():
    model, target_names = train_model()

    # Example flower measurements
    sample = [[5.1, 3.5, 1.4, 0.2]]

    prediction = model.predict(sample)[0]
    flower = target_names[prediction]

    print("Iris Flower Classification")
    print("--------------------------")
    print(f"Prediction: {flower}")

    return flower

#added comment

if __name__ == "__main__":
    predict_flower()