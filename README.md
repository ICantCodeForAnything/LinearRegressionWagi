# Linear-Regression-Wagi-Python

Demo of executing a python script in Wagi deployed on knative

## Running the demo

Python files are placed in './code' directory.

Run `make serve` to start wagi.

Pass the script name as the first argument

Pass parameters to the model as get parameters

```
$ curl -X GET 'http://localhost:3000?lb=1&ub=5&step=1&w=2&b=5&pred=10'
```
