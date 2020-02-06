from extractor import *
import matplotlib.pyplot as plt
plt.switch_backend('agg')
import os

OUTPUT_PATH='figures'

MARKERS = ['^', '<', 'o', 's']
HATCHES = ['//', '--', '\\\\', '||', '++', '--', '..', '++', '\\\\']
GRAYS = ['#2F4F4F', '#808080', '#A9A9A9', '#778899', '#DCDCDC', '#556677', '#1D3E3E', '#808080', '#DCDCDC']
COLORS = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']

def plot_batch_throughput(data, save_filename=None):

    fig, ax = plt.subplots(figsize = (8, 6))

    lengths = ['a', 'b', 'c', 'd']
    x_axis = list(data['batchsize'].drop_duplicates())
    x_axis.sort()
    lines = []
    for idx, length in enumerate(lengths):
        tmp_data = data[(data.length == length)]
        tmp_data = list(tmp_data.sort_values(by = ['batchsize'])['token/s'])
        #tmp_data = [tmp_data[0] / item for item in tmp_data]
        print tmp_data
        tx_axis = x_axis[:len(tmp_data)]
        #lines.append(ax.plot(x_axis, tmp_data, linewidth = 1.5, color = COLORS[idx], marker = MARKERS[idx], markersize = 14, markerfacecolor = 'none', label = kernel+"(%s)" % kl_abbr))
        #lines.append(ax.plot(x_axis, tmp_data, linewidth = 1.5, color = COLORS[idx], marker = MARKERS[idx], markersize = 14, markeredgecolor='k', markerfacecolor = 'none', label = kernel+"(%s)" % kl_abbr))
        lines.append(ax.plot(tx_axis, tmp_data, linewidth = 1.5, color = COLORS[idx], marker = MARKERS[idx], markersize = 14, markeredgecolor='k', markerfacecolor = 'none', label = length))

    ax.set_ylabel("token/s", size = 24)
    ax.set_xlabel("Batch Size", size = 24)
    ymax = ax.get_ylim()[1] * 1.15
    ymin = ax.get_ylim()[0] * 0.95
    ax.set_ylim(top = ymax, bottom = ymin)
    ax.yaxis.set_tick_params(labelsize=24)

    #ax.set_xlim(min(x_axis) - 100, max(x_axis) + 100)
    ax.set_xlim(min(x_axis) - 20, max(x_axis) + 20)
    ax.xaxis.set_tick_params(labelsize=24)

    ax.grid(color='#5e5c5c', linestyle='-.', linewidth=1)
    ax.legend(fontsize=24, loc='upper left')

    if not save_filename:# or True:
        plt.show()
	return
    else:
        plt.savefig(os.path.join(OUTPUT_PATH, '%s.pdf'%save_filename), bbox_inches='tight')
        plt.savefig(os.path.join(OUTPUT_PATH, '%s.png'%save_filename), bbox_inches='tight')


if __name__=='__main__':

    data = extract_data("v100_for_plot.xlsx")
    plot_batch_throughput(data, "test")
