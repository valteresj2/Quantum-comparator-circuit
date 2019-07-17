# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 14:13:34 2019

@author: valter.e.junior
"""

import classe_circuit_Qcomparator as QC

QC.comparator(qubit=3,not_list=True).generate_result()

# parameter not_list is to remove or not the list item to be searched for.
# the end result is the number of times the observations were state zero and one, zero being the search item and 1 having the item in the list.
# the parameter qubit is the size of itens in to list

