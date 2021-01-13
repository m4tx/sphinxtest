import io


def x_squared(x):
    """
    A function to return the square of X.

    Args:
        x (float): A float or numpy array

    Returns:
        float: The value of x-squared
    """
    return x*x


def x_cubed(x):
    """
    A function to return the cube of X.

    :param float x: a float
    :return: the value fo x-cubed
    :rtype: float
    """
    return x*x*x


def open_file():
    """
    Opens a file.

    See also: :py:func:`io.open`

    :return: opened file
    """
    return io.open('file', 'r')
