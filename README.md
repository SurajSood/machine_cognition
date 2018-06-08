# cognitive chatbot experiment
experimental conversational microservice for maragi

# hypothesis

my underlying assumption is that chatbots fundamentally lack an identity as well as the concept of theory of mind. i've created a KB microservice to handle this where there are several tables to handle accumulated knowledge about various aspects of the world. 

# KB service

## identity table

The identity table will record facts about the chatbot, specifically that it is a machine as well as more information pertaining specifically to its sense of self, its 'personality' and so on. 

## chronology table

The chronology table is merely a logbook, recording events, decisions and observations with the context of time. This is meant to give the chatbot a linear sense of time. 

## people table

My fundamental belief is that "theory of mind" is merely a collection of assertions and observations about a person. This table is meant to record such assertions. Over time, this data could be used to anticipate a person's wants and needs.

## world table

This is where encyclopedic knowledge about the world is recorded. This data will come from various sources. In some cases it will be looked up via various APIs, dictionaries, Wikis, and so on. In other cases it will be derived from conversation. The fundamental goal of this table is to be able to learn naturally over time. 

# Convo service

This service is literally just to record conversational interactions. I said, you said, he said, she said. All with time context. 

# NLP service

This is a service meant to provide many tools and utilities for the purposes of comprehending sentences. This is largely an interpretive service, meant to enumerate the most likely meanings of inbound sentences. 

# Listening service

This service periodically queries the convo service to look for new incoming sentences. Upon receiving a sentence it feeds it to the NLP service to gain better understanding of the intent. This service will also query the KB service to augment the meaning of the sentence, including context in time and conversation. Once the incoming sentence has been fully compiled it is passed to the speaking service.

# Speaking service

Upon receiving a sentence concept the speaking service works on compiling a response. It operates essentially by association and elimination. Using information gathered by the listening service, the speaking service prioritizes ideas and facts. Once the payload has been pared down, the list of remaining ideas and facts are passed to the NLP service to be compiled into meaningful sentences, at which point the speech is logged into the convo service and presented to the outside world (either via chat window or vocalization)
