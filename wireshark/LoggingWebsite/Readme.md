# HTTP Requests and Headers

## Introduction
This document showcases HTTP GET, PUT, and POST requests along with their headers and information captured during specific interactions.

## Methodology
The requests were captured using Wireshark during the login process on a website.

## HTTP GET Request

#### Example Request:
```http
GET /Login HTTP/1.1\r\n
Host: exam.ioe.edu.np:81\r\n
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36\r\n
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8\r\n
Accept-Language: en-US,en;q=0.6\r\n
Connection: keep-alive
