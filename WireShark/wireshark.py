import pyshark

def extract_dns_queries(pcap_file):
    try:
        # Open the pcap file with a display filter for DNS
        capture = pyshark.FileCapture(
            pcap_file,
            display_filter='dns',
            tshark_path=r"E:\CSIT\CyberConnect VAPT Fellowship\WiresharkPortable64\App\Wireshark\tshark.exe"
        )

        print("Source IP\t\tQueried Domain")
        print("-" * 50)

        for packet in capture:
            # Ensure packet has IP and DNS layers
            if hasattr(packet, 'ip') and hasattr(packet, 'dns'):
                
                # Only process DNS queries (not responses)
                if hasattr(packet.dns, 'qry_name'):
                    source_ip = packet.ip.src
                    queried_domain = packet.dns.qry_name
                    
                    print(f"{source_ip}\t{queried_domain}")

        capture.close()

    except Exception as e:
        print(f"Error processing pcap: {e}")


if __name__ == "__main__":
    pcap_path = "captured_traffic.pcapng"  
    extract_dns_queries(pcap_path)