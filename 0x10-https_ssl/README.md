# 0x10. HTTPS SSL

## Learning Objectives

### General
- **What is HTTPS SSL and its 2 main roles?**
  - HTTPS (Hypertext Transfer Protocol Secure) is an extension of HTTP (Hypertext Transfer Protocol) that is used to secure the transfer of data over the internet. SSL (Secure Sockets Layer) is the predecessor to TLS (Transport Layer Security), and it is the technology used to encrypt the connection between a web server and a user's web browser.

- **What is the purpose of encrypting traffic?**
  - The purpose of encrypting traffic is to secure the communication between a user's web browser and a web server. Encryption ensures that sensitive information, such as login credentials, personal data, or financial information, is transmitted securely and cannot be easily intercepted or tampered with by malicious actors.

- **What does SSL termination mean?**
  - SSL termination refers to the process of decrypting the encrypted SSL/TLS traffic at the web server or load balancer before passing it to the application servers. In other words, SSL termination occurs when the SSL/TLS encryption is removed (terminated) at a certain point in the network, allowing the unencrypted traffic to continue its journey to the web application servers.



