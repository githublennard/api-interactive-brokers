import argparse

parser = argparse.ArgumentParser()

# By default it will fail with multiple arguments.
parser.add_argument('--default')

# # # Telling the type to be a list will also fail for multiple arguments,
# # # but give incorrect results for a single argument.
# # parser.add_argument('--list-type', type=list)

# # # This will allow you to provide multiple arguments, but you will get
# # # a list of lists which is not desired.
# # parser.add_argument('--list-type-nargs', type=list, nargs='+')

# This is the correct way to handle accepting multiple arguments.
# '+' == 1 or more.
# '*' == 0 or more.
# '?' == 0 or 1.
# An int is an explicit number of arguments to accept.
#parser.add_argument('--nargs', nargs='+')
#parser.add_argument('DOWNLOADS', nargs='+', choices=['rock', 'paper', 'scissors'])
parser.add_argument('DOWNLOADS', nargs='+')##ESTE ES UN POSITIONAL ARGUMENTS ##POR ALGUNA RAZON TIENE PREPONDERANCIA SOBRE LOS OTROS 

##parsero.add_argument('DOWNLOADS1', nargs='+')##NO PUEDEN HABER DOS POSTIONAL ARGUMENTS EN UN MISMO CODIGO

#parser.add_argument('LIST', nargs='+')  ## SOLO UNO PUEDE ESTAR EN EL CODIGO

# To make the input integers
parser.add_argument('--nargs-int-type', nargs='+', type=int)##OPTIONAL ARGUMENT

# An alternate way to accept multiple inputs, but you must
# provide the flag once per input. Of course, you can use
# type=int here if you want.
parser.add_argument('--append-action', action='append')

# To show the results of the given option to screen.
for _, value in parser.parse_args()._get_kwargs():
    if value is not None:
        print(value)