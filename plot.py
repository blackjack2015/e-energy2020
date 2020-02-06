from extractor import *
import matplotlib.pyplot as plt
plt.switch_backend('agg')
import os

OUTPUT_PATH='figures'

MARKERS = ['^', '<', 'o', 's', '+', 'x', 'D', '>']
HATCHES = ['//', '--', '\\\\', '||', '++', '--', '..', '++', '\\\\']
GRAYS = ['#2F4F4F', '#808080', '#A9A9A9', '#778899', '#DCDCDC', '#556677', '#1D3E3E', '#808080', '#DCDCDC']
#COLORS = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']
COLORS = ['C%d' % i for i in range(8)]

def plot_batch(data, attribute="throughput", keyword="token/s", save_filename=None):

    fig, ax = plt.subplots(figsize = (8, 6))

    lengths = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    x_axis = list(data['batchsize'].drop_duplicates())
    x_axis.sort()
    lines = []
    for idx, length in enumerate(lengths):
        tmp_data = data[(data.length == length)]
        tmp_data = list(tmp_data.sort_values(by = ['batchsize'])[keyword])
        #tmp_data = [item / tmp_data[0] for item in tmp_data]
        print(tmp_data)
        tx_axis = x_axis[:len(tmp_data)]
        #lines.append(ax.plot(x_axis, tmp_data, linewidth = 1.5, color = COLORS[idx], marker = MARKERS[idx], markersize = 14, markerfacecolor = 'none', label = kernel+"(%s)" % kl_abbr))
        #lines.append(ax.plot(x_axis, tmp_data, linewidth = 1.5, color = COLORS[idx], marker = MARKERS[idx], markersize = 14, markeredgecolor='k', markerfacecolor = 'none', label = kernel+"(%s)" % kl_abbr))
        lines.append(ax.plot(tx_axis, tmp_data, linewidth = 1.5, color = COLORS[idx], marker = MARKERS[idx], markersize = 12, markeredgecolor='k', markerfacecolor = 'none', label = length))

    ax.set_ylabel(keyword, size = 24)
    ax.set_xlabel("Batch Size", size = 24)
    ymax = ax.get_ylim()[1] * 1.15
    ymin = ax.get_ylim()[0] * 0.95
    ax.set_ylim(top = ymax, bottom = ymin)
    ax.yaxis.set_tick_params(labelsize=24)

    #ax.set_xlim(min(x_axis) - 100, max(x_axis) + 100)
    ax.set_xlim(min(x_axis) - 20, max(x_axis) + 20)
    ax.xaxis.set_tick_params(labelsize=24)

    ax.grid(color='#5e5c5c', linestyle='-.', linewidth=1)
    ax.legend(fontsize=24, loc='upper center', bbox_to_anchor=(0.5, 1.3), ncol = 4)

    if not save_filename:# or True:
        plt.show()
        return
    else:
        plt.savefig(os.path.join(OUTPUT_PATH, '%s.pdf'%save_filename), bbox_inches='tight')
        plt.savefig(os.path.join(OUTPUT_PATH, '%s.png'%save_filename), bbox_inches='tight')

def plot_length(data, attribute="throughput", keyword="token/s", save_filename=None):

    fig, ax = plt.subplots(figsize = (8, 6))

    batchsizes = [1, 8, 32, 64, 128, 256, 512, 1024]
    x_axis = list(data['length'].drop_duplicates())
    x_axis.sort()
    lines = []
    for idx, bs in enumerate(batchsizes):
        tmp_data = data[(data.batchsize == bs)]
        tmp_data = list(tmp_data.sort_values(by = ['length'])[keyword])
        #tmp_data = [item / tmp_data[0] for item in tmp_data]
        print(tmp_data)
        tx_axis = x_axis[:len(tmp_data)]
        #lines.append(ax.plot(x_axis, tmp_data, linewidth = 1.5, color = COLORS[idx], marker = MARKERS[idx], markersize = 14, markerfacecolor = 'none', label = kernel+"(%s)" % kl_abbr))
        #lines.append(ax.plot(x_axis, tmp_data, linewidth = 1.5, color = COLORS[idx], marker = MARKERS[idx], markersize = 14, markeredgecolor='k', markerfacecolor = 'none', label = kernel+"(%s)" % kl_abbr))
        lines.append(ax.plot(tx_axis, tmp_data, linewidth = 1.5, color = COLORS[idx], marker = MARKERS[idx], markersize = 12, markeredgecolor='k', markerfacecolor = 'none', label = bs))

    ax.set_ylabel(keyword, size = 24)
    ax.set_xlabel("Length", size = 24)
    ymax = ax.get_ylim()[1] * 1.15
    ymin = ax.get_ylim()[0] * 0.95
    ax.set_ylim(top = ymax, bottom = ymin)
    ax.yaxis.set_tick_params(labelsize=24)

    #ax.set_xlim(min(x_axis) - 100, max(x_axis) + 100)
    #ax.set_xlim(min(x_axis) - 20, max(x_axis) + 20)
    ax.xaxis.set_tick_params(labelsize=24)

    ax.grid(color='#5e5c5c', linestyle='-.', linewidth=1)
    ax.legend(fontsize=24, loc='upper center', bbox_to_anchor=(0.5, 1.3), ncol = 4)

    if not save_filename:# or True:
        plt.show()
        return
    else:
        plt.savefig(os.path.join(OUTPUT_PATH, '%s.pdf'%save_filename), bbox_inches='tight')
        plt.savefig(os.path.join(OUTPUT_PATH, '%s.png'%save_filename), bbox_inches='tight')


if __name__=='__main__':

    data = extract_data("v100_for_plot.xlsx")
    plot_batch(data, "throughput", "token/s", "batch_thrt")
    plot_batch(data, "power", "power", "batch_power")
    plot_batch(data, "latency", "latency", "batch_latency")
    plot_batch(data, "energy efficiency", "energy/token", "batch_ee")
    plot_length(data, "throughput", "token/s", "length_thrt")
    plot_length(data, "power", "power", "length_power")
    plot_length(data, "latency", "latency", "length_latency")
    plot_length(data, "energy efficiency", "energy/token", "length_ee")
