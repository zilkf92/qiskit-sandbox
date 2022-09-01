# qiskit-sandbox

## Adding Virtual Environment in Jupyter Notebook
The virtual environment in Python is separate from Jupyter Notebooks. A few things are required before your virtual environment can be used in the Jupyter Notebook. These quick instructions are taken from [Creating and Using Virtual Environment on Jupyter Notebook with Python](https://towardsdatascience.com/creating-and-using-virtual-environment-on-jupyter-notebook-with-python-db3f5afdd56a)

1. Activate virtual environment

```
pip install --user ipykernel
```

2. Add kernel

```
python -m ipykernel install --user --name=myenv
```

Now the venv kernel is set up and ready to be used in the Jupyter Notebook.

To remove the virtual environment from Jupyter execute

```
jupyter kernelspec uninstall myenv
```

and confirm to remove the kernel.