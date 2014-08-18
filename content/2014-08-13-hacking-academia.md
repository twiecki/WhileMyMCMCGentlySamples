Title: SciFoo 2014: Hacking Academia from Inside and Out
date: 2014-08-13 13:00
comments: true
slug: hacking-academia

<!-- PELICAN_BEGIN_SUMMARY -->
Almost a year ago, I wrote a post I called the [Big Data Brain Drain](http://jakevdp.github.io/blog/2013/10/26/big-data-brain-drain/), lamenting the ways that academia is neglecting the skills of modern data-intensive research, and in doing so is driving away many of the men and women who are perhaps best equipped to enable progress in these fields. This seemed to strike a chord with a wide range of people, and has led me to some incredible opportunities for conversation and collaboration on the subject. One of those conversations took place this past weekend at the annual SciFoo conference, and this article is my way of recording some reflections on that conversation.

[SciFoo](http://www.digital-science.com/sciencefoo/) is an annual gathering of several hundred scientists, writers, and thinkers sponsored by Digital Science, Nature, O'Reilly Media & Google. SciFoo brings together an incredibly eclectic group of people: I met and spoke with philosophers, futurists, alien hunters, quantum physicists, mammoth cloners, journal editors, science funders, astrophysicists, musicians, mycologists, mesmerists, and many many more: the list could go on and on. The conference is about as unstructured as it can be: the organizers simply provide food, drink, and a venue for conversation, and attendees put together breakout discussions on nearly any imaginable topic. If you ever get the chance to go, my advice is to drop everything else and attend. It was one of the most intellectually stimulating weekends I've ever had.

<!-- PELICAN_END_SUMMARY -->

The SciFoo meeting is by invitation only, and given the incredible work other folks I met there I'm still not quite sure how I ended up on the invite list (it was perhaps the worst flare-up of imposter syndrome I've ever had!) I forced myself to get over it, though, and teamed-up with Chris Mentzel, Program director of the [Moore Foundation](http://www.moore.org/), and lead a session: we called it *Hacking Academia from Inside and Out*. The session was in many ways a conversation around the general topic of my *Big Data Brain Drain* post, though it was clear that many of the folks in attendance had been thinking in these terms long before I penned that particular essay.


## The Problem
The problem we discussed is laid out in some detail in my *Brain Drain* post, but a quick summary is this: scientific research in many disciplines is becoming more and more dependent on the careful analysis of large datasets. This analysis requires a skill-set as broad as it is deep: scientists must be experts not only in their own domain knowledge, but in statistics, computing, algorithm building, and software design as well. Many researchers are working hard to attain these skills and do good work; the problem is that academia's reward structure is not well-poised to recognize the value of this type of work. In short, time developing good, reusable software tools translates to less time writing and publishing, which in the current system leads to little hope for career advancement.

In my *Brain Drain* post, I observed the rise of data-intensive researchand lamented that researchers with the requisite interdisciplinary knowledge are largely unrecognized and unrewarded in academia, even as they are highly-sought-after in the tech industry.
I previously labeled this type of person a "new breed of scientist", but since then it's become clear that the working label for this type of person seems to have become (for better or worse) a *data scientist*.


## Defining Data Science
The term "Data Science" generally seems to get a bad rap: it's variously dismissed as [misleading](http://insideanalysis.com/2013/08/a-data-science-rant/), an [empty buzzword](http://www.forbes.com/sites/gilpress/2013/08/19/data-science-whats-the-half-life-of-a-buzzword/), or begrudgingly conceeded to be [flawed, but useful](http://radar.oreilly.com/2011/05/data-science-terminology.html). Perhaps "Data Scientist" can be understood as just a more subdued term for the ["sexy statisticians"](http://www.nytimes.com/2009/08/06/technology/06stats.html) that Hal Varian predicted would emerge this decade. I think the best illustration of data science's definition comes from Drew Conway's (somewhat tongue-in-cheek) [Data Science Venn Diagram](http://drewconway.com/zia/2013/3/26/the-data-science-venn-diagram), which applies the label "Data Science" to the intersection of hacking skills, statistical knowledge, and domain expertise.

{% img /images/Data_Science_VD.png 440 440 %}

The key is that there is both a breadth and a depth to the knowledge and skill-set involved. In the words of Alex Szalay, these sorts of researchers must be "Pi-shaped" as opposed to the more traditional "T-shaped" researcher:

{% img /images/pi_shaped.png 440 440 %}

A classic PhD program generates *T-shaped* researchers: scientists with wide-but-shallow general knowledge, but deep skill and expertise in one particular area.
The new breed of scientific researchers, the data scientists, must be *Pi-shaped*: that is, they maintain the same wide breadth, but push deeper both in their own subject area and in the statistical or computational methods that help drive modern research.

Perhaps neither of these labels or descriptions is quite right. Another school of thought on data science is to follow Jim Gray and label it the ["Fourth Paradigm"](http://research.microsoft.com/en-us/collaboration/fourthparadigm/) of scientific discovery: First came the observational insights of empirical science, then the mathematically-driven insights of theoretical science, then the simulation-driven insights of computational science, and now the data-driven insights of modern scientific research.
Just as the scientific method morphed and grew through each of the previous paradigmatic transitions, so should the scientific method across all disciplines be modified again for this new data-driven realm of knowledge.

Regardless of what metaphor, definition, or label you apply to this class of researcher, it is clear that their skill set is highly valuable in both academia and industry: the Brain Drain comes from the unfortunate fact that academia fails to properly reward the valuable skillset of the data scientist.

## Our Discussion: Academia and Data Science
With this label in mind, our SciFoo discussion focused largely around the following questions:

1. Where does Data Science fit within the current structure of the university?
2. What is it that academic data scientists want from their job? How can academia offer that?
3. What are the drivers that can shift academia to recognizing & rewarding data scientists in domain fields?
4. Recognizing that not all students will end up in academia, how do we best prepare them for life after their degree?

I'll go through some of the thoughts we discussed below:




### 1. Where does Data Science fit within the current structure of the university?

The question of data science's place in academia drew a variety of responses and ideas:

**The Status Quo: data science is simply a label for a skill-set, and shouldn't be separated from the departments in which it's used.** The thinking here is that data science is simply an umbrella term for an essential skill to performing science. For example, laboratory biologists are dependent on pipetting skills: this doesn't mean that the university should create a new "Department of Applied Pipetting". On the contrary, it simply means that pipetting technique should be part of a laboratory biologist's normal training. Similarly, departments across the university should simply incorporate relevant data science techniques into their normal curriculum.

**Data science as a consulting service.** Perhaps data science is more like Information Technologies (IT). All modern science labs depend on some sort of computer infrastructure, and most universities long ago realized that it's counter-productive to expect their specialized researchers to effectively manage that infrastructure. Instead, IT organizations were created which provide services to multiple departments. Perhaps data science should be the same thing: we can't expect every scientist to be fluent in the statistical and computational methods required to work with large datasets, so perhaps we should out-source these tasks to data science experts.

**Data science as an applied computer science department.** There has been a trend in the 20th-century of academic subjects splitting into "pure" and "applied" sub-domains. Many Universities have departments of "applied math" and "applied physics", which distinguish themselves from the non-applied version by applying the techniques of the field to practical rather than theoretical problems. Perhaps data science is best viewed as an applied branch of computer science or of statistics which should become its own academic department.

**Data science as an interdisciplinary institute.** A middle ground might be to give data science a home as an interdisciplinary institute; this is a common approach for topics that are inherently multi-disciplinary. Multi-disciplinary institutes are already common in academia: for example, the University of Washington is home to the [Joint Institute for the Study of Atmosphere and Ocean](http://jisao.washington.edu/), which brings together dozens of [department, schools, and labs](http://jisao.washington.edu/about/collaborators) to collaborate on topics related to the climate and the environment.



### 2. What is it that academic data scientists want from their job? How can academia offer that?

We brainstormed a list of goals that drive data scientists within academia and industry. While it is certainly not a homogeneous group, most folks are driven by some combination of the following concerns:

- Money, Salary, stock options, etc.
- Stability: the desire to live in one place rather than move every few years
- Opportunity for Advancement
- Respect of Peers
- Opportunity to work on open source software projects
- Opportunity to travel & attend conferences
- Flexibility to work on interesting projects
- Opportunity to publish / freedom from the burden of publishing
- Opportunity to teach / freedom from the burden of teaching
- Opportunity to mentor students / freedom from the burden of mentoring students

I've tried to generally order these from perks of industry to perks of academia from the perspective of a recently-minted PhD, but this rough one-dimensional categorization misses the variety of opportunities in both worlds. For example, some academic research scientists do not spend time teaching or mentoring students, and some tech industry jobs contain the type of flexibility usually associated with academic research.

The younger participants who have most recently been "in the game", so to speak, especially noted problems in academia with the first three. Compared to an industry data scientist position, an academic post-doc has some distinct disadvantages:

- Money: the NIH postdoc salary hovers somewhere between $\$$40,000 - $\$$50,000 per year. Industry can offer a qualified graduate several times that to start.
- Stability: it is common now for young scientists to do 2-3 postdocs, each perhaps in a different part of the country. This means many are unable to settle-down and build a community until their mid-30s. For an industry data scientist, many cities offer dozens of employment options near home.
- Advancement: those who focus on software and data in academia, rather than a breakneck pace of publication, have little hope for a tenure-track position under the current system. A researcher who spends their time building software tools can expect little reward within academia, no matter how influential those tools might be.

Anecdotally, these seem to be the top three issues for talented data scientists in academia. With the tech-industry market for data scientists as hot as it is, the most skilled PhD candidates have the most to gain by leaving their field of research.



### 3. What are the drivers that can shift academia to recognizing & rewarding data scientists in domain fields?

We discussed several drivers that might make academia a more friendly place for data scientists. Generally, these centered around notions of changing the current broken reward structure to recognize success metrics other than publication or citation. These could be broken-up into two different categories: those outside academia who might push for change (e.g. funding agencies, publishers, employers, etc.) and those inside academia who might implement the change themselves (e.g. university leadership and department leadership). We discussed the following ideas:

#### From the outside:
- Publishers might provide a means of publishing code as a primary research project.
- Funding agencies might provide funding specifically for data scientists within domain fields.
- Funding agencies might encourage interdisciplinary collaboration through specific grant requirements.

#### From the inside:
- University leadership might set aside funding for new data science departments or for interdisciplinary institutes.
- University leadership might create joint positions: paying half of a professor or researcher's salary so that they can focus time on tasks such as creating software tools.
- Department leadership might take the lead to adapt their curriculum to include data science topics, and specifically hire one or two tenure-track positions with data science emphasis.
- Department leadership might adjust their hiring practice to recognize alternative metrics that go beyond the H-index: for example, recognizing the importance of an open source software tool that is well-used, but may not generate a classic citation record.



### 4. Recognizing that not all students will end up in academia, how do we best prepare them for life after their degree?

This question is the flip-side of the "Brain Drain" theme: the number of PhDs granted far exceeds the number of academic positions available, so it is mathematically impossible for every graduate to remain in academia.
This is, for some reason, a somewhat taboo subject in academia: I've talked to many who were leaning toward an industry job, and dreaded having "the talk" with their thesis advisor.
But it's time that academic departments get serious about job prospects for their graduates, and that involves making sure they have marketable skills upon graduation.
Fortunately, these marketable skills are the same skills that can lead to success in science: the ability to design and write good software, to write tools that others can reuse, to effectively work with large datasets, etc.
Unfortunately, development of this skillset takes time and energy both at the level of graduate course requirements, and at the level of research time.
Departments should push to make sure that their students are learning these skills, and are rewarded for exercising them.


## Hacking Academia: How is this problem being addressed?
At the beginning of the SciFoo conference, each of the ~250 people present were invited to introduce themselves with a one line description of who they are.
The title of this article, "Hacking Academia", is a phrase that I borrowed from Chris Mentzel's one-line description of his focus.
This is hacking not in the sense of Matthew Broderick in [War Games](http://www.imdb.com/title/tt0086567/), but in the sense of working within a rigid system to accomplish something it's not necessarily designed to do.
In a sense, this is the best description of what we're after: to find shortcuts that will mold academic research into a more effective version of itself.

One of the favorite academic past-times is complaining together about the state of the academy, but rarely do you get to see actual solutions to the problems.
One of the best pieces of the SciFoo discussion was just this: hearing the steps that various individuals, foundations, and institutions are taking to address the concerns outlined above.

### UW, Berkeley, NYU: The Moore-Sloan Initiative
Chris Mentzel, who co-led this discussion, is a program director for the Moore Foundation, and I know him through his involvement with the recent [Moore-Sloan Data Science Initiative](http://www.moore.org/programs/science/data-driven-discovery/data-science-environments).
For years, he has been thinking about these issues from the perspective of a funder of scientific research, and this effort has recently culminated in this $\$$38 million initiative.
This multi-institution award is providing a joint five-year grant to three institutions: University of Washington, University of California Berkeley, and New York University.
An overarching goal of the grant is to jump-start new career paths for data scientists in domain fields, and each of the three universities has a team who is approaching the work in their own way.

In January, I was hired by UW's [eScience Institute](http://escience.washington.edu/) to help lead the UW portion of this effort. We're in the middle of building a data science studio that will be a central hub for data-intensive research on campus, and are currently in the process of hiring our first round of interdisciplinary postdocs, data scientists and research scientists. These positions are designed especially to attract those skilled "Pi-shaped" researchers who may fall through the cracks in classic academic tracks, and we place particular value on alternative metrics such as open source contributions. Berkeley and NYU are undertaking similar efforts on their own campuses.

### NSF: the IGERT program
The NSF has recently announced its Interactive Graduate Education and Research Traineeship (IGERT) program, which provides funding for interdisciplinary training for PhDs. UW was recently awarded an IGERT grant, and the first group of interdisciplinary Big Data PhDs will be starting this fall. An important piece of this was that home departments agreed to allow these students to forego some of their normal degree requirements to make room for courses on data science skills and techniques.

### UW: Provost's Data Science Initiative
The university-wide leadership is also taking some concrete actions along these lines: the provost has set aside funding for half-positions to encourage hiring of interdisciplinary researchers. The next Astronomy professor hired by UW, for example, might spend half of his or her time working and teaching through the eScience institute on general computational and data science methods.

### Harvard: (ex) Initiative for Advanced Computing
Alyssa Goodman of Harvard was part of our discussion, and mentioned that nearly a decade ago Harvard foresaw this problem and began addressing it. They created a short-lived Initiative for Advanced Computing, which was truncated by the global financial crisis before it could get off the ground.
After that false start, Alyssa and others at Harvard are seeking ways to re-build the momentum they had and address the problems we discussed.

### Michigan State: Applied Computational Systems
Another person at the discussion was Steve Hsu, Vice President for Research at Michigan State University. He shared some exciting news about a new initiative at Michigan State: the creation of a new *Applied Computational Systems* department. According to Dr. Hsu, they will be hiring around 20 interdisciplinary tenure-track faculty, who will have one foot in their home department and one foot in the new ACS department. MSU already has many impressive researchers: with this effort I'm excited to see the dynamic community they will build.


## Conclusion
The SciFoo discussion was excellent, and I'd like to thank O'Reilly Media, Digital Science, Nature Publishing Group, and Google for making it possible.
Nearly a year after my *Brain Drain* post, I'm excited to see that there are so many good people thinking about these problems, and so many real solutions on the horizon.
While the lure of a well-funded tech industry will still cause a steady stream of researchers to move away from their academic research, I'm heartened to see so much specific effort to carve-out good niches for the type of researchers equipped to be successful in a world of ever-growing datasets.