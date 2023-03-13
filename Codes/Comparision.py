import matplotlib.pyplot as plt
x = ['BILSTM', 'CHAR-ATTENTION', 'BILSTM-CRF',
     'BILSTM-GLOVE', 'BILSTM-WORD2VEC', 'BILSTM-FASTEXT']
y = [0.55, 0.58, 0.50, 0.5, 0.38, 0.20]
fig, ax = plt.subplots(figsize=(10, 10))
bars = ax.barh(x, y, 0.5)
for bar in bars:
    width = bar.get_width()  # Previously we got the height
    label_y_pos = bar.get_y() + bar.get_height() / 2
    ax.text(width, label_y_pos, s=f'{width}', va='center')
for tick in ax.yaxis.get_major_ticks():
    tick.label.set_fontsize(5)
for bar in bars[::2]:
    bar.set_color('r')
plt.title('Macro F1')
plt.xlabel('Macro F1 score')
plt.ylabel('Models')
plt.xlim([0.1, 0.6])
plt.show()
