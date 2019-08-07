from nice_plot import *

# fission spectrum
a = 0.988
b = 2.249
nerg = np.linspace(0.0, 10.0, 1000)
gerg = np.linspace(0.085, 8.0, 1000)
nspec = np.exp(-nerg / a) * np.sinh(np.sqrt(b * nerg))
gspec = []
for i in gerg:
    if i < .3:
        gspec.append(38.13 * (i - .085) * np.exp(1.648 * i))
    elif i < 1.0:
        gspec.append(26.8 * np.exp(-2.3 * i))
    else:
        gspec.append(8 * np.exp(-1.1 * i))
gspec = np.array(gspec)

nspec = nspec / max(nspec)
gspec = gspec / max(gspec)


plt.figure()
plt.plot(nerg, nspec, 'k-', label = 'neutron')
plt.plot(gerg, gspec, 'k--', label = 'gamma')
plt.xlabel('Energy (MeV)')
plt.ylabel('Norm. probability')
plt.legend(loc = 0)
plt.xlim((0, 6))
plt.grid()
plt.ylim(ymax = 1.05)
plt.savefig('ng_spec.png')
