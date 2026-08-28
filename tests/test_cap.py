from alerting.cap.generator import generate_test_cap

def test_cap_is_test_only():
    xml = generate_test_cap('demo-1','Demo','Not real')
    assert '<status>Test</status>' in xml
    assert '<scope>Restricted</scope>' in xml
