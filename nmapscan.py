import subprocess


def scan_network(ip_address, ports):
    command = ["nmap", "-sS", "-T4", "-p", ports, ip_address]
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    if error:
        print(f"Ошибка при сканировании: {error}")
        return None
    else:
        return output.decode("utf-8")


if __name__ == "__main__":
    ip_address = "192.168.1.0/24"
    ports = "1-40"

    scan_results = scan_network(ip_address, ports)

    if scan_results:
        print(f"Результаты сканирования Nmap для {ip_address}:\n{scan_results}")
    else:
        print("Сканирование не удалось.")
