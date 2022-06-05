from logic import *
agent=PropKB()
P11, P12, P21, P22, P31, B11, B21 = expr('P11, P12, P21, P22, P31, B11, B21')

~P11
B11 | '<=>' | ((P12 | P21))
B21 | '<=>' | ((P11 | P22 | P31))
~B11
B21

agent.tell(~P11)
agent.tell(B11 | '<=>' | ((P12 | P21)))
agent.tell(B21 | '<=>' | ((P11 | P22 | P31)))
agent.tell(~B11)
agent.tell(B21)

#agent.ask_if_true(~P11)
#agent.ask_if_true(B11 | '<=>' | ((P12 | P21)))
#agent.ask_if_true(B21 | '<=>' | ((P11 | P22 | P31)))
#agent.ask_if_true(~B11)
#agent.ask_if_true(B21)
print(agent.ask_if_true(P12))
print(agent.ask_if_true(~P12))
print(agent.ask_if_true(P22))
print(agent.ask_if_true(~P22))

print(pl_resolution(agent,P12)
)
print(pl_resolution(agent,~P12)
)
print(pl_resolution(agent,P22)
)
print(pl_resolution(agent,~P22)
)
