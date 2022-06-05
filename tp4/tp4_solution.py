from logic import *

# Exercise TP 1

agent = PropKB()
P11, P12, P21, P22, P31, B11, B21 = expr('P11, P12, P21, P22, P31, B11, B21')
agent.tell(~P11)
agent.tell(B11 | '<=>' | ((P12 | P21)))
agent.tell(B21 | '<=>' | ((P11 | P22 | P31)))
agent.tell(~B11)
agent.tell(B21)

print(agent.ask_if_true(~P12))
print(agent.ask_if_true(P12))
print(agent.ask_if_true(~P22))
print(agent.ask_if_true(P22))
print(pl_resolution(agent,~P12))
print(pl_resolution(agent,P12))
print(pl_resolution(agent,~P22))
print(pl_resolution(agent,P22))

# Exercise TP 2

agentDC = PropDefiniteKB()
clauses = ['(B & F)==>E', 
           '(A & E & F)==>G', 
           '(B & C)==>F', 
           '(A & B)==>D', 
           '(E & F)==>H', 
           '(H & I)==>J',
           'A', 
           'B', 
           'C']

for c in clauses:
    agentDC.tell(expr(c))

print(pl_fc_entails(agentDC, expr('G')))
print(pl_fc_entails(agentDC, expr('H')))
print(pl_fc_entails(agentDC, expr('I')))
print(pl_fc_entails(agentDC, expr('J')))


agentDC2 = PropDefiniteKB()


clauses2 =  ['P ==> Q',
               '(L & M) ==> P',
               '(B & L) ==> M',
               '(A & P) ==> L',
               '(A & B) ==> L',
               'A', 'B']

for c in clauses2:
    agentDC2.tell(expr(c))
    
print(pl_fc_entails(agentDC2, expr('Q')))

