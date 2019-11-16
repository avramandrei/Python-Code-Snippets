import argparse


def str2bool(arg):
    """
        Function that converts a string to its corresponding boolean value. Useful for command line argument conversion.

        Example:
            # the value of the 'is_true' argument will be interpreted as boolean
            parser.add_argument("--is_true", type=str2bool)


        Attributes:
            arg (str): Command line argument as string.

        Returns:
            The corresponding boolean value.

    """
    if isinstance(arg, bool):
       return arg
    if arg.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif arg.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')


