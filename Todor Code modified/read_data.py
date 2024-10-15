import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
import sys
sys.path.append(r"C:\Users\kento\Documents\University of Manchester\University Work\Fourth Year\MPhys\MPhys---VUV-Photosensor-Testing-for-Neutrino-and-Dark-Matter-Detectors\utils")
# from plotting_utils import plot2d
import matplotlib.colors
import matplotlib.cm as colormap
from mpl_toolkits.axes_grid1 import make_axes_locatable
from configuration import PLOTS_FOLDER

def read_large_file(filename, loc=r"C:\Users\kento\Documents\University of Manchester\University Work\Fourth Year\MPhys\MPhys---VUV-Photosensor-Testing-for-Neutrino-and-Dark-Matter-Detectors\results\\"):
    """Read a single large file

    Parameters
    ----------
    filename : str
        filename
    loc : str, optional
        filepath, by default a Windows path

    Returns
    -------
    _type_
        _description_
    """
    all_waveforms = []
    raw_data = np.genfromtxt(loc + filename, skip_header=0, delimiter=',')
    new_waveform = np.array([[-1, -1]])
    for index, entry in enumerate(raw_data):
        if entry[0] < raw_data[index - 1, 0]:
            if index == 0:
                new_waveform = np.append(new_waveform, [entry], axis=0)
                continue
            new_waveform = np.delete(new_waveform, 0, axis=0)
            all_waveforms.append(new_waveform)
            new_waveform = np.array([[-1, -1], entry])
        else:
            new_waveform = np.append(new_waveform, [entry], axis=0)
            if index == len(raw_data) - 1:
                new_waveform = np.delete(new_waveform, 0, axis=0)
                all_waveforms.append(new_waveform)
                new_waveform = np.array([[-1, -1]])
    
    return all_waveforms

# if __name__ == "__main__":
all_waveforms = read_large_file("results_pmt-WA0049.csv", loc=r"C:\Users\kento\Documents\University of Manchester\University Work\Fourth Year\MPhys\results\\")

# loc = r"C:\Users\kento\Documents\University of Manchester\University Work\Fourth Year\MPhys\MPhys---VUV-Photosensor-Testing-for-Neutrino-and-Dark-Matter-Detectors\results\\"
# filename = "results_pmt-WA0049.csv"

# file_path = loc + filename
# print(f"Trying to open file: {file_path}")

# raw_data = np.genfromtxt(file_path, skip_header=0, delimiter=',')
# print(raw_data)