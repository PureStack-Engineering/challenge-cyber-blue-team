import pytest
from incident_response import analyze_logs

LOG_FILE = "data/server_logs.txt"

def test_structure_exists():
    """Validates that the function returns a dictionary"""
    result = analyze_logs(LOG_FILE)
    assert isinstance(result, dict), "The function must return a dictionary"
    assert "attacker_ip" in result
    assert "attack_type" in result

def test_detect_attacker_ip():
    """
    Validates if the logic correctly identifies the IP 
    generating SQL Injection patterns.
    """
    result = analyze_logs(LOG_FILE)
    
    # Check if logic is implemented
    if result["attacker_ip"] is None:
        pytest.fail("❌ Logic not implemented: attacker_ip is None")
        
    assert result["attacker_ip"] == "192.168.1.66", \
        f"❌ Incorrect IP detected. Expected '192.168.1.66', got '{result['attacker_ip']}'"

def test_classify_attack():
    """
    Validates if the attack is correctly classified 
    as 'sql_injection' based on keywords (UNION, SELECT, OR '1'='1)
    """
    result = analyze_logs(LOG_FILE)
    
    expected_types = ["sql_injection", "sqli"]
    detected = str(result["attack_type"]).lower()
    
    assert any(x in detected for x in expected_types), \
        f"❌ Incorrect Classification. Expected 'sql_injection', got '{result['attack_type']}'"
