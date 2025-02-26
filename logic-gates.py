import sys
import math

'''
A logic gate is an electronic device implementing a boolean function, performing a logical operation on one or more binary inputs and producing a single binary output.
Given n input signal names and their respective data, and m output signal names with their respective type of gate and two input signal names, provide m output signal names and their respective data, in the same order as provided in input description.
All type of gates will always have two inputs and one output.
All input signal data always have the same length.
The type of gates are :
AND : performs a logical AND operation.
OR : performs a logical OR operation.
XOR : performs a logical exclusive OR operation.
NAND : performs a logical inverted AND operation.
NOR : performs a logical inverted OR operation.
NXOR : performs a logical inverted exclusive OR operation.
Signals are represented with underscore and minus characters, an undescore matching a low level (0, or false) and a minus matching a high level (1, or true).
'''

# Define the results for each gate type
types = {
    "AND" : {"_" : {"_" : "_", "-" : "_"},
                   "-" : {"_" : "_", "-" : "-"}
    },
    "OR" : {"_" : {"_" : "_", "-" : "-"},
                  "-" : {"_" : "-", "-" : "-"}
    },
    "XOR" : {"_" : {"_" : "_", "-" : "-"},
                   "-" : {"_" : "-", "-" : "_"}
    },
    "NAND" : {"_" : {"_" : "-", "-" : "-"},
                    "-" : {"_" : "-", "-" : "_"}
    },
    "NOR" : {"_" : {"_" : "-", "-" : "_"},
                   "-" : {"_" : "_", "-" : "_"}
    },
    "NXOR" : {"_" : {"_" : "-", "-" : "_"},
                    "-" : {"_" : "_", "-" : "-"}
    }
}

# Initialization of variables
inputs = dict()
outputs = list()

# Get the number of inputs and number of outputs
n = int(input())
m = int(input())

'''
Get the inputs from the user and store them.
Example of input : "A __---_-__--_-"
Store the inputs in an associative array, like inputs["A"] = "__---_-__--_-"
'''
for i in range(n):
  input_name, input_signal = input().split()
  inputs[input_name] = input_signal

'''
Get the outputs from the user and store them.
Example of output : "C AND A B", so : output name, logic gate, and the two inputs we want to combine.
Store the outputs in an array, like outputs[0] = ["C","AND", "A", "B"]
'''
for i in range(m):
  output_name, _type, input_name_1, input_name_2 = input().split()
  outputs.append([output_name,_type, input_name_1, input_name_2])

# Echo the results
lastTrailingN = m-1
for i in range(m):

  # Gather the data
  output = outputs[i]
  output_name = output[0]
  signal_type = output[1]
  input_name1 = output[2]
  input_name2 = output[3]
  input_signal1 = inputs[input_name1]
  input_signal2 = inputs[input_name2]

  # Hopefully, the signals will have the same length, but if not, we will stop outputting when the shorter input stops.
  output_length = 0
  length1 = len(input_signal1)
  length2 = len(input_signal2)
  if(length1 == length2):
    output_length = length1
  else:
    if(length1 < length2):
      output_length = length1 
    else:
      output_length = length2

  # Echo the outputs
  print(output_name+" ", end="")
  for i_signal in range(output_length):
    signal1 = input_signal1[i_signal]
    signal2 = input_signal2[i_signal]
    print(types[signal_type][signal1][signal2], end="")

  if(i != lastTrailingN):
    print("")

  # To debug: print("Debug messages...", file=sys.stderr, flush=True)
