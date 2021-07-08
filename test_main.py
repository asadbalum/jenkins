from main import user

def test_age():
    agent = user('asad','asad.gmail.com', 25)
    res = agent.tenY()
    assert res == 35