from nlp import *   

regles = ProbRules(
S = "NP VP [0.6] | S Conjunction S [0.4]",
NP = "Pronoun [0.2] | Name [0.05] | Noun [0.2] | Article Noun [0.15] | Article Adjs \
Noun [0.1] | Digit [0.05] | NP PP [0.15] | NP RelClause [0.1]",
VP = "Verb [0.3] | VP NP [0.2] | VP Adjective [0.25] | VP PP [0.15] | VP Adverb \
[0.1]",
Adjs = "Adjective [0.5] | Adjective Adjs [0.5]",
PP = "Preposition NP [1]",
RelClause = "RelPro VP [1]"
)

lexique = ProbLexicon(
Verb = "is [0.5] | say [0.3] | are [0.2]",
Noun = "robot [0.4] | sheep [0.4] | fence [0.2]",
Adjective = "good [0.5] | new [0.2] | sad [0.3]",
Adverb = "here [0.6] | lightly [0.1] | now [0.3]",
Pronoun = "me [0.3] | you [0.4] | he [0.3]",
RelPro = "that [0.5] | who [0.3] | which [0.2]",
Name = "john [0.4] | mary [0.4] | peter [0.2]",
Article = "the [0.5] | a [0.25] | an [0.25]",
Preposition = "to [0.4] | in [0.3] | at [0.3]",
Conjunction = "and [0.5] | or [0.2] | but [0.3]",
Digit = "0 [0.35] | 1 [0.35] | 2 [0.3]"
)
 
grammaire =  ProbGrammar("TP 6", regles, lexique)
   

print(grammaire.isa('the','Article'))

print(grammaire.isa('1','Verb'))

print(grammaire.generate_random() )




    
