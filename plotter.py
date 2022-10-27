"""Creates three figures containing data from Iris plants
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

iris = pd.read_csv('iris.data', header=None)
iris.columns = ['sepal_width', 'sepal_length',
                'petal_width', 'petal_length', 'species']
measurement_names = ['sepal_width',
                     'sepal_length', 'petal_width', 'petal_length']
plt.figure()
plt.boxplot(iris[measurement_names], labels=measurement_names)
plt.ylabel('cm')
plt.savefig('iris_boxplot.png')
print('Saved iris_boxplot.png')
plt.close()

plt.figure()
for species_name in set(iris['species']):
    iris_subset = iris[iris['species'] == species_name]
    plt.scatter(iris_subset['petal_length'], iris_subset['petal_width'],
                label=species_name, s=5)
plt.legend()
plt.xlabel('Petal length')
plt.ylabel('Petal width')
plt.savefig('petal_width_v_length_scatter.png')
print('Saved petal_width_v_length_scatter.png')
plt.close()

fig, axes = plt.subplots(1, 2)
fig.set_size_inches(10, 5)
axes[0].boxplot(iris[measurement_names], labels=measurement_names)
axes[0].set_ylabel('cm')

for species_name in set(iris['species']):
    iris_subset = iris[iris['species'] == species_name]
    axes[1].scatter(iris_subset['petal_length'], iris_subset['petal_width'],
                    label=species_name, s=5)
axes[1].legend()
axes[1].set_xlabel('Petal length')
axes[1].set_ylabel('Petal width')
plt.savefig('multi_panel_figure.png')
print('Saved multi_panel_figure.png')
