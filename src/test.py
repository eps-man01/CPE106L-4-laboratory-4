import unittest
from main import TrainFactory

class TestTrainFactory(unittest.TestCase):
    def test_passenger_train(self):
        train = TrainFactory.create_train("passenger", "6767 Series", "EMU", "narrow-gauge")
        self.assertEqual(train.describe(), "PassengerTrain(Model: 6767 Series, Type: EMU, Gauge Type: narrow-gauge)")

    def test_freight_train(self):
        train = TrainFactory.create_train("freight", "Class YM67", "Diesel Locomotive", "narrow-gauge")
        self.assertEqual(train.describe(), "FreightTrain(Model: Class YM67, Type: Diesel Locomotive, Gauge Type: narrow-gauge)")

    def test_highspeed_train(self):
        train = TrainFactory.create_train("highspeed", "E670y Series", "EMU", "standard-gauge")
        self.assertEqual(train.describe(), "HighSpeedTrain(Model: E670y Series, Type: EMU, Gauge Type: standard-gauge)")


if __name__ == "__main__":
    unittest.main()