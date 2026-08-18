import time

class RollingStock:
    def __init__(self, model, type, gauge_type):
        self.model = model
        self.type = type
        self.gauge_type = gauge_type

    def trainDescription(self):
        return f"RollingStock(Model: {self.model}, Type: {self.type}, Gauge Type: {self.gauge_type})"

class PassengerTrain(RollingStock):
    def describe(self):
        return f"PassengerTrain(Model: {self.model}, Type: {self.type}, Gauge Type: {self.gauge_type})"

class FreightTrain(RollingStock):
    def describe(self):
        return f"FreightTrain(Model: {self.model}, Type: {self.type}, Gauge Type: {self.gauge_type})"

class HighSpeedTrain(RollingStock):
    def describe(self):
        return f"HighSpeedTrain(Model: {self.model}, Type: {self.type}, Gauge Type: {self.gauge_type})"

class TrainFactory:
    @staticmethod
    def create_train(train_type, model, type, gauge_type):
        if train_type == "passenger":
            return PassengerTrain(model, type, gauge_type)
        elif train_type == "freight":
            return FreightTrain(model, type, gauge_type)
        elif train_type == "highspeed":
            return HighSpeedTrain(model, type, gauge_type)
        else:
            raise ValueError("Invalid train type")

def main():
   print("Welcome to the Yuan's Rolling Stock Factory! We make Trains!")
   time.sleep(0.5)
   print("This is a demonstration of the Design Pattern in Python.")
   time.sleep(0.5)
   print("For the unittest, please run 'python3 src/test.py'.")
   time.sleep(0.5)
   print("Running factory...")
   time.sleep(1)
   print("Creating sample trains...")
   time.sleep(1)
   print("Almost there...")
   time.sleep(2)
   print("Done! Sample trains created:")

   sample_data = [
       ("passenger", "6767 Series", "EMU", "narrow-gauge"),
       ("freight", "Class YM67", "Diesel Locomotive", "narrow-gauge"),
       ("highspeed", "E670y Series", "EMU", "standard-gauge")
   ]

   for train_type, model, type, gauge_type in sample_data:
       train = TrainFactory.create_train(train_type, model, type, gauge_type)
       print(train.describe())

def end():
    time.sleep(1)

    print("Please run test.py to see the unittest results.")

if __name__ == "__main__":
    main()
    end()