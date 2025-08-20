def test_home(client):
    response = client.get("/")
    # response.data — это байты, поэтому строку нужно закодировать в UTF-8
    assert "Новости".encode("utf-8") in response.data
