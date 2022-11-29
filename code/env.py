import sys

class Regressor:
    def __init__(self):
        self.w = 0
        self.b = 0

    def forward(self, x):
        return self.w * x + self.b

    def loss(self, x, y):
        return (self.forward(x) - y) ** 2

    def grad(self, x, y):
        y_hat = self.forward(x)
        return (y_hat - y) * x, (y_hat - y)

print('Content-Type: text/plain; charset=UTF-8')
print('Status: 200')
print()

if len(sys.argv) < 6:
    print("You didn't provide enough parameters!")
else:
    lb = int(sys.argv[1].split('=')[1])
    ub = int(sys.argv[2].split('=')[1])
    step_size = int(sys.argv[3].split('=')[1])

    w = float(sys.argv[4].split('=')[1])
    b = float(sys.argv[5].split('=')[1])

    x_test = float(sys.argv[6].split('=')[1])

    x_train = [x for x in range(lb, ub, step_size)]
    y_train = [w * x + b for x in x_train]

    model = Regressor()
    lr = 0.01
    n_epochs = 100

    for epoch in range(n_epochs):
        err = 0.0
        grad_w = 0.0
        grad_b = 0.0

        for (x, y) in zip(x_train, y_train):
            (dLdw, dLdb) = model.grad(x, y)
            grad_w += dLdw
            grad_b += dLdb
            err += model.loss(x, y)

            model.w -= lr * grad_w
            model.b -= lr * grad_b

    y_test = model.forward(x_test)
    print(f"Prediction: {y_test}")
