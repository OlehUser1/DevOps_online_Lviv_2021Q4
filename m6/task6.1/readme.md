1. Create virtual machines connection according to figure 1:

![image](https://user-images.githubusercontent.com/46942305/148701033-83738675-b413-47ee-bc5a-49b31a61e82c.png)

2. VM2 has one interface (internal), VM1 has 2 interfaces (NAT and internal). Configure all network
interfaces in order to make VM2 has an access to the Internet (iptables, forward, masquerade).

![image](https://user-images.githubusercontent.com/46942305/148701671-d7333895-0be4-4dfd-9d6f-57ec0f5a35c5.png)

![image](https://user-images.githubusercontent.com/46942305/148701700-b473da01-9e02-4f87-af10-2550a86cc0ca.png)

![image](https://user-images.githubusercontent.com/46942305/148701708-bc19162e-5b6f-4248-ae18-16c9bb8e6a01.png)

![image](https://user-images.githubusercontent.com/46942305/148701715-619d7bde-605d-43be-ad7e-d3c1b6bba702.png)

3. Check the route from VM2 to Host.

![image](https://user-images.githubusercontent.com/46942305/148701793-9200689b-267a-4e6f-8b0f-d22fe3e5bfaa.png)

4. Check the access to the Internet, (just ping, for example, 8.8.8.8).

![image](https://user-images.githubusercontent.com/46942305/148701818-78c4d271-5485-4dcd-8f25-f6b3a8b143ce.png)

5. Determine, which resource has an IP address 8.8.8.8.

![image](https://user-images.githubusercontent.com/46942305/148702058-b9174bae-5963-4db3-bbb8-73eec8953d56.png)

6. Determine, which IP address belongs to resource epam.com.

![image](https://user-images.githubusercontent.com/46942305/148702108-b5ac5bf5-3520-4a9d-8f85-c177cb1231cc.png)

7. Determine the default gateway for your HOST and display routing table.

![image](https://user-images.githubusercontent.com/46942305/148702285-a4fefab9-2843-43a1-9b24-b9dfdfa7e0f9.png)

8. Trace the route to google.com.

![image](https://user-images.githubusercontent.com/46942305/148702164-c2f23fe5-fcb9-41f6-9f52-984dd03f5c4f.png)
