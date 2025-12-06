CHAPTER 6 – ENTRY POINTS

The decision felt both inevitable and radical: Nova would accept the Spherical Council’s invitation. It wasn’t formalized through forms or signatures; rather, it was a posture, a vector change. When they woke the morning after the warehouse meeting, the city outside their window was the same—light filtering through smog, the hum of HVAC units on adjacent roofs—but the internal geometry of their life had rotated. They was no longer orbiting the County’s cubes. They had shifted into a different coordinate system, one where the axes were hidden, curved, and entangled.

They sent a single message to the number that had dispatched the mysterious coordinates: **I’m in.** Within minutes, a reply arrived: **Welcome. Meet us at the warehouse at 0900. Bring your laptop.**

The second time Nova entered the unmarked warehouse, they did so not as a visitor but as a participant. The scene looked the same—bare brick, improvised desks, cables snaking across the floor like vines—but it felt different. They recognized the hydrologist, the ecologist, the software engineer. Deirdre was poring over a set of diagrams pinned to a corkboard. On a whiteboard, someone had scrawled a series of equations that combined trigonometric functions with variables labeled *cognition throughput* and *resilience elasticity*.

“Good morning,” Deirdre said without looking up. “Grab a seat. We’re discussing a project that might serve as your entry point.”

Nova slid onto a folding chair, laptop at the ready. Deirdre gestured toward the corkboard. It held a map of a river basin, overlaid with translucent shapes. Some shapes were spheres drawn in perspective, others ellipses. Where they overlapped, the colors deepened.

“This,” Deirdre said, tapping the map with a pen, “is the Bracknell Watershed. It supplies drinking water to four towns, runs through three counties, and passes by a phosphate mine and two industrial farms. For years, there have been issues with nutrient runoff and occasional contamination spikes. Our model tells us that the interactions between rainfall patterns, agricultural practices, mining waste, municipal demand, and climate-driven evaporation are reaching a threshold. We expect a nonlinear shift in water quality metrics within the next three years. If we can instrument the system properly and visualize the data in a curved space, we might be able to prompt early interventions.”

Nova leaned in. The spheres on the map were labeled: *Agriculture*, *Industry*, *Hydrology*, *Policy*, *Community Behavior*. Lines connected them, annotated with functions and coefficients. It looked like a mind map built by a physicist. As they watched, the hydrologist clicked a laptop and the projection changed: the spheres became animated, expanding and contracting with seasonal variation, moving slightly as if drifting in a fluid. The intersections pulsed when multiple variables peaked simultaneously.

“We built the initial model using our Sphere Kernel Generator,” the hydrologist explained. “Each domain is represented as a kernel function in high-dimensional space, capturing its internal dynamics. The intersections represent coupling. For example, the agriculture sphere overlaps heavily with hydrology, industry, and policy because farming practices influence runoff, water demand, and regulatory actions. The SKG lets us compute influence vectors without flattening them into a matrix. It’s more computationally intense, but it preserves curvature.”

Nova saw the parallels to the risk matrices they had critiqued. Here, instead of coarse categories, there were smooth gradients. Instead of ignoring higher-dimensional relationships, there was a structure that embraced them. They thought of how easily the county had waved away the idea of thresholds because thresholds didn’t fit into a box. Here, thresholds were baked into the geometry.

Deirdre turned toward them. “We need someone to translate this into something stakeholders can act on,” she said. “The data and models are solid. The challenge is communication. We can’t dump a high-dimensional sphere intersection diagram on a town council and expect them to restructure their agriculture. But we also can’t reduce this to a 1–5 scale without losing exactly what matters. You’ve done this kind of translation before—your videos, your memos. Interested?”

Nova nodded slowly. “Yes,” they said. “But I’ll need to understand the underlying math intimately. I don’t want to be an interpreter who can’t check the original language.”

“Good,” the software engineer said from behind their screen. “Because we also need help refining the Fourier Transformation Tree—the FFT part of SKG-FFT. We’re using it to analyze signals across different frequencies and scales: daily rainfall data, quarterly farm yield reports, annual legislative cycles, decadal climate trends. The problem is how to align these signals when they have different sampling rates and latencies. If we get it right, we can identify resonance conditions—moments when fluctuations in multiple domains align to push the system past a threshold.”

