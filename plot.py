import numpy
import numpy as np
import matplotlib.pyplot as plt
import re
import os

# plot parameters
x_label_scale = 15
y_label_scale = 15
anchor_text_size = 15
show = True
save = False
save_file_type = '.pdf'
# problem params
n_j = 6
n_m = 6
l = 1
h = 99
stride = 50
datatype = 'vali'  # 'vali', 'log'

# Try both vanilla and PDR-suffixed filenames; use the first that exists
base_filename = f"./{datatype}_{n_j}_{n_m}_{l}_{h}.txt"
alt_filename = f"./{datatype}_{n_j}_{n_m}_{l}_{h}_PDR.txt"
candidate_files = [base_filename, alt_filename]
filename = next((p for p in candidate_files if os.path.exists(p)), None)
if filename is None:
    raise FileNotFoundError(
        f"Could not find any of: {', '.join(candidate_files)}.\n"
        f"Tip: If you're plotting PDR runs, logs are saved with the _PDR suffix."
    )

f = open(filename, 'r').readline()
if datatype == 'vali':
    obj = numpy.array([float(s) for s in re.findall(r'-?\d+\.?\d*', f)[1::2]])[:]
    idx = np.arange(obj.shape[0])
    # plotting...
    plt.xlabel('Iteration', {'size': x_label_scale})
    plt.ylabel('MakeSpan', {'size': y_label_scale})
    plt.grid()
    plt.plot(idx, obj, color='tab:blue', label='{}x{}'.format(n_j, n_m))
    plt.tight_layout()
    plt.legend(fontsize=anchor_text_size)
    if save:
        plt.savefig('./{}{}'.format('message-passing_time', save_file_type))
    if show:
        plt.show()
elif datatype == 'log':
    obj = numpy.array([float(s) for s in re.findall(r'-?\d+\.?\d*', f)[1::2]])[:].reshape(-1, stride).mean(axis=-1)
    idx = np.arange(obj.shape[0])
    # plotting...
    plt.xlabel('Iteration', {'size': x_label_scale})
    plt.ylabel('MakeSpan', {'size': y_label_scale})
    plt.grid()
    plt.plot(idx, obj, color='tab:blue', label='{}x{}'.format(n_j, n_m))
    plt.tight_layout()
    plt.legend(fontsize=anchor_text_size)
    if save:
        plt.savefig('./{}{}'.format('message-passing_time', save_file_type))
    if show:
        plt.show()
else:
    print('Wrong datatype.')



