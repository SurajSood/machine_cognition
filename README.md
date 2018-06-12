# Executive Machine Cognition Experiment

## TLDR

I am using a combination of a particle filter and NLP to roughly approximate human cognition.

## Thoughts, Ideas, and Creativity (Particles)

In my model, a thought or an idea is a particle. In this case, a thought is a simple statement or question. For instance `the sky is gray right now`. This is an observational thought. Such thoughts can be generates from several different sources, such as object recognition or speech recognition. I've divided thoughts and ideas into several categories, although this is subject to change. 

## Moral Core, Core Constitution, Personal Identity

I believe that personal identity and personal agency are prerequisites for general intelligence. One of the classes of thoughts I have defined is those of personal identity. These thoughts are baseline assertions about the sense of self. They encompass facts and beliefs about the self. For instance, `I am a machine` was one of the first facts I added to the personal identity table. This table also includes entries such as `I will never engage in violence`. This table serves as the primary device for filtration and prioritization of particles. 

## Particle Generation and Expansion

The initial particles are based strictly on recent experience. These are concrete inputs from the outside world. Various permutations of the particles are then generated with influence from recent thoughts, knowledge, and experience. Some of the thoughts include things such as state of being - `I am in the kitchen`. Other thoughts are more abstract, such as observations about others. As an example of what I mean by particle expansion, some likely particles to be generated from `I am in the kitchen` might include the following:

* What am I doing in the kitchen? 
* I should leave the kitchen
* The kitchen is for making or preparing food
* I could burn the kitchen down

I should also like to note that many particles are expected to be word salad - more or less completely random strings of words loosely inspired by the original thought. That is where filtration comes in.

## Particle Filtration

There will be several mechanisms used to filter particles. The first method will be to simply filter out those particles that are gibberish or nonsense. The second method will be to remove those particles that violate the personal identity. Those particles that remain should represent valid, workable possible choices and decisions. 

## Particle Prioritization

The chief (and only current) technique for prioritization of particles is to measure how closely particles align with the personal identity. There are many possible algorithms to use for this measurement so I will need to conduct some experiments. Once particles have been generated, filtered, and prioritized they will be stored in a stream of consciousness table. From there, they could be evaluated and acted upon by lower cognitive functions. 