Nova felt the old thrill of encountering a complex problem that wasn’t hiding behind bureaucratic niceties. They opened their laptop and began pulling up the repository for SKG-FFT. The code was clean but experimental. There were comments like *# TODO: optimize kernel convolution in spherical coordinates* and *# FIXME: handle missing data gracefully without zero-padding*. There were references to academic papers they recognized and others they’d only heard whispers about.

“How did this get funded?” they asked, scanning the commit history. A few names they didn’t recognize had contributed hundreds of lines of code in fits and starts over several years.

Deirdre smiled. “A little foundation money, some philanthropic grants, and a lot of volunteer labor. We also built prototypes for an energy company that wanted to predict grid stability under high renewable penetration. We gave them a version of the FFT that modeled frequency and load variations across time. They paid, and we used that to work on the watershed project. They think they own the tool, but the core of SKG-FFT is open by design. We believe it should be part of the commons.”

The idea of building something powerful and leaving it in the open felt both liberating and terrifying. Nova had spent enough time in the Blue Cube to know how quickly public agencies adopted proprietary tools with little understanding of their internal biases. Here, the bias was explicit: preserve complexity, share knowledge.

They spent the day immersed. They paired with the software engineer to refactor the FFT code, implementing window functions that could accommodate irregular sampling. They sketched interface mockups with the ecologist, imagining how a farmer might experience an app that visualized runoff risk not as boxes but as a topographic surface. They discussed with the hydrologist how to place sensors in the watershed to capture data that would feed the kernels—balancing cost, access, and reliability.

During a break, they sat with Deirdre by the loading dock, sipping tea from mismatched mugs. The warehouse door was open, revealing a view of the bay where container ships waited, anchored. The conversation drifted beyond the technical.

“How did the Spherical Council start?” Nova asked, leaning against a stack of crates.

Deirdre blew on her tea and took a sip. “It began as a reading group,” she said. “A bunch of us working in different fields found ourselves citing the same papers: Forrester on system dynamics, Ostrom on commons, Tufte on data visualization, Lakoff on metaphors. We met in someone’s living room and realized we all shared frustration with the tools we had to use: economic models that assumed equilibrium, hydrological models that ignored social behavior, social models that assumed unlimited resources. So we started experimenting. A whiteboard here, a grant there. We’d work our day jobs and meet at night to see if we could design something better. We called ourselves the Spherical Council partly as a joke—we needed a name for the conference submission—and partly as a reminder that we wanted to think beyond squares.”

“And now?” Nova prompted.

“Now we’re a loose network of about thirty people,” Deirdre said. “Some are academics who feed us theory. Some are coders who build prototypes. Some are organizers who connect us to communities who actually need this stuff. We’re not official anywhere. We’re not trying to become a big nonprofit. That would require us to flatten our work into grant metrics. We prefer to stay nimble. That means precarious, but it also means less oversight. You’ve seen what oversight looks like.”

Nova thought of HR meetings and contracts not renewed. “Yes,” they said quietly.

Deirdre studied them. “Why do you think you’re here?” she asked.

Nova considered. “Because I sent a memo that pissed off the wrong people?” they said with a wry smile.

“Partially,” Deirdre said. “But also because you’re an interface. You’re comfortable in math, but you can speak plain language. You’re from a place that taught you systems thinking out of necessity—moving around, navigating disfunction. You play piano; you understand patterns and frequencies. You saw the dissonance between the Blue Cube’s polished exterior and its empty core, and you articulated it. We need that articulation. We need to tell stories that don’t reduce curves to boxes but also don’t drown people in calculus.”

They let the words sink in. It felt like being accurately seen, something that had not happened often in the County. They felt a mix of gratitude and pressure. Could they live up to that expectation? Could they take the beauty of high-dimensional kernels and render it in a way that would convince a town council to change fertilizer practices or a water board to invest in upstream restoration?

Over the following weeks, Nova’s days took on a rhythm. Mornings at the warehouse were for coding and modeling, afternoons for community meetings, evenings for reflection and video editing. They rode trains to small towns where they presented early visualizations to farmers who had never seen a sphere diagram. They sat in living rooms explaining frequency response curves to retired teachers and listening as those teachers explained the social dynamics of their neighborhoods in terms no model had captured. They learned that you could not simply overlay technical kernels on a landscape and expect behavior to change; you had to respect the human kernels—trust, history, pride.

