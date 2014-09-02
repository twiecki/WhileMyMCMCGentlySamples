Title: On Frequentism and Fried Chicken
date: 2014-09-02 16:00
comments: true
slug: on-frequentism-and-fried-chicken

<!-- PELICAN_BEGIN_SUMMARY -->
My recent series of posts on [Frequentism and Bayesianism](http://jakevdp.github.io/blog/2014/03/11/frequentism-and-bayesianism-a-practical-intro/) have drawn a lot of comments, but recently Frederick J. Ross, a UW colleague whom I have not yet had the pleasure of meeting, penned a particularly strong-worded critique: [Bayesian vs frequentist: squabbling among the ignorant](http://madhadron.com/posts/2014-08-30-frequentist_and_bayesian_statistics.html). Here I want to briefly explore and respond to the points he makes in the post.
<!-- PELICAN_END_SUMMARY -->

Mr. Ross doesn't mince words. He starts as follows:

> Every so often some comparison of Bayesian and frequentist statistics comes to my attention. Today it was on a blog called [Pythonic Perambulations](http://jakevdp.github.io/blog/2014/03/11/frequentism-and-bayesianism-a-practical-intro/). It's the work of amateurs.

He goes on to lodge specific complaints about subtleties I glossed-over in the four posts, all of which seem to miss one salient detail: the posts were an explicit response to my observation that "many scientific researchers never have opportunity to learn the distinctions between Frequentist and Bayesian methods and the different practical approaches that result..." That is, I aimed the discussion not toward someone with a deep background in statistics, but at someone who *can't even name the fundamental differences between frequentism and Bayesianism.*

Did I gloss over advanced subtleties in this introductory primer? Certainly. As interesting as it may have been for Mr. Ross and other well-read folks had I delved into, say, the deeper questions of assumptions implicit in [frequentist constraints vs. Bayesian priors](http://www.stat.berkeley.edu/~stark/Preprints/constraintsPriors12.pdf), it would have distracted from the purpose of the posts, and would have lost the very readers for whom the posts were written.

Rethinking the Debate
---------------------
Thus, we see that his first set of complaints can be chalked-up to a simple misunderstanding of the intended audience: that's an honest mistake, and I won't make more of it. But he goes beyond this, and proposes his own final answer to the centuries-old debate between frequentists and Bayesians. As he writes: "Which one is right? The answer, as usual when faced with a dichotomy, is neither."

This should pique your interest: he's claiming that not only am I, a humble blogger, an ignorant amateur (which may be true), but that luminaries of the science and statistics world &mdash; people like Neyman, Pearson, Fisher, Jaynes, Jeffries, Savage, and many others who sometimes ardently addressed this question &mdash; are simply ignorant squabblers within the field which they all but created. I doubt I'm alone in finding this sweeping indictment a bit suspect.

But let's skip these charges and dig further: what third route does Mr. Ross propose to trample all this precedent?  The answer is decision theory:

> Probability, as a mathematical theory, has no need of an interpretation... the real battleground is statistics, and the real purpose is to choose an action based on data. The formulation that everyone uses for this, from machine learning to the foundations of Bayesian statistics, is decision theory.

His argument is that frequentist and Bayesian methods, in a reductionist sense, are both simply means of reaching a decision based on data, and can therefore be viewed as related branches of decision theory. He goes on to define some notation which explains how any statistical procedure can be formulated as a question of progressing from data, via some loss function, to a particular decision. Frequentist and Bayesian approaches are simply manifestations of this unified theory which use particular loss functions, and thus squabbling about them is the pastime of the ignorant.

I'd like to offer an analogy in response to this idea.

Baked or Fried?
---------------
One day in the kitchen, two chefs begin arguing about who makes the best chicken. Chef Hugh prefers his chicken fried: the quick action of the hot oil results light, crispy spiced outer breading complementing the tender meat it encloses. Chef Wolfgang, on the other hand, swears by baked chicken, asserting that its gentler process leaves more moisture, and allows more time for complex flavors to seep into the meat. They decide to have a cook-off: Fried vs. Baked, to decide once and for all which method is the best.

They're just beginning their preparations in the test kitchen when Rick, the local Food Theorist, storms through the door. He follows these chefs on Twitter, and has heard about this great Fried vs. Baked debate. Given his clear expertise on the matter, he wants to offer his final say on the question. As Food Theorists are wont to do, he starts lecturing them:

"Truly, I'm not really sure what this whole contest is about. Don't you know that baking and frying are both doing essentially the same thing? Proteins denature as they heat. Water evaporates, sugar caramelizes, and the Maillard Reaction turns carbohydrates and amino acids into a crispy crust. If you could just get into your ignorant heads that any cooking method is simply a manifestation of these simple principles, you'd realize that neither method is better, and we wouldn't need to waste our time on this silly competition."

At this point, Chef Hugh and Chef Wolfgang pause, catch each other's gaze for a moment, and burst into a hearty laughter. They turn around continue the task of actually turning the raw chicken meat into an edible meal, enjoying the craft and camaraderie of cooking even in the midst of their friendly disagreement. Rick slips out the door and heads home to gaze at his navel while eating a dinner of microwaved pizza bagels.


Baked or Fried? Bayesian or Frequentist?
----------------------------------------
So what's my point here? The fact is that everything our Food Theorist has said is technically correct: from a completely reductionist perspective, cooking meat is nothing more than controlled denaturing of proteins, evaporation of water, and other well-understood chemical processes. But to *actually prepare a meal*, you can't stop with the theory. You have to figure out how to apply that knowledge in practice, and that requires decisions about whether to use an oven, a deep fryer, or a charcoal grill.

Similarly, everything Mr. Ross said in his blog post is more or less true, but you can't stop there. Applying his decision theory in practice requires making some choices: despite his protests, you actually *do* have to decide how to map your theory of probability onto reality reflected in data, and that requires some actual philosophical choices about how you treat probability.


Frequentism vs. Bayesianism, Again
----------------------------------
This brings us back to the original question Mr. Ross (not I) posed: Frequentism vs. Bayesianism: which is correct? As I've maintained throughout my posts (and as Mr. Ross seems to have overlooked when reading them): neither is correct. Or both. It really depends on the situation. As I have attempted to make clear, if you're asking questions about long-term limiting frequencies of repeated processes, classical frequentist approaches are probably your best bet. If you're hoping to update your knowledge about the world based on a finite set of data, Bayesian approaches are more appropriate.

While I have argued that Frequentist approaches [answer the wrong question](https://jakevdp.github.io/blog/2014/06/12/frequentism-and-bayesianism-3-confidence-credibility/) in most scientific settings, I have never claimed that frequentism is fundamentally flawed, or that it is "wrong": on the contrary, in that particular post I went to great length to use Monte Carlo simulations to show that the frequentist approach *does* in fact give the correct answer to the question it asks. Frequentist and Bayesian approaches answer different statistical questions, and that is a fact you must realize in order to use them.

So where does this leave us? Well, Mr. Ross seems to have based his critique largely on misunderstandings: my intended audience was novices rather than experts, and despite his claims otherwise I never attempted to promote frequentism over Bayesianism or vice versa. His protests notwithstanding, I maintain that in practice, frequentism and Bayesianism remain as different as fried and baked chicken: you can huff and puff about unified theoretical frameworks until your face is blue, but at the end of the day you need to choose between the oven and the fryer.