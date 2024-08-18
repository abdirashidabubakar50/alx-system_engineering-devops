🚨 Issue Summary: When the Code Goes Rogue 🚨
Duration of the Outage:
The chaos reigned for 2 hours and 15 minutes, from 06:15 EAT to 08:30 EAT. (Enough time to finish your morning coffee or realize the system's down—whichever came first.)
Impact:
During this caffeine-fueled time, 35% of our users faced the horror of failed logins and API slowness. Some users probably thought their internet connection had given up on them—false alarm! It was us. Apologies for the unexpected "log-out party."
Root Cause:
Well, it wasn't gremlins. A sneaky memory leak in the authentication service code quietly filled up server memory until it finally waved the white flag and crashed. Lesson learned: sometimes, your code needs to go on a diet. 🍩❌

🕒 Timeline: A Series of Unfortunate Events 🕒
06:15 EAT - Our Datadog alert woke up the team, screaming, "HIGH MEMORY USAGE!"
06:20 EAT - An engineer, likely half-asleep, dives in to check CPU usage.
06:30 EAT - The engineer suspects a DDoS attack, scans firewall logs, and secretly hopes it's just a bad dream.
06:50 EAT - After confirming we weren’t being attacked by an army of bots, the focus shifts to the authentication service logs.
07:15 EAT - The engineer gives the server a good old restart—works for your computer, right? Not for long…
07:30 EAT - Backend team enters the scene, like detectives hunting down a bug. After deep diving into the code, the culprit is found: a memory leak from last night's deployment.
08:00 EAT - Hotfix applied, fingers crossed 🤞, and a full restart of the service happens.
08:30 EAT - Boom! Services are back, users can log in, and peace is restored. 🎉

🔍 Root Cause and Resolution: CSI - Code Scene Investigation 🔍
Root Cause:
The authentication service had been quietly hoarding memory due to a flaw in the session cleanup code. This memory leak kept stacking up until the server reached critical mass, threw in the towel, and collapsed. Not cool.
Resolution:
Our heroes (the backend team) swooped in, patched up the rogue code, and implemented a hotfix to ensure sessions were cleaned up properly. The server was given a clean restart, and memory usage returned to a manageable state. Crisis averted!

🛠️ Corrective and Preventative Measures: How We Plan to Stop Future Shenanigans 🛠️
Improvements:
Code Review Bootcamp: From now on, our code will undergo stricter reviews to avoid any sneaky leaks. No code sneaks by us again!
Memory Police: We’re stepping up our load testing game to catch these memory hogs before they wreak havoc in production.
Alert Overhaul: We're fine-tuning our alerts so the next time, we catch the problem before the servers beg for mercy.
Action Items:
Patch authentication service with the hotfix in all environments (no exceptions).
Set up memory leak detection tools in the CI/CD pipeline because prevention > cure.
Revise alert thresholds in Datadog—let's catch the fire before it starts.
Post-mortem code review to find hidden gremlins that might still lurking in the codebase.
Team training on memory management—so everyone knows how to keep the code in shape. 🏋️‍♂️

