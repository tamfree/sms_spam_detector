import pickle

def saveObject(in_obj, in_save_as_dot_pkl_filename):
    """
    A layer of abstraction to save Python objects.

    Parameters:
    - in_obj (Object): Object to be saved
    - in_save_as_dot_pkl_filename (str): Desired file name

    Returns:
    - text_clf (Pipeline): Fitted pipeline model for SMS classification.

    A layer of abstraction to save Python objects. The underlying means of saving may change over time. 
    It currently uses Pickle.
    """
    with open(in_save_as_dot_pkl_filename, 'wb') as file:
        pickle.dump(in_obj, file)

def readObject(in_file_name_of_saved_obj):
    """
    A layer of abstraction to retrieve saved Python objects.

    Parameters:
    - in_file_name_of_saved_obj (str): The filename of the saved object

    Returns:
    - the unpickled object save under the specified file name

    A layer of abstraction to retrieve saved Python objects. The underlying means of saving may change over time. 
    It currently uses Pickle.
    """
    with open(in_file_name_of_saved_obj, 'rb') as file:
        return (pickle.load(file))
    
#NTS Future: introduce naming conventions and model-specific overloading