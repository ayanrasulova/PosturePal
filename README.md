# PosturePal 
The smart, wearable posture assistant using IMU technology to track and correct posture in real-time.
Entry for HooHacks 2025, submitted by Ayan Rasulova, Emilie Deadman, Amelia Chen, Jack Ellis

## Inspiration
As computer science majors, our team understands the strain of spending long hours at a desk, often leading to poor posture and back pain. To address this, we developed PosturePal— a tool designed to help users maintain better posture through a simple, user-friendly interface.

PosturePal is built for anyone who spends extended periods sitting, whether students, professionals, or remote workers. By providing real-time feedback, it encourages better posture habits without being intrusive, making it easier to stay comfortable and avoid long-term strain.

## What it does
PosturePal uses accelerometer data to track the posture of its user. This data is transmitted over radio-frequency waves using a RFNano microcontroller. A second RFNano receives this transmission, unpacking the data being sent. The two devices have prenegotiated that the data will be transmitted as an array of three floats, which represent the force of gravity in the X axis, Y axis, and Z axis respectively. This data is then transmitted to the computer using serial communication through a USB port. 

Then, the numbers are ran through an algorithm to determine a "posture quality score." This score is then displayed through our "live tracker" feature in the form of a graph, tracking a user's general changes in their posture over time. When a user's posture reaches a negative range, the webapp displays this to inform them and help them correct their spine. 

## How we built it
For the hardware, we needed to combine a power supply greater than 5 volts, an IMU to measure the necessary data, an RF Nano for wireless communication and a charging circuit to keep the batteries going after they lose their initial charge. As it was easy to collect from various uva students, the batteries used are reclaimed from rechargeable disposable vapes. However, they only provide 3.7V each, and safe recharging circuits on the market only supported up to 3.7V when we need 5. The new charging circuit consisted of an adafruit 3.7V battery charging circuit, two 3.7V vape batteries, and a 3PDT switch. The switch causes the batteries to alternate between being connected in parallel, where they can charge safely and in series where they can output 7.4V, a power supply within our desired range. The IMU, an Adafruit ICM 20649 6-DOF model, communicates important data with the RF Nano via I2C communication. 

For the front-end, we used Django to help build the website, styling our interface from scratch using CSS. 

## Challenges we ran into
We had some issues with trying to sync up our graph.py file to our actual webapp. The prototype is entirely functional, we just launched it directly by running "python graph.py" in the posturepal directory instead of through a link in the website.

## Accomplishments that we're proud of
Taking on the ambitious nature of doing a hardware based project caused a fair amount of adversity, but we were able to work past these initial struggles. We were especially proud of using collected, lithium-ion vape batteries to power our device, when they otherwise would have ended up in a landfill and harmed the environment. 

## What we learned
We definitely learned a lot about webapp development throughout this entire experience. All four of us are relatively new to hackathons, so this project definitely helped sharpen our skills and teach us plenty about real-world applications. On another note, we definitely learned that our posture is a bit worse than we initially thought. 

## What's next for PosturePal
We are genuinely passionate about this project, and are 100% considering further development. This device is only a prototype as of now, but we would love to explore adding new features such as integrating machine learning to personalize posture recommendations, improving the real-time feedback, and exploring different sensor technologies for further accuracy.

Additionally, we aim to perfect PosturePal's ergonomics for maximum user comfort, ensuring it can seamlessly integrate into users’ daily routines. We were also considering a mobile app for tracking posture trends over time, providing users with personalized improvement plans. Ultimately, our goal is to create an accessible solution that helps people maintain better posture and prevent long-term health issues.



