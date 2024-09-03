# SmartHoneypot
docker build -t honeypot .
docker run -d -p 2222:2222 -p 8080:8080 -p 23:23 -p 3389:3389 honeypot