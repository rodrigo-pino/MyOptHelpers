import numpy as np
from .OptTools import simplex, dual_simplex, gomori_pi, pep

def optimize(method:str, inital_table:np.ndarray, initial_base:list, usr_options:dict = dict()):
    options = set_options(usr_options)
    if method == "simplex":
        return simplex(inital_table, initial_base, options["slacks"], options["display"])

    if method == "dual-simplex":
        return dual_simplex(inital_table, initial_base, options["slacks"], options["display"])

    if method == "gomori-pi":
        return gomori_pi(inital_table, initial_base, options["slacks"], options["display"])

    if method == "pep":
        return pep(inital_table, initial_base, options["slacks"], options["display"])

    raise NotImplementedError(f"{method}")
    if method == "balas":
        pass

def set_options(usr_options:dict):
    options = {"slacks":0, "display":False}
    for opt in usr_options:
        try:
            options[opt]
            options[opt] = usr_options[opt]
        except KeyError:
            av_opt = "{" + ", ".join(opt for opt in options) + "}" 
            raise Exception(
                f"There is no option {opt}. Available options are:\n{av_opt}"
            )
    return options