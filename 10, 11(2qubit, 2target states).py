#!/usr/bin/env python
# coding: utf-8

# In[1]:


from qiskit.quantum_info import Statevector, Operator
from qiskit import QuantumCircuit, Aer, execute


# ### Q = HPHO = H (2 |00⟩ ⟨00| - I) H (I - 2 |10⟩ ⟨10| - 2 |11⟩ ⟨11|)

# In[2]:


qc = QuantumCircuit(2)
backend = Aer.get_backend('statevector_simulator')
result = execute(qc, backend).result()
state = result.get_statevector()
display("initialised |ψ0⟩", state.draw('latex'))
density_operator = state.to_operator()
#print(density_operator.data)
coherence = 0
for i in range(4):
    for j in range(4):
        if(i != j):
            coherence += abs(density_operator.data[i,j])
print("coherence of |ψ0⟩ = ",coherence)

qc.h([0,1])
result = execute(qc, backend).result()
state = result.get_statevector()
display("applied Hadamard to all |ψ1⟩", state.draw('latex'))
density_operator = state.to_operator()
#print(density_operator.data)
coherence = 0
for i in range(4):
    for j in range(4):
        if(i != j):
            coherence += abs(density_operator.data[i,j])
print("coherence of |ψ1⟩ = ",coherence)

#1st iteration
print("1st ITERATION OF GROVER'S OPERATOR")
O_operator = Operator([[ 1, 0, 0, 0],
                       [ 0, 1, 0, 0],
                       [ 0, 0,-1, 0],
                       [ 0, 0, 0,-1]])
qc.append(O_operator,[0,1])
result = execute(qc, backend).result()
state = result.get_statevector()
display("applied O operator to |ψ2⟩", state.draw('latex'))
density_operator = state.to_operator()
#print(density_operator.data)
coherence = 0
for i in range(4):
    for j in range(4):
        if(i != j):
            coherence += abs(density_operator.data[i,j])
print("coherence of |ψ2⟩ = ",coherence)

qc.h([0,1])
result = execute(qc, backend).result()
state = result.get_statevector()
display("applied Hadamard to all |ψ3⟩", state.draw('latex'))
density_operator = state.to_operator()
#print(density_operator.data)
coherence = 0
for i in range(4):
    for j in range(4):
        if(i != j):
            coherence += abs(density_operator.data[i,j])
print("coherence of |ψ3⟩ = ",coherence)

P_operator = Operator([[ 1, 0, 0, 0],
                       [ 0,-1, 0, 0],
                       [ 0, 0,-1, 0],
                       [ 0, 0, 0,-1]])
qc.append(P_operator,[0,1])
result = execute(qc, backend).result()
state = result.get_statevector()
display("applied P operator to |ψ4⟩", state.draw('latex'))
density_operator = state.to_operator()
#print(density_operator.data)
coherence = 0
for i in range(4):
    for j in range(4):
        if(i != j):
            coherence += abs(density_operator.data[i,j])
print("coherence of |ψ4⟩ = ",coherence)

qc.h([0,1])
result = execute(qc, backend).result()
state = result.get_statevector()
display("applied Hadamard to all |ψ5⟩", state.draw('latex'))
density_operator = state.to_operator()
#print(density_operator.data)
coherence = 0
for i in range(4):
    for j in range(4):
        if(i != j):
            coherence += abs(density_operator.data[i,j])
print("coherence of |ψ5⟩ = ",coherence)

#2nd iteration
print("2nd ITERATION OF GROVER'S OPERATOR")
qc.barrier()
O_operator = Operator([[ 1, 0, 0, 0],
                       [ 0, 1, 0, 0],
                       [ 0, 0,-1, 0],
                       [ 0, 0, 0,-1]])
qc.append(O_operator,[0,1])
result = execute(qc, backend).result()
state = result.get_statevector()
display("applied O operator to |ψ2⟩", state.draw('latex'))

qc.h([0,1])
result = execute(qc, backend).result()
state = result.get_statevector()
display("applied Hadamard to all |ψ3⟩", state.draw('latex'))

P_operator = Operator([[ 1, 0, 0, 0],
                       [ 0,-1, 0, 0],
                       [ 0, 0,-1, 0],
                       [ 0, 0, 0,-1]])
qc.append(P_operator,[0,1])
result = execute(qc, backend).result()
state = result.get_statevector()
display("applied P operator to |ψ4⟩", state.draw('latex'))

qc.h([0,1])
result = execute(qc, backend).result()
state = result.get_statevector()
display("applied Hadamard to all |ψ5⟩", state.draw('latex'))

