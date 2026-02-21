# Network Traffic Basics

## Task 1 - Introduction

Network Traffic Analysis is a process of capturing, inspecting and analyzing data as it flows in a network.  Its goal is to have complete visibility and understand what is communicated inside and outside the network.

---

## Task 2 - What is The Purpose Of Network Traffic Anaysis ?

### DNS Tunneling and Beaconing

Suppose you are a SOC Analyst, and you receive an alert stating that an unusual number of DNS queries are coming from a host named `WIN-016` with `IP 192.168.1.16`. The DNS logs on the firewall show multiple DNS queries going to the same TLD, each time using a different subdomain.

```
2025-10-03 09:15:23    SRC=192.168.1.16      QUERY=aj39skdm.malicious-tld.com    QTYPE=A      
2025-10-03 09:15:31    SRC=192.168.1.16      QUERY=msd91azx.malicious-tld.com    QTYPE=A     
2025-10-03 09:15:45    SRC=192.168.1.16      QUERY=cmd01.malicious-tld.com       QTYPE=TXT     
2025-10-03 09:15:45    SRC=192.168.1.16      QUERY=cmd01.malicious-tld.com       QTYPE=TXT   
```

Based on DNS logs, we can retrieve the following information:

- Query and querytype
- Subdomain and top-level domain: We can check tools like abuseDB or VirusTotal to check if the domain is malicious
- Host IP: We can identify the system sending out the DNS queries
- Destination IP: We can use tools like AbuseIPDB or VirusTotal to verify if the IP is flagged as malicious
- Timestamp: We can build a timeline mapping out the different suspicious queries

Since the DNS logs doesn't contain any more useful information so we will have to inspect DNS traffic deeply to make a meaningful conclusion.

This scenario best describes why we need Network Traffic Analysis. 

Firewalls and other network devices list DNS quieries and their responses but not content. Threat actors could, for example, use TXT records to send Command and Control instructions to a compromised system. We can discover this by inspecting the content of the DNS queries. 

The packet capture fragment below shows the content of a DNS reply that contains C2 commands:

```
Domain Name System (response)
    Transaction ID: 0x4a2b
    Flags: 0x8180 Standard query response, No error
        1... .... .... .... = Response: Message is a response
        .... .... .... 0000 = RCODE: No error (0)
    Questions: 1
    Answer RRs: 1
    Authority RRs: 0
    Additional RRs: 0
    Queries
        cmd1.evilc2.com: type TXT, class IN
    Answers
        cmd1.evilc2.com: type TXT, class IN, TTL 60, TXT length: 20
            TXT: "SSBsb3ZlIHlvdXIgY3VyaW91c2l0eQ=="
```

### Why should we analyse network traffic?

Generally, we will use network traffic analysis to:

Monitor network performance

- Check for abnormalities in the network. E.g., sudden performance peaks, slow network, etc
- Inspect the content of suspicious communication internally and externally. E.g., exfiltration via DNS, download of a malicious ZIP file over HTTP, lateral movement, etc

From a SOC perspective, network traffic analysis helps:

- Detecting suspicious or malicious activity
- Reconstructing attacks during incident response
- Verifying and validating alerts


Below are two more scenarios that illustrate the importance of network traffic analysis:

- Based on the logs for an end-user system, the system began to deviate from its normal behavior around 4 PM UTC. Analyzing the network traffic going to and from this system, we found a suspicious HTTP request and were able to extract a suspicious ZIP-file

- We received an alert that an end-user system is sending many DNS requests in comparison to baseline of the network. After inspecting the DNS requests, we discovered that data was being exfiltrated using a technique called DNS tunneling

### Answer the questions below

What is the name of the technique used to smuggle C2 commands via DNS?

`DNS Tunneling`

---

## Task 3 - What Network Traffic We Can Observe ?

### Answer the questions below

- Look at the HTTP example in the task and answer the following question: What is the size of the ZIP attachment included in the HTTP response? Note down the answer in bytes.

    #### Answer:

    `10485760`

- Which attack do attackers use to try to evade an IDS?

    `fragmentation`

- What field in the TCP header can we use to detect session hijacking?

    `sequence number`

---

## Task 4 - Network Traffic Sources and Flows

### Answer the questions below

- Which category of devices generates the most traffic in a network?

    `endpoint`

- Before an SMB session can be established, which service needs to be contacted first for authentication?

    `kerberos`

- What does TLS stand for?

    `Transport Layer Security`

---

## Task 5 - How Can We Observe Network Traffic

### Answer the questions below

- What is the flag found in the HTTP traffic in scenario 1? The flag has the format THM{}.


    #### Answer
    
    `THM{FoundTheMalware}`

    #### Explanation

    ![alt text](Images/Network%20Traffic%20Basics/Flag%201.png)

- What is the flag found in the DNS traffic in scenario 2? The flag has the format THM{}.

    #### Answer

    `THM{C2CommandFound}`

    #### Explanation

    ![alt text](Images/Network%20Traffic%20Basics/Flag%202.png)

---
