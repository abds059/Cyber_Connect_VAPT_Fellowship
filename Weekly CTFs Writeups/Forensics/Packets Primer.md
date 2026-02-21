# Packets Primer

![alt text](image.png)

## Description

Download the packet capture file and use packet analysis software to find the flag.

---

## Solution

Here we are given a file which we have to analyze and find the flag.

After downloading the given file we open it in wireshark.

![alt text](image-1.png)

Upon analyzing the content closely we can observe one frame with `[PSH | ACK]` signifying some data is being pushed.

![alt text](image-2.png)

Upon clicking this frame the flag will be displayed 

![alt text](image-3.png)
