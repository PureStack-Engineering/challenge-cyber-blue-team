import pytest
import os
from incident_response import analyze_logs

# Definimos la ruta relativa al archivo de logs
LOG_FILE = os.path.join("data", "server_logs.txt")

def test_evidence_exists():
    """Valida que el archivo de logs existe."""
    assert os.path.exists(LOG_FILE), "❌ El archivo 'data/server_logs.txt' no se encuentra."

def test_identify_attacker():
    """Valida si el candidato encontró la IP correcta."""
    result = analyze_logs(LOG_FILE)
    
    expected_ip = "192.168.1.66"
    
    assert result['attacker_ip'] is not None, "❌ No has identificado ninguna IP (sigue siendo None)."
    assert result['attacker_ip'] == expected_ip, f"❌ IP Incorrecta. Esperaba {expected_ip}, recibí {result['attacker_ip']}"

def test_identify_attack_type():
    """Valida si clasificó el ataque correctamente (Bonus)."""
    result = analyze_logs(LOG_FILE)
    
    # Aceptamos variantes comunes
    valid_types = ["sql injection", "sqli", "injection"]
    detected = result['attack_type'].lower()
    
    assert any(t in detected for t in valid_types), f"❌ Tipo de ataque no reconocido. Esperaba 'SQL Injection', recibí '{detected}'"
