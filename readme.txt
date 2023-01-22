Topsis Score and Rank Calculator

I have created a Python package implementing Topsis(Technique for Order of Preference by Similarity to Ideal Solution) method used for multi-criteria decision analysis.


you just need to provide your input attributes using the command line and it will give you the results which will be displayed both on console and stored in a csv file provided as the last argument.


## Installation

$ pip install TOPSIS-101816021==0.0.1

In the commandline, you can run it in the following ways -
    $ python <package_name> <path to input_data_file_name> <weights as strings> <impacts as strings> <result_file_name>

E.g for input data file as data.csv, command will be like
    $ python topsis.py data.csv "1,1,1,1" "+,+,-,+" output.csv

This will print all the output attribute values along with the Topsis Core and Rank column, in a tabular format

License -> MIT