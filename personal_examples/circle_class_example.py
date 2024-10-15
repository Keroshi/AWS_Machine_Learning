class Car:
    def __init__(self):
        self.speed = 0
        self.acceleration = 0

    class Motor:
        def __init__(self):
            self.horsepower = 0
            self.capacity = 0

    class Tire:
        class Rubber:
            def __init__(self):
                self.no_of_threads = 0

        class Wheel:
            def __init__(self):
                self.no_of_spokes = 0
