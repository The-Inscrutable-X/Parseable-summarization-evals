# Parseable Summarization: Basic Project Proposal
## Executive Summary
This project aims to make progress towards accurate evaluations of summarization by using the validation of Group Model Building methods within systems thinking as a case study. I will employ LLMs to analyze peer-reviewed literature to support or refute relations presented in causal loop diagrams. The final output of the LLMs’ analysis will be in a parseable format with a definite truth value, which may allow for more objective accuracy evaluation metrics compared to metrics such as ROGUE or METEOR that depend on similarity to human summaries. [2][3]
## Background and Introduction
Why Group Model Building?

Group Model Building (GMB) involves the utilization of communication with the community and domain knowledge to build graph based models. These methods are prone to bias and lead to inaccurate results. The difficulty of evaluating the quality of these models leads to highly varying quality amongst models and poses credibility challenges. By referencing literature we can use existing studies and peer-reviewed papers to evaluate the accuracy of these models relative to the current scientific consensus. 

Abstractive summarization using LLMs and simpler algorithms have been successfully applied to extract parseable information from scientific literature by analyzing sentences individually. [1]

The recent emergence of chat based LLMs such as GPT-3.5 conceivably gives us the ability to extract more nuanced information spread over multiple sentences or paragraphs. This is particularly useful for the task of literature analysis for GMB due to the qualitative and nuanced nature of literature relating to fields within which GMB is commonly applied. 

Causal loop diagrams (CLDs) relate variables such as community income level to community median house value. These variables can be concrete or more conceptual and harder to measure. For example academic stress and signs of depression. CLDs are directed graphs that relate these variables together in terms of causation and correlation. 

Academic literature can be “deterministically” analyzed by humans to find if a specific paper stated a correlation between predetermined variables. This knowledge can be used to generate an evaluation dataset by sourcing variables from existing CLDs.

## Objectives and Methods
Develop a proof of concept literature summarization system capable of receiving complete text from academic papers as input and output parseable information equivalent to the adjacency list of a directed graph to validate causal loop diagrams. 

Create a proof of concept evaluation metric based on ~10 relations sourced from a diverse set of ~10 CLDs and ~20 papers related to these relations.

Act as a case study for structured parseable summarization in general. Showing that “deterministic” means can be used to evaluate summarization. At least one iteration of the system will first produce a summary of all relations within the literature, then variable relations will be extracted from this summary, which will allow us to determine the comprehensiveness of summarization. 
## Methods and Scope
Current LLMs cannot produce consistent results on this task with prompting. Fine tuning, and feeding different data and prompts in stages will be required. 

References
[1]https://arxiv.org/abs/2303.05352  
[2]https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1204/reports/custom/report53.pdf
[3]http://nlpprogress.com/english/summarization.html
https://towardsdatascience.com/to-rouge-or-not-to-rouge-6a5f3552ea45 
https://arxiv.org/abs/2303.05352
https://towardsdatascience.com/how-to-evaluate-text-generation-models-metrics-for-automatic-evaluation-of-nlp-models-e1c251b04ec1
https://www.semanticscholar.org/reader/1cfe781523b4b3469d822bc52a0721b1c70cee5f