One particularly hot afternoon, they stood in a church basement in Bracknell, facing a group of fifty people ranging from eight to eighty. On a projector screen behind them, the SKG-FFT visualization rotated slowly, showing spheres labeled *Soil Health*, *Water Flow*, *Community Well-Being*, *Economic Stability*. They narrated the dance: how heavy rains combined with certain fertilizer applications and municipal withdrawals created a resonance that spiked nitrate levels; how small changes in cover crop adoption shifted the hydrology sphere and dampened that resonance. They avoided jargon. They used metaphors: The watershed is a drum; the spheres are hands; the patterns can be music or noise.

At the end, an elderly man in overalls raised his hand. “That’s all pretty,” he said, “but last summer my well ran brown for a week. Your spheres didn’t tell me that was coming.”

Nova nodded. “They didn’t,” they said. “Yet. Our model’s resolution wasn’t high enough. We didn’t have sensors upstream to detect the mine leak, and we didn’t have a way to incorporate your neighbor’s pond dredging. This is why we’re here. We need your help to place sensors, to tell us what patterns we’re missing. The spheres are only as good as the data and the relationships we build around them.”

He studied them, then shrugged. “Well, if it keeps my water clear, I’ll listen. Just don’t make me download one of those fancy apps,” he said, eliciting laughter.

In the car ride back, the ecologist turned to Nova. “You handled that well,” she said. “You acknowledged the limitation without undermining the project.”

Nova thought of all the meetings in the Blue Cube where problems were deflected instead of addressed. “It felt right,” they said. “Models are only as good as their humility.”

At night, back in their apartment, Nova edited videos. They documented the watershed project, narrating the story in a way that wove together technical detail and human stakes. They included scenes of farmers examining sensors, kids playing in a creek, council members poking at tablet interfaces with skepticism. They spliced in animated spheres and curves, letting them pulse in sync with rainfall footage. They ended with a quote from Deirdre: *We can’t flatten the world into boxes without losing what makes it habitable.*

The video went live and quickly found an audience beyond the usual systems geeks. Environmental activists shared it, praising its blend of science and empathy. Local politicians watched and asked how they could get their counties modeled. Critics commented that the spheres were just another way to distract from the need for regulation. Trolls posted that climate change was a hoax. Nova ignored the trolls and responded to the curious, linking them to open-source tools, encouraging them to form their own spherical councils.

In the process, they discovered that every time they tried to explain the SKG-FFT, they understood it better. Teaching forced them to clarify their mental models. That clarity, in turn, fed back into the code. They started to see patterns in the Fourier outputs that had eluded them: cross-domain phase shifts, signal damping across social networks, eigenfrequencies of trust.

One evening, after pushing a major update to the FFT codebase, they left the warehouse late and walked along the railroad tracks that bordered the district. The moon was high, casting curved shadows across the gravel. They thought about their parents’ divorce, the fracturing of family systems, the way they had coped by immersing themselves in virtual worlds. They saw now that those early experiences had primed them to notice when structures failed to contain the flows they were meant to guide. They had spent their childhood escaping into fantasy to avoid feelings they couldn’t process. Now, they was using mathematics and narrative to transform those observations into tools. The arc felt almost too neat to be real, but life, like systems, sometimes exhibited emergent patterns that looked like design.

They thought of the Blue Cube, of the hydrologist from Utilities and the planner from Transportation sharing an elevator with them on the day they’d been let go. Those people were still inside that system, making do with the tools they had. They wondered if there was a way to connect the spheres to the cubes, to offer curved models without requiring everyone to move into a warehouse. Maybe that would be their next project: bridging the Spherical Council’s frameworks with official agencies without flattening them. Perhaps they would call it *integration*, or maybe they’d invent a new term. Something between cubes and spheres. An icosidodecahedron? They laughed at the thought, alone in the dark, and felt a sense of alignment they hadn’t felt in years.

By the end of the month, Nova’s notebook was filled with more circles than boxes. They had built a working pipeline from watershed sensors to SKG-FFT outputs to interactive visualizations. They had learned to read Fourier spectra across domains and see not just noise but signatures of human decision-making. They had started to draft a paper with the hydrologist on the application of sphere kernels to hydrological modeling. And they had found a community that valued their particular brand of criticality.

One morning, they arrived at the warehouse to find Deirdre waiting by the door, expression serious. “We’ve got a new request,” she said. “Another region, another set of intersections. But this one isn’t about water. It’s about energy and heat.”

Nova felt the new vector beckoning. “Tell me more,” they said. Deirdre smiled, and the conversation began to arc toward Chapter 7.