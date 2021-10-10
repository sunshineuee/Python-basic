import time


class TrafficLight:
    _colour = 'Red', 'Yellow', 'Green'
    _timer = 7, 2, 5
    condition = 0

    def running(self):
        while True:
            print(self._colour[self.condition])
            time.sleep(self._timer[self.condition])
            if self.condition == 2:
                self.condition = 0
            elif self.condition not in (0, 1, 2):
                print('TrafficLight does not work')
                break
            else:
                self.condition += 1


traffic_lights = TrafficLight()
traffic_lights.running()