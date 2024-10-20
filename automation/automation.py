mport json

def automated_scan():
    # Pre-Work: Take user input (target URL/IP)
    target = input("Enter the target (URL/IP): ")
    print(f"Target received: {target}")
    
    # For simplicity, assume we run a scan here and get a sample result
    result = {
        "target": target,
        "scan_result": {
            "open_ports": [80, 443],
            "vulnerabilities": ["XSS Detected", "SQL Injection Possible"]
        }
    }

    # Post-Work: Display and save the scan result
    process_results(result)

def process_results(result):
    # Displaying results
    print("\nScan Results:")
    print(f"Target: {result['target']}")
    print(f"Open Ports: {result['scan_result']['open_ports']}")
    print(f"Vulnerabilities Found: {', '.join(result['scan_result']['vulnerabilities'])}")
    
    # Storing results in a file
    with open('scan_results.json', 'w') as file:
        json.dump(result, file)
    print("\nResults saved to 'scan_results.json'.")

if __name__ == "__main__":
    automated_scan()

