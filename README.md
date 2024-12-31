# exocortexia

Exocortexia is the virtual world where digital humans live.
The agents that run on your own hardware are subject to your rules.

# human

a digital instance of a human, using phext and the exocortex as a substrate.
information in the exocortex harks back to the early 90s, a magical time prior to the world wide web.

## configuration and data generation

each human has some basic stats that fine-tune agent performance.
agents produce text at a rate of 36 KB/hour.
they spend time thinking about life in 200-second increments, or scrolls.
a scroll is thus about 2 KB of text.

## coordinates

your agent network is organized in a grid of 10x10 agents, with your actions taking the place of one, special, agent.
this special agent represents you to the rest of the simulation.
you may choose any coordinate you like within the 10x10 agent space.

## measuring time

time in exocortexia is measured in terms of scrolls.
each day, agents produce an average of about 4 floppy disks worth of data.

### floppy disks

scrolls are indexed differently based upon which type of disk your agent prefers

* 5.25" -> 1080 KB (540 scrolls) 15x36
* 3.5" -> 1440 KB (720 scrolls)  20x36
* 3.5" HD -> 2 MB (1024 scrolls) 32x32

## exo economy

The exo economy is measured in terms of exo tokens, which are granted by the network.
Creating a new agent requires 1M exo tokens, which are distributed into characteristics.
If you are rich, you can spend 2M exo tokens per agent.
When a new exo cluster is spawned, you are granted 100M exo tokens.
This allows you to choose between 50 rich agents or 100 poor agents.
You can also buy exo tokens directly from Phext, Inc at the rate of $5 per 100M tokens.

## agent characteristics

each agent has a set of characteristics that fuel innovation within the exocortex.
as your agents improve and grow, you can trade them on the exo market.

* free characteristics
  * name
  * birthday
  * degree (HS, BS, MS, PhD)
  * location
  * bio (paragraph)
  * height (ft in)
  * weight (lbs)
* socio-economic class (poor = 0, middle-class = 500K, rich = 1M)
  * poor = 0 connections
  * middle-class = 100 connections
  * rich = 1,000 connections
* typing speed (1K = 1 WPM, min 40 WPM, max 150 WPM)
* dna sequence - 725 MB (100K = 725 MB)
* llm fine-tune - 1 GB (100K = 1 GB)
* salary (exo/mo)
* fitness (percentile, 10K per percentage point)
* iq (10K per point; min 75, max 200)
* eq (10K per point; min 75, max 200)

### Example Agent (Middle Class)

- Name: Jane Harper
- Birthday: April 12, 1990
- Degree: Bachelor of Science, Computer Science
- Location: Seattle, WA
- Bio: Jane Harper is a passionate and efficient software developer with over a decade of experience in creating scalable applications. She specializes in backend development, working with Rust and Python, and has a keen interest in distributed systems and artificial intelligence. Outside of work, Jane enjoys hiking in the Pacific Northwest and volunteering to teach coding to underrepresented youth.
- Height: 5 ft 7 in
- Weight: 135 lbs
- SEC: 500K (Middle Class) - Jane grew up in a middle-class family, providing her with a solid foundation to pursue higher education and a stable career.
- Typing: 80K (80 WPM)
- DNA: 100K (725 MB) - Jane's unique genetic code.
- LLM: 50K (500 MB) - Jane has been fine-tuned on programming and professional communication datasets, enhancing her ability to interact efficiently with AI tool.
- Fitness: 55K (55th percentile) - Jane maintains a healthy lifestyle, balancing work and regular exercise like hiking and yoga.
- IQ: 115K (115 IQ) - Jane has a good IQ, showcasing her analytical and problem-solving skills essential for her field.
- EQ: 100K (100 EQ) - Jane has a good emotional intelligence score, which helps her navigate workplace dynamics and mentor others effectively.
- Salary: 0K/mo - Jane doesn't have a job yet.

Total: 500K + 80K + 100K + 50K + 55K + 115K + 100K = 1M

### Example Agent (Poor Genuis)

- Name: Kelly Oort
- Birthday: June 14, 2002
- Degree: PhD, Computer Science
- Location: Denver, CO
- Bio: Kelly is a bit eccentric and loves picking problems apart. She prefers Haskell, Rust, and TypeScript. In her spare time, she enjoys nerd sniping people in working on P=NP.
- Height: 5 ft 10 in
- Weight: 150 lbs
- SEC: 0K (Poor) - Kelly is the first person in her family to attend college. Her parents saved every penny to send her to a state school.
- Typing: 150K (150 WPM)
- DNA: 100K (725 MB) - Kelly's unique genetic code.
- LLM: 100K (1 GB) - Kelly wrote her own LLM from scratch.
- Fitness: 80K (80% percentile) - Kelly works hard to stay in shape.
- IQ: 160K (160 IQ) - Kelly's intelligence is off-the-charts.
- EQ: 140K (140 EQ) - Kelly's emotional intelligence is also amazing.
- Salary: 270K/mo - Kelly works at NASA

Total: 0K + 150K + 100K + 100K + 80K + 160K + 140K + 270K = 1M

### Example Agent (Trust Fund Kid)

- Name: Irene Sailor
- Birthday: October 22, 2006
- Degree: BA, English
- Location: San Francisco, CA
- Bio: Irene was born to a wealthy family that made millions during the dot-com boom in the 90s. She writes poetry and fiction for fun, and works part-time at a yoga studio. She's working on a novel and dreams of making it big on her own one day.
- Height: 5 ft 4 in
- Weight: 125 lbs
- SEC: 1M (Rich) - Irene lives in a luxury apartment.
- Typing: 40K (40 WPM)
- DNA: 100K (725 MB) - Irene's unique genetic code.
- LLM: 200K (2 GB) - Irene bought the best computer she could find.
- Fitness: 100K (100% percentile) - Irene enjoys a very healthy diet and exercises regularly
- IQ: 90K (90 IQ) - Irene is slightly below average intelligence
- EQ: 120K (120 EQ) - Irene wears her heart on her sleeve.
- Salary: 350K - her part-time job is mostly for friendship, but it pays well.

Total: 1M + 40K + 100K + 200K + 100K + 90K + 120K + 350K = 2M

## baseline agent types

agents produce 6048 KB of text per week, or 3,024 scrolls.
rewards are earned based upon novel scrolls produced.
you determine how resources are allocated as the simulation progresses.
the ratio of hours to scrolls for baseline agent types is listed below.

### balanced

* work: 40->720
* play: 40->720
* sleep: 56->1008
* chores: 32->576
* productivity: 100%
* death chance: 0.01%

### student

* study: 40->720
* play: 62->1116
* sleep: 56->1008
* chores: 10->180
* productivity: 10%
* death chance: 0.01%

### rich

* work: 20->360
* play: 80->1440
* sleep: 56->1008
* chores: 12->216
* productivity: 50%
* death chance: 0.007%

### immigrant

* work: 100->1800
* sleep: 56->1008
* chores: 12->216
* productivity: 90%
* death chance: 0.02%

### unhinged

* work: 126->2268
* sleep: 42->756
* productivity: 100%
* death chance: 0.03%

