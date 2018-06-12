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

# Model of Cognition

The model of cognition that I am working with is divided into roughly three tiers. 

## Executive Cognition

This experiment represents the uppermost tier of cognition. By 'uppermost' I mean that tier which is most abstracted from physical reality. Thoughts and ideas can exist completely independent of physical laws and limitations. Executive cognition is the thought that goes into high level decision making. This level of cognition happens exclusively in words. I have made this decision because using natural language and words immediately gives us tens of thousands of individual words and exponentially more ways to combine words to describe things and express ideas. 

## Lower Cognition

Lower cognition encompases cognitive functions that are more empirical or physical in nature. This includes things such as walking, speaking, grasping, and so on. These functions require some intelligence but are not themselves executive in nature. These functions are important problems to solve but are more of a means to an end. These types of cognition deal with converting numbers to words and vice versa. For instance, think about describing how you walk. You can articulate some aspects of walking, but many aspects of walking are simply beyond description. Those are aspects that you feel more than think. This is where the mind becomes abstracted away from the body. Lower cognition is the set of tools the mind has to interact with the body. 

## Peripheral Cognition

Peripheral cognition is where many domains of machine learning reside. This includes things like object recognition, classification and regression problems. These problems are closest to the 'real world'. These functions take raw data and/or information from the outside world and ascribe meaning to it. They take images and apply labels. They take sounds and apply labels. These describe the physical world around the machine. Peripheral cognition is the interfact between the mind and the outside world. 
