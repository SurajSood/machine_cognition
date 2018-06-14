# Executive Machine Cognition Experiment

## Hypothesis

Creativity and problem-solving can be approximated by simulating the human behavior known as "brain-storming" and then filtration based upon semantic relationships between a premise and an 'idea'. Where the premise is a sentence representing the goal or purpose and the idea is a spontaneously generated sentence. 

### Examples

For instance, consider the statement "The automobile will not start" and "The automobile is out of gas". The relationship between these two statements is effect/cause. The second sentence is a possible explanation for the first.

In this case, the first sentence could come from a human query or statement. The second sentence can easily be randomly created by generating random statements while using a KB system as a seed. 

This could work based on searching the KB for keywords - in thise case "automobile". Creating random permutations of a KB that contains facts such as "automobiles run on gasoline for fuel" could easily arrive at a statement such as "the automobile does not have fuel".
 
# Methods

## Particle Generation aka "Brainstorming"

Generate random sentences in three classes. 

* Interrogative
* Declarative
* Imperative

These random sentences can be compared to detected speech, memories, and personal morality for semantic relationships. The sentences should also be able to be created based upon an input seed. This will allow the generation of sentences related to a known topic.


## Particle Filtration

Identify semantic relationship between two given sentences. Filter or rank sentences based on relevant criteria or given task. 

* Cause/Effect (Action/Result)
* Antagonistic (Mutually exclusive?)
* Question/Answer (Query/Response)
* Similar meaning
* Related topic
* Unrelated

This will probably be best achieved by vectorizing sentences and training a deep neural network

# Data

## Knowledge

### Facts

Examples 

Subject | Verb | State
--- | --- | ---
the sky | is | blue
bacon | is | meat
I | am | human
kitchen | contains | sink
house | does not contain | giraffe
automobiles | require | gasoline

### Explanations

Fact | Rule | Reason
--- | --- | ---
the sky is blue | because of | nitrogren in the atmosphere
kitchen contains sink | for the purpose of | washing dishes
automobiles are made of steel | because | steel is strong and cheap
automobiles use gasoline | for the purpose of | chemical fuel for their internal combustion engine

## Perception

### Sight

Label | Class | Description | Identity
--- | --- | --- | ---
House | Building, structure | Burgundy, ranch style | My home
Dog | Animal, canine | Furry, german shepard | My dog named Bingo

### Sound

Label | Value | Description | Source
--- | --- | --- | ---
Speech | Go to the kitchen | Shouting, male | Person, human
Siren | emergency response vehicle | typical of American police cruiser | outside, distant
