from xml.etree.ElementTree import Element, SubElement, tostring

def generate_test_cap(identifier: str, headline: str, description: str) -> str:
    alert = Element('alert')
    SubElement(alert, 'identifier').text = identifier
    SubElement(alert, 'sender').text = 'mountainguard-ai@example.invalid'
    SubElement(alert, 'status').text = 'Test'
    SubElement(alert, 'msgType').text = 'Alert'
    SubElement(alert, 'scope').text = 'Restricted'
    info = SubElement(alert, 'info')
    SubElement(info, 'category').text = 'Safety'
    SubElement(info, 'event').text = 'Educational multi-hazard simulation'
    SubElement(info, 'headline').text = headline
    SubElement(info, 'description').text = description
    return tostring(alert, encoding='unicode')
