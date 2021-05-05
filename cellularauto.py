import numpy as np
import matplotlib.pyplot as plt


plt.rcParams['image.cmap'] = 'binary'      ###so that we get black and white simulations


def rule_index(triplet):                 ##gives you which index to access. Say we encounter 000, then index = 7-(0)=7
    L, C, R = triplet
    index = 7 - (4*L + 2*C + R)
    return int(index)



def one_d(initial_state, n_steps, rule_number):
    rule_string = np.binary_repr(rule_number, 8)
    rule = np.array([int(bit) for bit in rule_string])

    m_cells = len(initial_state)
    final = np.zeros((n_steps, m_cells))    # initalzing
    final[0, :] = initial_state           #first row

    for step in range(1, n_steps):
        triplets = np.stack([np.roll(final[step - 1, :], 1), final[step - 1, :], np.roll(final[step - 1, :], -1)] ) 
        #print(triplets[)  #np roll->Elements that roll beyond the last position are re-introduced at the first. 
        final[step, :] = rule[np.apply_along_axis(rule_index, 0, triplets)]

    return final



initial =np.zeros(100)
initial[50]=1
data = one_d(initial, 100, 30)
plt.imshow(data)
plt.show()

