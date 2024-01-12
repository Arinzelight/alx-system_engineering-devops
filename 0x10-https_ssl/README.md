# 0x10. HTTPS SSL

## Learning Objectives

### General
- **What is HTTPS SSL and its 2 main roles?**
  - HTTPS (Hypertext Transfer Protocol Secure) is an extension of HTTP (Hypertext Transfer Protocol) that is used to secure the transfer of data over the internet. SSL (Secure Sockets Layer) is the predecessor to TLS (Transport Layer Security), and it is the technology used to encrypt the connection between a web server and a user's web browser.

- **What is the purpose of encrypting traffic?**
  - The purpose of encrypting traffic is to secure the communication between a user's web browser and a web server. Encryption ensures that sensitive information, such as login credentials, personal data, or financial information, is transmitted securely and cannot be easily intercepted or tampered with by malicious actors.

- **What does SSL termination mean?**
  - SSL termination refers to the process of decrypting the encrypted SSL/TLS traffic at the web server or load balancer before passing it to the application servers. In other words, SSL termination occurs when the SSL/TLS encryption is removed (terminated) at a certain point in the network, allowing the unencrypted traffic to continue its journey to the web application servers.


# Installing Certbot in your HAproxy Load Balancer Server

## Step 1: Log in to your load balancer server with its IP address (E.g 54.152.60.213
vagrant@ubuntu-focal:~$ ssh ubuntu@54.152.60.213

## Step 2: Check if HAproxy is installed
haproxy -v
ubuntu@135836-lb-01:~$ haproxy -v
HA-Proxy version 2.0.29-0ubuntu1.3 2023/02/13 - https://haproxy.org/

## Step 3: Install certbot with the command below
ubuntu@135836-lb-01:~$ sudo snap install --classic certbot
Mount snap "certbot" (2913)                                                                 /
certbot 2.5.0 from Certbot Project (certbot-eff✓) installed

## Step 4: Stop HAproxy from running
ubuntu@135836-lb-01:~$ sudo service haproxy stop
ubuntu@135836-lb-01:~$

## Step 5: Generate your SSL certificate for your domain/subdomain (E.g michaelharry.tech) and respond accordingly to the prompts.
sudo certbot certonly --standalone -d www.michael.tech

Output:
ubuntu@135836-lb-01:~$ sudo certbot certonly --standalone -d www.devniyi.tech
Saving debug log to /var/log/letsencrypt/letsencrypt.log
Enter email address (used for urgent renewal and security notices)
 (Enter 'c' to cancel): samagbeyigbeminiyi@gmail.com

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Please read the Terms of Service at
https://letsencrypt.org/documents/LE-SA-v1.3-September-21-2022.pdf. You must
agree in order to register with the ACME server. Do you agree?
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
(Y)es/(N)o: Y

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Would you be willing, once your first certificate is successfully issued, to
share your email address with the Electronic Frontier Foundation, a founding
partner of the Let's Encrypt project and the non-profit organization that
develops Certbot? We'd like to send you email about our work encrypting the web,
EFF news, campaigns, and ways to support digital freedom.
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
(Y)es/(N)o: N
Account registered.
Requesting a certificate for www.devniyi.tech

Successfully received certificate.
Certificate is saved at: /etc/letsencrypt/live/www.devniyi.tech/fullchain.pem
Key is saved at:         /etc/letsencrypt/live/www.devniyi.tech/privkey.pem
This certificate expires on 2023-07-13.
These files will be updated when the certificate renews.
Certbot has set up a scheduled task to automatically renew this certificate in the background.

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
If you like Certbot, please consider supporting our work by:
 * Donating to ISRG / Let's Encrypt:   https://letsencrypt.org/donate
 * Donating to EFF:                    https://eff.org/donate-le
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
ubuntu@135836-lb-01:~$

## Step 6: Create the directory certs
sudo mkdir -p /etc/haproxy/certs

## Step 7: Combine the certificate and the key generated from step 5 into a .pem file in your certs directory
#use a variable to store the domain name
#combine the keys
DOMAIN='www.devniyi.tech' sudo -E bash -c 'cat /etc/letsencrypt/live/$DOMAIN/fullchain.pem /etc/letsencrypt/live/$DOMAIN/privkey.pem > /etc/haproxy/certs/$DOMAIN.pem'


## Step 8: Change the mode of the file
sudo chmod -R go-rwx /etc/haproxy/certs

## Step 9: Add the following lines to your front_end in your haproxy config file
#open the file
sudo vim /etc/haproxy/haproxy.cfg
#lines to add 
bind *:443 ssl crt /etc/haproxy/certs/domain.pem
redirect scheme https if !{ ssl_fc }


...
frontend http_front
        bind *:80
        bind *:443 ssl crt /etc/haproxy/certs/www.devniyi.tech.pem
        redirect scheme https code 301 if !{ ssl_fc }
        default_backend http_back
...

## Step 10: Check if the configuration file is valid
sudo haproxy -f /etc/haproxy/haproxy.cfg -c

## Step 11: Run this command to correct the DH parameter error
sudo openssl dhparam -out /etc/haproxy/dhparams.pem 2048

## Step 12: Add the line below to your config file, as the last line of the global section
ssl-dh-param-file /etc/haproxy/dhparams.pem


## Step 13: Restart your haproxy
sudo systemctl restart haproxy.service





