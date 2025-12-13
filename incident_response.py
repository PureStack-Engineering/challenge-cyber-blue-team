import os

class LogAnalyzer:
    """
    Blue Team Challenge:
    Implementa la lógica para analizar logs y detectar IPs maliciosas.
    """
    
    def __init__(self, log_path):
        self.log_path = log_path

    def analyze(self):
        """
        Debe leer el log y devolver un diccionario con:
        1. 'attacker_ip': La IP que más intentos fallidos tiene.
        2. 'attack_type': 'brute_force' si hay más de 3 fallos seguidos en < 1 minuto.
        """
        # TODO: Implementar lógica de análisis forense aquí
        return {
            "attacker_ip": None,
            "attack_type": "unknown"
        }

if __name__ == "__main__":
    # Prueba manual
    analyzer = LogAnalyzer("data/server_logs.txt")
    print(analyzer.analyze())
