import os

def analyze_logs(file_path):
    """
    Reads the log file and identifies the attacker.
    
    Args:
        file_path (str): Path to the log file.
        
    Returns:
        dict: A dictionary with 'attacker_ip' and 'attack_type'.
    """
    
    # TODO: Implement log parsing logic here.
    # 1. Read the file
    # 2. Look for suspicious keywords (UNION, SELECT, OR '1'='1)
    # 3. Extract the IP address associated with them.
    
    detected_ip = None
    attack_type = "unknown"
    
    return {
        "attacker_ip": detected_ip, 
        "attack_type": attack_type
    }

if __name__ == "__main__":
    # For manual testing
    result = analyze_logs("data/server_logs.txt")
    print(f"Analysis Result: {result}")
