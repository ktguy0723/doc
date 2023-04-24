import src.main as main

def test_lambda_handler():
    response = main.lambda_handler(None, None)
    assert response['statusCode'] == 200
    assert response['body'] == 'Hello World'