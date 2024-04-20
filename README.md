# TheTechies- Emergency Vehicle Traffic Control System

### Problem Statement: 
Optimizing Traffic Control for Emergency Vehicles:  This project aims to develop a traffic management system that prioritizes the passage of emergency vehicles through intersections. By implementing Google Maps API to detect traffic congestion and an app for engaging the traffic clearing system, the system will dynamically adjust traffic signals to provide immediate green signal to approaching emergency vehicles while halting opposing traffic. The objective is to minimize response times for emergency services, enhance road safety, and potentially save lives by streamlining the flow of traffic specifically for emergency vehicles.

### Significance of the problem:
The problem statement focuses on preventing emergency vehicles having to slow down or stop in traffic. By prioritizing the passage of emergency vehicles through intersections, this project addresses a critical need in modern planning and emergency response systems. By streamlining traffic flow specifically for emergency vehicles, this project has the potential to save lives and significantly improve the effectiveness of emergency response efforts in urban areas.

### Proof of Concept:
https://drive.google.com/file/d/1lyyFly5uF7OjvEw6H4K729PLEshnMsg2/view?usp=sharing

### Solution:
Our proposed solution involves the development of a simple but efficient traffic management system tailored specifically for prioritizing the passage of emergency vehicles through intersections. 

- *Integration with Google Maps API*: Integrating the Google Maps API to obtain real-time traffic data and identify congestion points. This will enable the system to accurately detect areas where traffic is there and will aloow clearing of the traffic before the emergency vehicle even reaches the intersection
- *Development of a User-Friendly App*: Designing and developing an intuitive app that allows emergency responders to engage with the traffic clearing system. Through the app the first responders will put the location for pickup of patient and when confirmed the Traffic clearing system will activate allowing free passage
- *Dynamic Traffic Signal Adjustment*: The system will detect all traffic signals onroute to the emergency situation and then clear up the traffic when the vehicle reaches a certain distance away from the signal. By doing this the traffic will be cleared by the time the vehicle reaches the intersection allowing quick passage.

Overall, our solution aims to optimize traffic control for emergency vehicles, minimize response times, enhance road safety, and ultimately save lives by efficiently managing traffic flow through intersections in cities.


### Prototype: 
https://www.figma.com/file/JnqXynRlOQVjWTj8RPReYn/Untitled?type=design&node-id=0-1&mode=design&t=ZnrW1wtJGFfzXeJd-0

### Implementation:

## Concept: 
Method 1: The proposed methodology was to ensure that when an emergency vehicles approaches the traffic signal, it should by default go into the free left turn lane (aka left lane) so that the emergency vehicle can get out of that traffic and then go whichever direction it was already heading. In this concept all the 4 sides of traffic with have a free left always on so as to empty out the traffic efficiently. This method can be used by the emergency vehicles to cut through that traffic stop (incase it is a red light) and reach the destination safe and as quickly as possible. This doesnt mean the emergency vehicle has to take a left turn using this free left turn lane, but to be able to just get out of that traffic stop and then go towards whatever direction it has to go.

Method 2: This method is using reinforced learning to pass ambulance to send a signal to the traffic light to turn green at the most optimised time so that the ambulance doesnt slow down due to traffic and other people in the other lanes are not waiting for too long for the ambulance to pass.

## Simulation:
Tech Stack: Simulating the working through Pygame, Python

### Proposed Diagram:

![Diagram](https://github.com/s-sukriti/TheTechies/blob/main/images/Ambulance.jpg)

### Output

![Diagram](https://github.com/s-sukriti/TheTechies/blob/main/images/Simulation_demo.jpg)

### Simulation

Link - https://drive.google.com/file/d/1WmgE2krdv2RT3w1JHurGiVEeWIOMYA-3/view?usp=sharing
