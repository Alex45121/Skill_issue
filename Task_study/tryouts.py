class Perseptron:
    def __init__(self, num_inputs=2, weights=[2,1]):
        self.num_inputs = num_inputs
        self.weights = weights

    def weight_sum(self,inputs):
        weighted_sum = 0
        for i in range(self.num_inputs):
            weighted_sum += inputs[i] * self.weights[i]
        return weighted_sum

    def activation(self, weighted_sum):
        if weighted_sum >= 0:
            return 1
        else:
            return -1

    def training(self,training_set):
        found_line = False
        while not found_line:
            total_error = 0
            for inputs in training_set:
                predictions = self.activation(self.weight_sum(inputs))

                real = training_set[inputs]
                error = real - predictions
                total_error = abs(error)
                for i in range(self.num_inputs):
                    self.weights[i] += error * inputs[i]
            if total_error == 0:
                found_line = True



cool_perseptron = Perseptron()
small_training_set = {(0,3):1, (3,0):-1, (0,-3):-1, (-3,0):1}

print(cool_perseptron.training(small_training_set))