#3rd iteration
print("3rd ITERATION OF GROVER'S OPERATOR")
qc.barrier()
O_operator = Operator([[ 1, 0, 0, 0],
                       [ 0, 1, 0, 0],
                       [ 0, 0,-1, 0],
                       [ 0, 0, 0,-1]])
qc.append(O_operator,[0,1])
result = execute(qc, backend).result()
state = result.get_statevector()
display("applied O operator to |ψ2⟩", state.draw('latex'))

qc.h([0,1])
result = execute(qc, backend).result()
state = result.get_statevector()
display("applied Hadamard to all |ψ3⟩", state.draw('latex'))

P_operator = Operator([[ 1, 0, 0, 0],
                       [ 0,-1, 0, 0],
                       [ 0, 0,-1, 0],
                       [ 0, 0, 0,-1]])
qc.append(P_operator,[0,1])
result = execute(qc, backend).result()
state = result.get_statevector()
display("applied P operator to |ψ4⟩", state.draw('latex'))

qc.h([0,1])
result = execute(qc, backend).result()
state = result.get_statevector()
display("applied Hadamard to all |ψ5⟩", state.draw('latex'))

qc.draw('mpl')


# ### coherence increases with H, remains constant with O, decreases with H, remains constant with P, then increases with H

# ### G = DO = (2 |ψ1⟩ ⟨ψ1| - I) (I - 2 |10⟩ ⟨10| - 2 |11⟩ ⟨11|)

# In[3]:


qc = QuantumCircuit(2)
backend = Aer.get_backend('statevector_simulator')
result = execute(qc, backend).result()
state = result.get_statevector()
display("initialised |ψ0⟩", state.draw('latex'))
density_operator = state.to_operator()
#print(density_operator.data)
coherence = 0
for i in range(4):
    for j in range(4):
        if(i != j):
            coherence += abs(density_operator.data[i,j])
print("coherence of |ψ0⟩ = ",coherence)

qc.h([0,1])
result = execute(qc, backend).result()
state = result.get_statevector()
display("applied Hadamard to all |ψ1⟩", state.draw('latex'))
density_operator = state.to_operator()
#print(density_operator.data)
coherence = 0
for i in range(4):
    for j in range(4):
        if(i != j):
            coherence += abs(density_operator.data[i,j])
print("coherence of |ψ1⟩ = ",coherence)

#1st iteration of Grover's operator
print("1st ITERATION OF GROVER'S OPERATOR")
O_operator = Operator([[-1, 0, 0, 0],
                       [ 0,-1, 0, 0],
                       [ 0, 0, 1, 0],
                       [ 0, 0, 0, 1]])
qc.append(O_operator,[0,1])
result = execute(qc, backend).result()
state = result.get_statevector()
display("applied O operator to |ψ2⟩", state.draw('latex'))
density_operator = state.to_operator()
#print(density_operator.data)
coherence = 0
for i in range(4):
    for j in range(4):
        if(i != j):
            coherence += abs(density_operator.data[i,j])
print("coherence of |ψ2⟩ = ",coherence)

D_operator = Operator([[-1/2, 1/2, 1/2, 1/2],
                       [ 1/2,-1/2, 1/2, 1/2],
                       [ 1/2, 1/2,-1/2, 1/2],
                       [ 1/2, 1/2, 1/2,-1/2]])
qc.append(D_operator,[0,1])
result = execute(qc, backend).result()
state = result.get_statevector()
display("applied D operator to |ψ5⟩", state.draw('latex'))
density_operator = state.to_operator()
#print(density_operator.data)
coherence = 0
for i in range(4):
    for j in range(4):
        if(i != j):
            coherence += abs(density_operator.data[i,j])
print("coherence of |ψ5⟩ = ",coherence)

#2nd iteration of Grover's operator
print("2nd ITERATION OF GROVER'S OPERATOR")
qc.barrier()
O_operator = Operator([[-1, 0, 0, 0],
                       [ 0,-1, 0, 0],
                       [ 0, 0, 1, 0],
                       [ 0, 0, 0, 1]])
qc.append(O_operator,[0,1])
result = execute(qc, backend).result()
state = result.get_statevector()
display("applied O operator to |ψ2⟩", state.draw('latex'))

D_operator = Operator([[-1/2, 1/2, 1/2, 1/2],
                       [ 1/2,-1/2, 1/2, 1/2],
                       [ 1/2, 1/2,-1/2, 1/2],
                       [ 1/2, 1/2, 1/2,-1/2]])
qc.append(D_operator,[0,1])
result = execute(qc, backend).result()
state = result.get_statevector()
display("applied D operator to |ψ5⟩", state.draw('latex'))

qc.draw('mpl')


# ### coherence increases with H, remains constant with O and D

# In[ ]:




