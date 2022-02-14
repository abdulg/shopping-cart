## Shopping Cart Application
### Installation

Clone the repo then create a virtual environment, activate it and install dependencies:
```shell
git clone git@github.com:abdulg/shopping-cart.git
cd shopping-cart
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Run the tests

Run all the tests:

```shell
pytest
```

Run just the AC tests
```shell
pytest -k __ac
```

Add a `-v` flag to see verbose output
