import matplotlib.pyplot as plt
import numpy as np

# データ準備
Case = np.array(['L1_c1', 'L1_c2', 'L1_c3', 'I_c1 ', 'I_c2 ', 'I_c3 '])
Wway = np.array([ 308, 494, 388, 508, 707, 503])
Ures = np.array([2235, 2235, 1118, 456, 456, 228])
Psta = np.array([ 122, 122, 61, 122, 122, 61])
Coth = np.array([ 371, 371, 186, 358, 358, 179])
EadM = np.array([ 419, 463, 463, 420, 464, 464])
Bank = np.array([   0, 12, 6, 0, 12, 6])
Tsum = np.array([3754, 3996, 2491, 2154, 2409, 1667])
Wway = Wway + Psta + Bank
Oths = Tsum - EadM - Coth - Ures - Wway
xx = np.array([1, 2, 3, 5, 6, 7])

# 作図領域定義
cef = 1000
fsz = 12
fig = plt.figure(figsize=(7, 8), facecolor='w')
plt.rcParams["font.size"] = fsz
plt.subplot(111)
plt.xticks(xx, Case)
plt.xlim(0, 8)
plt.ylim(0, 6000 / cef)
plt.xlabel('Case')
plt.ylabel('Cost Index')
plt.grid(color='#999999', linestyle='--')

# 積み上げプロット
b0 = np.array([0, 0, 0, 0, 0, 0])
b1 = b0 + Oths / cef
b2 = b1 + EadM / cef
b3 = b2 + Coth / cef
b4 = b3 + Ures / cef
plt.bar(xx, Wway / cef, bottom=b4, width=0.8, align='center', label='Waterway')
plt.bar(xx, Ures / cef, bottom=b3, width=0.8, align='center', label='Upper Res.')
plt.bar(xx, Coth / cef, bottom=b2, width=0.8, align='center', label='Civil_others')
plt.bar(xx, EadM / cef, bottom=b1, width=0.8, align='center', label='E&M')
plt.bar(xx, Oths / cef, bottom=b0, width=0.8, align='center', label='Others')

# ９０度回転した説明書きの描画
stext = [' F-PSPP\n in Country-A', ' S-PSPP\n in Country-A', ' S-PSPP\n in Country-B']
plt.text(xx[0], Tsum[0] / cef, stext[0], rotation=90, va='bottom', ha='center', fontsize=fsz - 2)
plt.text(xx[1], Tsum[1] / cef, stext[1], rotation=90, va='bottom', ha='center', fontsize=fsz - 2)
plt.text(xx[2], Tsum[2] / cef, stext[2], rotation=90, va='bottom', ha='center', fontsize=fsz - 2)
plt.text(xx[3], Tsum[3] / cef, stext[0], rotation=90, va='bottom', ha='center', fontsize=fsz - 2)
plt.text(xx[4], Tsum[4] / cef, stext[1], rotation=90, va='bottom', ha='center', fontsize=fsz - 2)
plt.text(xx[5], Tsum[5] / cef, stext[2], rotation=90, va='bottom', ha='center', fontsize=fsz - 2)

# ボックス内説明書きの描画
ss1 = 'Site: L1, 1000MW x 8hr'
ss1 = ss1 + '\n' + 'Dam height     : 189m'
ss1 = ss1 + '\n' + 'waterway length: 2304m'
ss2 = 'Site: I , 1000MW x 8hr'
ss2 = ss2 + '\n' + 'Dam height     : 90m'
ss2 = ss2 + '\n' + 'waterway length: 5638m'
props = dict(boxstyle='round', lw=0.8, facecolor='#ffffff', alpha=1)
plt.text(2, 5100 / cef, ss1, color='#000000', fontsize=fsz - 1, va='bottom', ha='center', bbox=props)
plt.text(6, 3500 / cef, ss2, color='#000000', fontsize=fsz - 1, va='bottom', ha='center', bbox=props)

# 凡例とタイトル描画
plt.legend(shadow=True, loc='upper right')
plt.title('Comparison of Cost Index between Site-L1 and Site-I', loc='left', fontsize=fsz - 1)

# 画像の保存と画面描画
fnameF = 'fig_bar2.png'
plt.tight_layout()
plt.savefig(fnameF, dpi=100, bbox_inches="tight", pad_inches=0)
plt.show()
