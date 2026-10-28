import unittest
from app import train_model, predict_flower


class TestIrisApp(unittest.TestCase):

    def test_model_training(self):
        model, target_names = train_model()

        self.assertEqual(len(target_names), 3)
        self.assertEqual(len(model.classes_), 3)

    def test_prediction(self):
        prediction = predict_flower()

        self.assertIn(
            prediction,
            ["setosa", "versicolor", "virginica"]
        )


if __name__ == "__main__":
    unittest.main()