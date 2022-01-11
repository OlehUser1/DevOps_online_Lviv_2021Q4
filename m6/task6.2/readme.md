1. Use already created internal-network for three VMs (VM1-VM3). VM1 has NAT and internal,VM2, VM3 – internal only interfaces.

![image](https://user-images.githubusercontent.com/46942305/148965604-96349516-ba96-4da9-ae30-88788d21bf6d.png)

2. Install and configure DHCP server on VM1. 
3. Check VM2 and VM3 for obtaining network addresses from DHCP server.

DNSMASQ

![image](https://user-images.githubusercontent.com/46942305/148965901-5ee9d56e-68cf-4baa-b483-b91af9faf8da.png)

![image](https://user-images.githubusercontent.com/46942305/148966125-fe545134-71e2-4d7c-9c48-9673fad3a23c.png)

![image](https://user-images.githubusercontent.com/46942305/148966217-54922505-fafa-45d8-89a8-4d58ed573c3d.png)

ISC-DHSPSERVER

![image](https://user-images.githubusercontent.com/46942305/148978810-b90bc9ae-5413-400d-939b-e9481bff87fc.png)

![image](https://user-images.githubusercontent.com/46942305/148979453-090e2b53-5568-4310-b80a-80618ce0b9ef.png)

![image](https://user-images.githubusercontent.com/46942305/148979595-d97954f5-106d-4707-bcf7-8e771c541672.png)

4. Using existed network for three VMs (from p.1) install and configure DNS server on VM1. 
