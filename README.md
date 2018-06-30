# Hypothesis

Human thought can be roughly approximated using words

# Types of Knowledge

## Encyclopedic Knowledge

* "book learning"
* Dictionary definitions
* Abstract knowledge

## Personal Experience

* First-hand observations
* Hands-on experience
* Long term and short term memory

# Cognitive Concepts

## Subject Concept

* list of statements regarding a thing (topic, subject, event, etc)
* composed of encyclopedic knowledge and extended by personal experience
* can be used to keep track of thoughts and discussion points
* can be refined over time (filtered and augmented)

ex:

`[kitchen; a place to cook and prepare food; a room in a house or structure; typically contains an oven, microwave, or stove; my home has a kitchen; i visited my kitchen two hours ago; my home kitchen is located at X,Y,Z]`

## Action Concept

* very similar to subject concept
* focused on activities, methods and results
* can also be modified over time
* can be filtered or augmented based upon conversation, context, etc

ex:

`[clean; to remove dirt, debris and/or sanitize; typically performed with a cleaning implement and solvent; One typically uses an ammonia based cleaner and papertowels to clean windows; a broom and dustpan can be used to clean the floor; a window is considered clean when it is highly transparent, free of smudges and streaks; a floor is considered clean when it is free of dust and debris]`

## Compiling Concepts

Cognitive concepts can be compiled, filtered and augmented using several sources. 

* KB article system
* Encyclopedia system
* Dictionary systems
* Short term and long term memory system
* Conversational NLP systems

### Methods

Compiling concepts is relatively easy. There are several methods by which this can be done quickly and efficiently.

* Query sources for keywords, prioritize based upon recency
* Look up definitions, synonyms, hypernyms, hyponyms, and antonyms
* Augmenting concepts is roughly the same behavior as compiling concepts, just with more material already in place

## Filtering Concepts

Filtering cognitive concepts is highly critical as many words carry a lot of ambiguity and it is necessary to refine ideas during the course of conversation and to function independently. Filtering concepts is a bit more difficult.

### Methods

* Filter based on recency - in cases of ambiguity, favor terms and statements more similar to recent information
* Filter based on context - use broader context of conversation and surroundings to remove elements of a concept that are not relevant
* Filter based on conversation - talk about concepts and ask for clarification (also used for augmenting concepts)

# Concepts in Conversation

The purpose of the concept is to enable a machine to have a cohesive continuity of thought during a conversation.

Subject concepts can act as an organizational structure, roughly approximating short term memory during the course of a conversation. Concepts can be compiled and filtered autonomically by a MARAGI machine and then referenced as needed for dialog generation.

For example, if during the course of a conversation, a person informs you that they were born in Sweden, this fact can be added to a subject concept centered around that person. Thus, if they later refer to where they grew up, it can be inferred by the machine, using this concept, that they grew up in Sweden.

# Concepts in Planning

The purpose of action concepts is to map out actions, tasks, and plans in natural language such that they can be communicated and evaluated into real actions.

In the same way that subject concepts can serve as a vessel for short term memory while compiling and trimming (filtering) statements from a subject, so to can action concepts be refined when compiling and communicating tasks. The ability to dynamically compile and understand tasks is a critical function for general purpose robotics e.g. MARAGI

The action concept is a way for a machine to hold, in abstract, a task before executing so that the concept can be discussed and evaluated before being acted upon. This is necessary to handle the large degree of ambiguity in simple commands. It allows a MARAGI user to include things in the concept such as methods and definitions of done. Refer to the above concept of cleaning. 